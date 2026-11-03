#!/usr/bin/env python3
"""foldcheck.py: static review cues for recurring interface patterns.

Zero dependencies. Python 3.8+. Scans source files for the patterns listed in
references/anti-slop.md: blinking and looping decoration, default gradient
heroes, glow and cyberpunk styling, emoji as icons, icon and button spam,
placeholder content, hotlinked stock images, em dashes, and more.

Usage:
    python3 foldcheck.py src/ components/ index.html
    python3 foldcheck.py --rules          list every rule
    python3 foldcheck.py --strict src/    warnings also fail
    python3 foldcheck.py --format json src/
    python3 foldcheck.py --allow-infinite src/   do not flag infinite animations

Patterns are contextual cues, not style bans or authorship signals. Exit code 1
is reserved for likely implementation/content defects, not visual preferences.
"""

import argparse
import colorsys
import json
import os
import re
import sys

SKIP_DIRS = {
    "node_modules", ".git", "dist", "build", "coverage", ".next", ".nuxt",
    ".cache", "venv", ".venv", "__pycache__", ".svelte-kit", "vendor",
}

CODE_EXT = {".html", ".htm", ".css", ".scss", ".sass", ".less", ".js", ".jsx",
            ".ts", ".tsx", ".mjs", ".cjs", ".vue", ".svelte", ".astro",
            ".md", ".mdx", ".txt"}
CSS_EXT = {".css", ".scss", ".sass", ".less", ".vue", ".svelte", ".astro"}
JS_EXT = {".js", ".jsx", ".ts", ".tsx", ".mjs", ".cjs"}

MAX_BYTES = 1_500_000

JARGON = (
    "seamless|effortless|revolutionary|game-changing|cutting-edge|"
    "next-generation|best-in-class|world-class|state-of-the-art|"
    "unleash|supercharge|delve|tapestry|elevate|synergy"
)

RULES = {
    "EM-DASH": ("info", "Punctuation cue only. Keep it when it fits the product voice; review generic or repetitive copy in context."),
    "EN-DASH": ("info", "Punctuation cue only. Preserve intentional typography and the user's style."),
    "LOOP-INFINITE": ("warn", "Review whether the loop communicates real state or supports this product. Decorative motion is not automatically wrong."),
    "KEYFRAME-DECOR": ("info", "Review this motion in context. Keep it when it communicates state, interaction, or an intentional brand moment."),
    "GRADIENT-HERO": ("info", "A familiar gradient was found. Check whether it fits the brief; the pattern alone is not a defect."),
    "RAINBOW-GRADIENT": ("info", "A multi-hue gradient was found. Check its role, contrast, and fit with the product."),
    "TINY-TEXT": ("warn", "Check legibility, zoom, and the relevant text-size requirements; no universal 12px floor is assumed."),
    "GRADIENT-TEXT": ("info", "Check legibility and contrast in the rendered state; gradient text is not inherently a defect."),
    "TEXT-GLOW": ("info", "Check whether the effect supports identity or hierarchy and preserves legibility."),
    "BIG-GLOW": ("info", "Check whether this shadow communicates elevation or is decorative noise."),
    "CYBERPUNK": ("info", "Style cue only. Keep the direction when it matches the user's brief and the product."),
    "NEON-COLOR": ("info", "Color cue only. Check contrast, meaning, and product fit in context."),
    "EMOJI-ICON": ("info", "Check cross-platform rendering and accessible meaning; emoji may be appropriate as product content."),
    "ICON-SPAM": ("info", "Review whether each icon improves recognition or scanning; file count alone is not a defect."),
    "BUTTON-SPAM": ("info", "Review action hierarchy and semantics; button count alone is not a defect."),
    "LOREM": ("error", "Placeholder copy is present. Replace it or label the screen as a content prototype."),
    "COMING-SOON": ("warn", "Check whether this is an intentional product message or an unfinished placeholder."),
    "TODO-MARKER": ("warn", "Check whether this marker or unfinished work belongs in the shipped interface."),
    "HOTLINK": ("warn", "Check asset rights, reliability, and whether this is a placeholder URL."),
    "ALERT-DIALOG": ("error", "alert()/confirm()/prompt(). Use inline messages, dialogs, or toasts with role=status."),
    "IMG-NO-ALT": ("error", "<img> without alt text."),
    "OUTLINE-KILL": ("warn", "outline: none/0 with no :focus-visible replacement in this file."),
    "INTER-IDENTITY": ("info", "Check whether this typeface is a deliberate brand or product choice; do not reject it by default."),
    "JARGON": ("info", "Check whether this claim is concrete and truthful in context; vocabulary alone is not a defect."),
    "PILL-DEFAULT": ("info", "Check whether the shape communicates a chip, state, or brand choice."),
    "UPPERCASE-SPAM": ("info", "Check readability and whether casing carries useful hierarchy or category meaning."),
    "IMPORTANT-SPAM": ("info", "Frequent !important. Fix specificity instead."),
}

