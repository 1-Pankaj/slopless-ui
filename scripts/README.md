# Optional scripts

The scripts support review; none can decide whether a design fits its product.

| Script | Purpose | Requirements |
|---|---|---|
| `foldcheck.py` | Scans source for a subset of recurring UI and content patterns. It reports contextual cues plus likely implementation issues. | Python 3.8+ |
| `contrast.py` | Calculates contrast ratios for supplied foreground/background pairs. | Python 3.8+ |
| `finish.mjs` | Captures screenshots and checks browser errors and horizontal overflow. | Node 18+, Playwright |

Run paths relative to the skill folder:

```bash
python3 scripts/foldcheck.py src/                 # recursive scan
python3 scripts/foldcheck.py --rules              # list rules and severity
python3 scripts/foldcheck.py --strict src/        # warnings also fail
python3 scripts/foldcheck.py --format json src/   # machine-readable output
python3 scripts/contrast.py "#201B12" "#F6F1E5"  # one or more color pairs
node scripts/finish.mjs ./index.html              # browser review
```

`foldcheck.py` reserves errors for likely implementation/content defects. Pattern-based findings about typography, gradients, color, motion, copy, and component frequency are review cues and do not fail a build by themselves. Some heuristics can still misread source context. Check the location and rendered behavior. The scanner does not infer authorship or score design quality.

`contrast.py` computes a ratio for the values supplied. It does not determine which WCAG criterion applies, account for all visual context, or establish conformance.

`finish.mjs` is optional. Use an available host browser when possible. Screenshots expose visual issues, while viewport automation and console checks have limits. They do not establish usability or accessibility.

## Adding a rule

Every new rule needs a fixture and a test. Start with `info` or `warn` when a pattern needs human context. Use error only when the scanner has reliable evidence of a likely defect. Include the rule's known false positives in its message or documentation.
