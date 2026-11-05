# Optional scripts

The scripts support review; none can decide whether a design fits its product.

| Script | Purpose | Requirements |
|---|---|---|
| `foldcheck.py` | Scans source for a subset of recurring UI and content patterns. It reports contextual cues plus likely implementation issues. | Python 3.8+ |
| `contrast.py` | Calculates contrast ratios for supplied `#RGB` or `#RRGGBB` foreground/background pairs. | Python 3.8+ |
| `finish.mjs` | Captures screenshots and checks browser errors and horizontal overflow. Failed requests are warnings unless strict network mode is enabled. | Node 18+, Playwright |

Run commands from the project being checked. In this repository, the skill folder is the repository root, so these paths work directly. When the skill is installed elsewhere, replace `<skill-folder>` with the directory containing this `SKILL.md`; do not assume the agent's current project has a `scripts/` folder.

```bash
python3 "<skill-folder>/scripts/foldcheck.py" src/                 # recursive scan
python3 "<skill-folder>/scripts/foldcheck.py" --rules              # list rules and severity
python3 "<skill-folder>/scripts/foldcheck.py" --strict src/        # warnings also fail
python3 "<skill-folder>/scripts/foldcheck.py" --format json src/   # machine-readable output
python3 "<skill-folder>/scripts/contrast.py" "#201B12" "#F6F1E5"  # one or more hex pairs
node "<skill-folder>/scripts/finish.mjs" ./index.html              # browser review
```

On Windows, use `py -3` in place of `python3` when that is the available Python launcher. The repository test suite has a native Python runner: `py -3 tests/run_tests.py`; `bash tests/run_tests.sh` remains available where Bash is installed.

`foldcheck.py` reserves errors for likely implementation/content defects. Pattern-based findings about typography, gradients, color, motion, copy, and component frequency are review cues and do not fail a build by themselves. Some heuristics can still misread source context. Check the location and rendered behavior. The scanner does not infer authorship or score design quality.

The scanner recognizes gradients written with hex, HSL, or OKLCH colors and can expand CSS custom properties defined in the same scanned file. It cannot resolve the browser's cascade or variables defined only in imported stylesheets. Icon import counts cover Lucide, Heroicons, React Icons, Radix Icons, Tabler, Phosphor, Iconify, MUI, and Ant Design; they are still a review cue, not a component-count rule.

`contrast.py` accepts only 3- or 6-digit hexadecimal colors; it reports unsupported CSS color syntax as a usage error. It computes a ratio for the values supplied. It does not determine which WCAG criterion applies, account for all visual context, or establish conformance.

`finish.mjs` is optional. It resolves `playwright` or `playwright-core` from the project working directory, so run it with the checked project as the current directory. A global `playwright-cli` executable is not an importable Node package. Failed requests such as optional fonts or analytics are reported but do not fail the pass unless `--strict-network` is supplied. Use an available host browser when possible. Screenshots expose visual issues, while viewport automation and console checks have limits. They do not establish usability or accessibility.

## Adding a rule

Every new rule needs a fixture and a test. Start with `info` or `warn` when a pattern needs human context. Use error only when the scanner has reliable evidence of a likely defect. Include the rule's known false positives in its message or documentation.