DECOR_KEYFRAMES = re.compile(
    r"@keyframes\s+[\w-]*(blink|pulse|bounce|float|glow|shimmer|flicker|neon|wiggle)[\w-]*",
    re.IGNORECASE,
)
GRADIENT = re.compile(r"(?:linear|radial|conic)-gradient\(([^;)]*)\)", re.IGNORECASE)
NAMED_PURPLE = re.compile(r"purple|indigo|violet|fuchsia|magenta", re.IGNORECASE)
HEX = re.compile(r"#[0-9a-fA-F]{3,8}")
GRADIENT_CLIP = re.compile(r"background-clip:\s*text", re.IGNORECASE)
FONT_SIZE_PX = re.compile(r"font-size\s*:\s*(\d+(?:\.\d+)?)px", re.IGNORECASE)
TEXT_SHADOW = re.compile(r"text-shadow\s*:", re.IGNORECASE)
BIG_SHADOW = re.compile(r"box-shadow\s*:[^;]*?(?:[4-9]\d|[1-9]\d\d)px", re.IGNORECASE)
CYBER = re.compile(r"\b(cyberpunk|synthwave|vaporwave|holographic|glitch)\b", re.IGNORECASE)
NEON_WORD = re.compile(r"\bneon\b", re.IGNORECASE)
NEON_HEX = re.compile(r"#(?:00ff00|39ff14|00ff41|ff10f0)\b|#0f0\b", re.IGNORECASE)
EMOJI = re.compile(
    "[\U0001F000-\U0001FAFF\u2600-\u26FF\u2700-\u27BF\u2B00-\u2BFF\uFE0F\u2049\u203C]"
)
LUCIDE = re.compile(r"data-lucide=|from\s+[\"']lucide-react[\"']", re.IGNORECASE)
BUTTON = re.compile(r"<button\b", re.IGNORECASE)
LOREM = re.compile(r"lorem\s+ipsum", re.IGNORECASE)
COMING = re.compile(r"coming\s+soon", re.IGNORECASE)
TODO = re.compile(r"\b(TODO|FIXME)\b")
HOTLINK = re.compile(r"(?:placehold\.co|via\.placeholder\.com|picsum\.photos|placekitten\.com|images\.unsplash\.com)", re.IGNORECASE)
ALERT = re.compile(r"\b(?:alert|confirm|prompt)\s*\(", re.IGNORECASE)
IMG = re.compile(r"<img\b(?![^>]*\balt=)[^>]*>", re.IGNORECASE)
OUTLINE_NONE = re.compile(r"outline\s*:\s*(?:none|0)\b", re.IGNORECASE)
FOCUS_VISIBLE = re.compile(r":focus-visible", re.IGNORECASE)
INTER = re.compile(r"font-family\s*:\s*[\"']?Inter\b[\"']?", re.IGNORECASE)
JARGON_RE = re.compile(r"\b(" + JARGON + r")\b", re.IGNORECASE)
PILL = re.compile(r"border-radius\s*:\s*(?:9999px|9999rem|100vmax|999px)", re.IGNORECASE)
UPPERCASE = re.compile(r"text-transform\s*:\s*uppercase", re.IGNORECASE)
IMPORTANT = re.compile(r"!important")
EM_DASH = re.compile("[\u2014\u2015]")
EN_DASH = re.compile("[\u2013]")

ANIMATION_INFINITE = re.compile(r"animation[^;]*\binfinite\b", re.IGNORECASE)
ANIMATION_EXEMPT = re.compile(
    r"spinner|loading|progress|skeleton|aria-busy|marquee|ticker", re.IGNORECASE
)


def hue_family(hex_text):
    """Return the HSV hue (degrees) and saturation for a hex color, else None."""
    text = hex_text[1:]
    if len(text) == 3:
        text = "".join(c * 2 for c in text)
    if len(text) not in (6, 8):
        return None
    try:
        r, g, b = (int(text[i : i + 2], 16) / 255.0 for i in (0, 2, 4))
    except ValueError:
        return None
    h, s, _v = colorsys.rgb_to_hsv(r, g, b)
    return h * 360.0, s


