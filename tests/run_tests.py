#!/usr/bin/env python3
"""Cross-platform regression checks for the bundled skill scripts."""

import json
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
FOLDCHECK = ROOT / "scripts" / "foldcheck.py"
CONTRAST = ROOT / "scripts" / "contrast.py"


def run_python(script, *args):
    return subprocess.run(
        [sys.executable, str(script), *map(str, args)],
        cwd=str(ROOT), text=True, capture_output=True, check=False,
    )


class FoldcheckTests(unittest.TestCase):
    def scan(self, source, suffix=".tsx", *args):
        with tempfile.TemporaryDirectory(prefix="slopless-ui-") as directory:
            path = pathlib.Path(directory) / ("sample" + suffix)
            path.write_text(source, encoding="utf-8")
            return run_python(FOLDCHECK, *args, path)

    def test_rules_and_examples(self):
        rules = run_python(FOLDCHECK, "--rules")
        self.assertEqual(rules.returncode, 0, rules.stderr)
        self.assertEqual(len(rules.stdout.splitlines()), 29)
        self.assertEqual(run_python(FOLDCHECK, ROOT / "tests/fixtures/clean.html").returncode, 0)
        self.assertEqual(run_python(FOLDCHECK, ROOT / "tests/fixtures/sloppy.html").returncode, 1)
        for page in ("oscilla", "outerform", "nocturne"):
            before = json.loads(run_python(FOLDCHECK, "--format", "json", ROOT / "examples" / page / "before.html").stdout)
            self.assertGreater(before["summary"]["info"], 0)
            self.assertEqual(before["summary"]["error"], 0)
            self.assertEqual(run_python(FOLDCHECK, ROOT / "examples" / page / "index.html").returncode, 0)

    def test_comments_and_method_names_do_not_create_error_findings(self):
        result = self.scan(
            "// TODO fix later; prompt(\"old\")\n"
            "/* alert('removed'); */\n"
            "const result = agent.prompt('design');\n"
            "dialog.confirm('continue');\n"
            "// <img src=\"old.png\">\n"
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertNotIn("ALERT-DIALOG", result.stdout)
        self.assertNotIn("TODO-MARKER", result.stdout)
        html = self.scan("<script>\n// TODO prompt('old')\n</script>\n", ".html")
        self.assertNotIn("TODO-MARKER", html.stdout)
        self.assertNotIn("ALERT-DIALOG", html.stdout)
        prose = self.scan("<p>Use prompt() for the feature name, not a browser prompt.</p>\n", ".html")
        self.assertNotIn("ALERT-DIALOG", prose.stdout)
        html_script = self.scan("<script>window.confirm('Continue?')</script>\n", ".html")
        self.assertIn("ALERT-DIALOG", html_script.stdout)
        astro = self.scan("---\n// TODO remove\nconst name = agent.prompt('design');\n---\n<p>Done</p>\n", ".astro")
        self.assertNotIn("TODO-MARKER", astro.stdout)
        self.assertNotIn("ALERT-DIALOG", astro.stdout)
        markdown = self.scan("Visible copy. <!-- TODO: implementation note -->\n", ".md")
        self.assertNotIn("TODO-MARKER", markdown.stdout)
        scss_comment = self.scan("color: red;// TODO remove\n", ".scss")
        scss_url = self.scan(".hero { background: url(https://picsum.photos/800/600); }\n", ".scss")
        self.assertNotIn("TODO-MARKER", scss_comment.stdout)
        self.assertIn("HOTLINK", scss_url.stdout)

    def test_real_alert_is_still_reported(self):
        result = self.scan("window.alert('blocking');\n")
        self.assertEqual(result.returncode, 1)
        self.assertIn("ALERT-DIALOG", result.stdout)

    def test_multiline_img_alt_is_parsed_as_one_tag(self):
        valid = self.scan('<img\n  src="portrait.png"\n  alt="Portrait"\n/>\n', ".html")
        invalid = self.scan('<img\n  src="portrait.png"\n/>\n', ".html")
        quoted_angle = self.scan('<img src="photo>crop.png" alt="Portrait">\n', ".html")
        data_alt = self.scan('<img src="portrait.png" data-alt="not alternative text">\n', ".html")
        self.assertNotIn("IMG-NO-ALT", valid.stdout)
        self.assertIn("IMG-NO-ALT", invalid.stdout)
        self.assertNotIn("IMG-NO-ALT", quoted_angle.stdout)
        self.assertIn("IMG-NO-ALT", data_alt.stdout)

    def test_multiline_animation_exemption_is_scoped_to_css_rule(self):
        spinner = self.scan(
            ".spinner {\n  animation-name: spinner;\n  animation-iteration-count: infinite;\n}\n",
            ".css",
        )
        decorative = self.scan(
            ".orb {\n  animation-name: drift;\n  animation-iteration-count: infinite;\n}\n",
            ".css",
        )
        unrelated_word = self.scan(
            '.orb { content: "spinner"; animation-name: drift; animation-iteration-count: infinite; }\n',
            ".css",
        )
        self.assertNotIn("LOOP-INFINITE", spinner.stdout)
        self.assertIn("LOOP-INFINITE", decorative.stdout)
        self.assertIn("LOOP-INFINITE", unrelated_word.stdout)
        self.assertEqual(decorative.returncode, 0)

    def test_modern_gradient_formats_and_tailwind_full_radius_are_seen(self):
        result = self.scan(
            ".hero { background: linear-gradient(90deg, hsl(270 80% 50%), oklch(60% .2 300)); }\n"
            ":root { --brand-a: hsl(270 80% 50%); --brand-b: oklch(60% .2 300); }\n"
            ".theme { background: linear-gradient(90deg, var(--brand-a), var(--brand-b)); }\n",
            ".css",
        )
        self.assertIn("GRADIENT-HERO", result.stdout)
        self.assertGreaterEqual(result.stdout.count("GRADIENT-HERO"), 2)
        pill = self.scan('<span className="rounded-full px-3 py-1">New</span>\n')
        self.assertIn("PILL-DEFAULT", pill.stdout)
        self.assertEqual(result.returncode, 0)

    def test_supported_icon_libraries_are_counted(self):
        imports = (
            'import React from "react";\n'
            'import { Search, User, Bell, Menu } from "lucide-react";\n'
            'import { Home, ArrowLeft, ArrowRight } from "@heroicons/react/24/outline";\n'
            'import { FaSearch, FaUser } from "react-icons/fa";\n'
            'import { MagnifyingGlassIcon, PersonIcon } from "@radix-ui/react-icons";\n'
            'import { IconHome } from "@tabler/icons-react";\n'
        )
        result = self.scan(imports)
        self.assertIn("ICON-SPAM", result.stdout)
        self.assertIn("12 supported icon-library references", result.stdout)

    def test_style_cues_do_not_fail_default_or_strict_mode(self):
        source = "body { background: linear-gradient(90deg, #6366F1, #EC4899); }\n"
        self.assertEqual(self.scan(source, ".css").returncode, 0)
        self.assertEqual(self.scan(source, ".css", "--strict").returncode, 0)

    def test_achromatic_hsl_and_oklch_gradients_are_not_mislabeled_purple(self):
        source = ".neutral { background: linear-gradient(90deg, hsl(270 0% 50%), oklch(60% 0 300)); }\n"
        result = self.scan(source, ".css")
        self.assertNotIn("GRADIENT-HERO", result.stdout)
        self.assertNotIn("RAINBOW-GRADIENT", result.stdout)

    def test_terminal_chrome_and_fake_telemetry_detected(self):
        source = (
            "<h2>01 // PRODUCTION MODULE</h2>\n"
            "<div>CORE_ENGINE // OS</div>\n"
            "<span>telemetry blueprint</span>\n"
        )
        result = self.scan(source, ".html")
        self.assertIn("TERMINAL-CHROME", result.stdout)
        self.assertIn("FAKE-TELEMETRY", result.stdout)



class ContrastTests(unittest.TestCase):
    def test_known_ratios(self):
        checks = run_python(ROOT / "tests/check_ratios.py")
        self.assertEqual(checks.returncode, 0, checks.stdout + checks.stderr)
        self.assertEqual(run_python(CONTRAST, "#201B12", "#F6F1E5").returncode, 0)
        self.assertEqual(run_python(CONTRAST, "#999999", "#FFFFFF").returncode, 1)

    def test_missing_options_and_unsupported_colors_are_clean_usage_errors(self):
        for args in (
            ("--min",), ("--pairs",), ("--pairs", "--suggest"),
            ("#fff", "#fff", "--min"), ("--min", "0.5", "#fff", "#fff"),
            ("--min", "22", "#fff", "#fff"), ("--min", "inf", "#fff", "#fff"),
        ):
            result = run_python(CONTRAST, *args)
            self.assertEqual(result.returncode, 2, result.stdout + result.stderr)
            self.assertNotIn("Traceback", result.stderr)
        for color in ("#ffffff80", "rgba(0,0,0,.5)", "hsl(0 0% 0%)", "rebeccapurple"):
            result = run_python(CONTRAST, color, "#ffffff")
            self.assertEqual(result.returncode, 2, result.stdout + result.stderr)
            self.assertIn("Invalid color pair", result.stderr)
            self.assertNotIn("Traceback", result.stderr)
        with tempfile.TemporaryDirectory(prefix="slopless-ui-pairs-") as directory:
            pairs = pathlib.Path(directory) / "pairs.json"
            pairs.write_text(json.dumps([["#fff"]]), encoding="utf-8")
            result = run_python(CONTRAST, "--pairs", pairs)
            self.assertEqual(result.returncode, 2)
            self.assertIn("array of [foreground, background]", result.stderr)


class PackagingTests(unittest.TestCase):
    def test_python_sources_compile(self):
        for path in (FOLDCHECK, CONTRAST, ROOT / "tests/check_ratios.py", ROOT / "tests/run_tests.py"):
            compile(path.read_text(encoding="utf-8"), str(path), "exec")

    def test_frontmatter_and_local_references(self):
        skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        match = re.search(r"^---\n(.*?)\n---", skill, re.DOTALL)
        self.assertIsNotNone(match, "SKILL.md frontmatter missing")
        front = match.group(1)
        name = re.search(r"^name:\s*(.+)$", front, re.MULTILINE)
        description = re.search(r"^description:\s*(.+)$", front, re.MULTILINE)
        self.assertEqual(name.group(1).strip(), ROOT.name)
        self.assertTrue(description and len(description.group(1)) <= 1024)
        for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", skill):
            if target.startswith(("http://", "https://", "#", "mailto:")):
                continue
            self.assertTrue((ROOT / target.split("#", 1)[0]).is_file(), target)

    def test_examples_have_responsive_viewport_and_basic_motion_accessibility(self):
        for page in ("oscilla", "outerform", "nocturne"):
            text = (ROOT / "examples" / page / "index.html").read_text(encoding="utf-8")
            self.assertIn('name="viewport"', text)
            self.assertIn("prefers-reduced-motion", text)
            self.assertIn(":focus-visible", text)

    def test_node_script_parses_when_node_is_available(self):
        node = shutil.which("node")
        if not node:
            self.skipTest("Node.js is not installed")
        result = subprocess.run([node, "--check", str(ROOT / "scripts/finish.mjs")], cwd=str(ROOT), text=True, capture_output=True)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_finish_resolves_project_playwright_and_network_policy(self):
        node = shutil.which("node")
        if not node:
            self.skipTest("Node.js is not installed")
        with tempfile.TemporaryDirectory(prefix="slopless-ui-node-") as directory:
            project = pathlib.Path(directory)
            package = project / "node_modules" / "playwright"
            package.mkdir(parents=True)
            (package / "index.js").write_text(
                """
exports.chromium = {
  launch: async () => ({
    newContext: async () => ({
      newPage: async () => {
        const listeners = {};
        return {
          on: (name, callback) => { listeners[name] = callback; },
          goto: async (url) => {
            listeners.requestfailed({url: () => 'https://assets.test/font.woff2', failure: () => ({errorText: 'ERR_FAILED'})});
            listeners.console({type: () => 'error', text: () => 'Failed to load resource: net::ERR_FAILED'});
            listeners.response({status: () => 404, url: () => 'https://assets.test/favicon.ico', request: () => ({resourceType: () => 'image'})});
            if (url.includes('document-404')) {
              listeners.response({status: () => 404, url: () => url, request: () => ({resourceType: () => 'document'})});
            }
          },
          evaluate: async () => 0,
          waitForTimeout: async () => {},
          screenshot: async () => {},
          title: async () => 'Fixture',
        };
      },
      close: async () => {},
    }),
    close: async () => {},
  }),
};
""".lstrip(), encoding="utf-8",
            )
            script = str(ROOT / "scripts" / "finish.mjs")
            target = "https://fixture.test/"
            default = subprocess.run([node, script, target, "--widths", "390", "--out", "output"], cwd=str(project), text=True, capture_output=True)
            strict = subprocess.run([node, script, target, "--widths", "390", "--out", "output", "--strict-network"], cwd=str(project), text=True, capture_output=True)
            self.assertEqual(default.returncode, 0, default.stdout + default.stderr)
            self.assertIn("review warnings", default.stdout)
            self.assertIn("font.woff2", default.stdout)
            self.assertIn("favicon.ico", default.stdout)
            self.assertNotIn("console errors 1", default.stdout)
            self.assertEqual(strict.returncode, 1, strict.stdout + strict.stderr)
            self.assertIn("failed request", strict.stdout)
            document = subprocess.run([node, script, "https://document-404.test/", "--widths", "390", "--out", "output"], cwd=str(project), text=True, capture_output=True)
            self.assertEqual(document.returncode, 1, document.stdout + document.stderr)
            self.assertIn("document response", document.stdout)

    def test_finish_reports_missing_dependency_and_malformed_args_clearly(self):
        node = shutil.which("node")
        if not node:
            self.skipTest("Node.js is not installed")
        with tempfile.TemporaryDirectory(prefix="slopless-ui-empty-project-") as directory:
            script = str(ROOT / "scripts" / "finish.mjs")
            missing = subprocess.run([node, script, "https://fixture.test/", "--widths", "390"], cwd=directory, text=True, capture_output=True)
            self.assertEqual(missing.returncode, 3)
            self.assertIn("Install it in the project directory", missing.stderr)
            bad_args = subprocess.run([node, script, "https://fixture.test/", "--widths"], cwd=directory, text=True, capture_output=True)
            self.assertEqual(bad_args.returncode, 2)
            self.assertIn("--widths needs", bad_args.stderr)


if __name__ == "__main__":
    unittest.main(verbosity=2)
