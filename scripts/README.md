# Scripts

Three small tools back the finishing pass. Zero dependencies (Python 3.8+ for the two Python scripts; Node 18+ only for the optional browser pass). No network calls, no telemetry.

| Script | What it does | Needs |
|---|---|---|
| `foldcheck.py` | Scans source files for machine-made patterns: looping decoration, default gradient heroes, glow and cyberpunk styling, emoji icons, icon and button spam, lorem ipsum, hotlinked stock images, em dashes, and more. | Python 3.8+ |
| `contrast.py` | WCAG 2.x contrast ratios for color pairs, with grades and a suggested passing shade. | Python 3.8+ |
| `finish.mjs` | Opens the page in a real browser: screenshots at desktop and phone widths, collects console and page errors and failed requests, fails on horizontal overflow. | Node 18+, Playwright (optional) |

## foldcheck.py

```bash
python3 foldcheck.py src/                  # scan a folder (recursive)
python3 foldcheck.py index.html styles.css # scan specific files
python3 foldcheck.py --rules               # list every rule with severity
python3 foldcheck.py --strict src/         # warnings also fail the run
python3 foldcheck.py --format json src/    # machine-readable output
python3 foldcheck.py --allow-infinite src/ # tolerate infinite animations
```

Exit code 0 when no errors. Warnings do not fail a normal run; fix them or note why they are intentional. The audit is static and heuristic: a clean run is permission to look at the rendered page, not proof of quality.

Skipped by default: `node_modules`, `.git`, `dist`, `build`, `coverage`, `.next`, `.nuxt`, `.cache`, `venv`, `__pycache__`, dot-directories, files over 1.5 MB, and binary files.

## contrast.py

```bash
python3 contrast.py "#201B12" "#F6F1E5"              # one pair: fg bg
python3 contrast.py fg1 bg1 fg2 bg2                  # several pairs
python3 contrast.py "#6D6455" "#F6F1E5" --suggest    # suggest a passing shade
python3 contrast.py "#C1502E" "#E7ECE9" --min 3.0    # large-text threshold
python3 contrast.py --pairs pairs.json               # [["fg","bg"], ...]
```

Grades: AAA (7:1 and up), pass (4.5:1 and up), large text only (3:1 to 4.5:1), fail. Exit code 1 when any pair is below the threshold.

## finish.mjs

```bash
node finish.mjs ./index.html                    # local file
node finish.mjs http://localhost:3000           # dev server
node finish.mjs ./index.html --widths 1440,768,390
node finish.mjs ./index.html --full             # full-page screenshots
node finish.mjs ./index.html --out verify-out   # where PNGs land
```

Install Playwright once per project:

```bash
npm i -D playwright && npx playwright install chromium
```

If Playwright is missing, the script explains that and exits with code 3 instead of pretending to verify. Any other browser tool works just as well; the required outcome is described in [../references/verification.md](../references/verification.md): screenshots at desktop and phone widths, zero console errors, and eyes on the result.

## Adding a foldcheck rule

Rules live in `foldcheck.py` as a regex plus one entry in `RULES`. When you add a rule: keep it zero-dependency, prefer `warn` until you have seen it misfire at least twice, and add a fixture in `../tests/fixtures/` with the expected exit code in the test runner.