def is_default_gradient(args_text):
    """True when a gradient mixes two or more purple-family hues, or names them.

    The band starts at 235 degrees so the Tailwind indigos (indigo-500 sits
    near 239, indigo-600 near 243) count as the purple family; true blues sit
    below 225 degrees and stay out of it.
    """
    if NAMED_PURPLE.search(args_text):
        return True
    colors = [hue_family(m.group(0)) for m in HEX.finditer(args_text)]
    colors = [c for c in colors if c and c[1] > 0.15]
    purples = [c for c in colors if 235 <= c[0] <= 340]
    return len(purples) >= 2


def is_rainbow_gradient(args_text):
    """True when a gradient spans two or more saturated hues far apart on the wheel."""
    hues = [hue_family(m.group(0)) for m in HEX.finditer(args_text)]
    hues = [h for h, s in hues if s > 0.25]
    for i in range(len(hues)):
        for j in range(i + 1, len(hues)):
            distance = abs(hues[i] - hues[j])
            distance = min(distance, 360 - distance)
            if distance > 100:
                return True
    return False


def scan_file(path):
    """Return a list of findings for one file."""
    with open(path, "rb") as handle:
        raw = handle.read(MAX_BYTES + 1)
    if len(raw) > MAX_BYTES or b"\x00" in raw[:4096]:
        return []
    text = raw.decode("utf-8", errors="replace")
    ext = os.path.splitext(path)[1].lower()
    findings = []

    def add(rule, line_no, col, extra=""):
        severity, base_message = RULES[rule]
        message = base_message + (" " + extra if extra else "")
        findings.append((line_no, col, rule, severity, message))

    for line_no, line in enumerate(text.splitlines(), 1):
        stripped = line.strip()
        for match in EM_DASH.finditer(line):
            add("EM-DASH", line_no, match.start() + 1)
        if EN_DASH.search(line):
            add("EN-DASH", line_no, EN_DASH.search(line).start() + 1)
        if ANIMATION_INFINITE.search(line):
            if not (ANIMATION_EXEMPT.search(line) or ANIMATION_EXEMPT.search(stripped)):
                add("LOOP-INFINITE", line_no, line.lower().find("infinite") + 1)
        if DECOR_KEYFRAMES.search(line):
            add("KEYFRAME-DECOR", line_no, 1)
        for match in GRADIENT.finditer(line):
            if is_default_gradient(match.group(1)):
                add("GRADIENT-HERO", line_no, match.start() + 1)
            elif is_rainbow_gradient(match.group(1)):
                add("RAINBOW-GRADIENT", line_no, match.start() + 1)
        if ext not in {".md", ".mdx", ".txt"}:
            tiny = FONT_SIZE_PX.search(line)
            if tiny and float(tiny.group(1)) < 12:
                add("TINY-TEXT", line_no, tiny.start() + 1)
        if GRADIENT_CLIP.search(line):
            add("GRADIENT-TEXT", line_no, GRADIENT_CLIP.search(line).start() + 1)
        if TEXT_SHADOW.search(line):
            add("TEXT-GLOW", line_no, TEXT_SHADOW.search(line).start() + 1)
        if BIG_SHADOW.search(line):
            add("BIG-GLOW", line_no, 1)
        if CYBER.search(line):
            add("CYBERPUNK", line_no, CYBER.search(line).start() + 1)
        elif NEON_WORD.search(line):
            add("CYBERPUNK", line_no, NEON_WORD.search(line).start() + 1, '(the word "neon")')
        if NEON_HEX.search(line):
            add("NEON-COLOR", line_no, NEON_HEX.search(line).start() + 1)
        if ext not in {".md", ".mdx", ".txt"} and EMOJI.search(line):
            add("EMOJI-ICON", line_no, EMOJI.search(line).start() + 1)
        if LOREM.search(line):
            add("LOREM", line_no, LOREM.search(line).start() + 1)
        if COMING.search(line):
            add("COMING-SOON", line_no, COMING.search(line).start() + 1)
        if TODO.search(line):
            add("TODO-MARKER", line_no, TODO.search(line).start() + 1)
        if HOTLINK.search(line):
            add("HOTLINK", line_no, HOTLINK.search(line).start() + 1)
        if ext in JS_EXT and ALERT.search(line):
            add("ALERT-DIALOG", line_no, ALERT.search(line).start() + 1)
        if ext in {".html", ".htm"} or ext in JS_EXT:
            for match in IMG.finditer(line):
                add("IMG-NO-ALT", line_no, match.start() + 1)
        if INTER.search(line):
            add("INTER-IDENTITY", line_no, INTER.search(line).start() + 1)
        for match in JARGON_RE.finditer(line):
            add("JARGON", line_no, match.start() + 1, '(the word "{}")'.format(match.group(1)))
        if PILL.search(line):
            add("PILL-DEFAULT", line_no, PILL.search(line).start() + 1)
        if UPPERCASE.search(line):
            add("UPPERCASE-SPAM", line_no, UPPERCASE.search(line).start() + 1)
        if len(IMPORTANT.findall(line)) > 2:
            add("IMPORTANT-SPAM", line_no, 1)

    counts = {
        "lucide": len(LUCIDE.findall(text)),
        "button": len(BUTTON.findall(text)),
        "uppercase": len(UPPERCASE.findall(text)),
        "important": len(IMPORTANT.findall(text)),
    }
    if counts["lucide"] > 8:
        findings.append((0, 0, "ICON-SPAM", "info",
                         "{} icon references in one file; review them in the rendered context.".format(counts["lucide"])))
    if counts["button"] > 6:
        findings.append((0, 0, "BUTTON-SPAM", "info",
                         "{} <button> elements in one file; review semantics and hierarchy per view.".format(counts["button"])))
    if counts["uppercase"] > 3:
        findings.append((0, 0, "UPPERCASE-SPAM", "info",
                         "{} uppercase transforms in one file.".format(counts["uppercase"])))
    if counts["important"] > 3:
        findings.append((0, 0, "IMPORTANT-SPAM", "info",
                         "{} !important declarations in one file.".format(counts["important"])))
    if OUTLINE_NONE.search(text) and not FOCUS_VISIBLE.search(text):
        findings.append((0, 0, "OUTLINE-KILL", "warn",
                         "outline removed with no :focus-visible style in this file."))

    findings.sort(key=lambda f: (f[0], f[1]))
    return findings


def iter_files(paths):
    for root_path in paths:
        if os.path.isfile(root_path):
            yield root_path
            continue
        for current, dirs, names in os.walk(root_path):
            dirs[:] = [d for d in dirs if d not in SKIP_DIRS and not d.startswith(".")]
            for name in names:
                ext = os.path.splitext(name)[1].lower()
                if ext in CODE_EXT:
                    yield os.path.join(current, name)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("paths", nargs="*", help="files or folders to scan")
    parser.add_argument("--rules", action="store_true", help="list rules and exit")
    parser.add_argument("--strict", action="store_true", help="warnings also fail the run")
    parser.add_argument("--allow-infinite", action="store_true", help="do not flag infinite animations")
    parser.add_argument("--format", choices=["text", "json"], default="text")
    args = parser.parse_args(argv)

    if args.rules:
        for name, (severity, message) in RULES.items():
            print("{:16} [{:5}] {}".format(name, severity, message))
        return 0

    if not args.paths:
        parser.print_usage()
        print("Give at least one file or folder, or use --rules.")
        return 2

    report = {}
    for path in iter_files(args.paths):
        findings = scan_file(path)
        if args.allow_infinite:
            findings = [f for f in findings if f[2] != "LOOP-INFINITE"]
        if findings:
            report[path] = findings

    totals = {"error": 0, "warn": 0, "info": 0}
    for findings in report.values():
        for finding in findings:
            totals[finding[3]] += 1

    if args.format == "json":
        print(json.dumps({
            "files": {
                path: [
                    {"line": f[0], "col": f[1], "rule": f[2], "severity": f[3], "message": f[4]}
                    for f in findings
                ]
                for path, findings in report.items()
            },
            "summary": totals,
        }, indent=2))
    else:
        for path, findings in report.items():
            print(path)
            for line_no, col, rule, severity, message in findings:
                where = "{}:{}".format(line_no, col) if line_no else "file"
                print("  {:>8}  {:14} [{:5}] {}".format(where, rule, severity, message))
        file_count = len(report)
        print("\n{} file(s) with findings. {} error(s), {} warning(s), {} note(s).".format(
            file_count, totals["error"], totals["warn"], totals["info"]))

    failed = totals["error"] > 0 or (args.strict and totals["warn"] > 0)
    if args.format != "json":
        print("Fail. Review error findings as likely defects; see references/anti-slop.md." if failed
              else "No error-level findings. Review contextual cues and inspect the rendered result.")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
