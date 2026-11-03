# Contributing

Small, focused changes are welcome. This project aims to help agents make product-specific decisions, not add another fixed visual template.

## House rules

1. Every new `foldcheck.py` rule needs a fixture and a test. Document likely false positives.
2. Use `info` or `warn` for contextual visual patterns. Reserve errors for findings that indicate a likely implementation or content defect.
3. Generate documented contrast ratios with `scripts/contrast.py`; do not estimate them.
4. Keep `SKILL.md` focused on the reusable workflow. Put substantial guidance in a linked reference and deterministic mechanics in scripts.
5. Treat examples and style guidance as options. Do not claim that illustrative examples or passing scripts prove the skill improves design quality.
6. Python scripts use the standard library. `finish.mjs` uses Playwright only when it has been installed by the project.

## Local development

```bash
bash tests/run_tests.sh
python3 scripts/foldcheck.py --rules
python3 scripts/foldcheck.py examples/oscilla/index.html
python3 scripts/contrast.py "#201B12" "#F6F1E5"
python3 tests/check_ratios.py
```

To inspect an example in a browser, install Playwright in the project and run:

```bash
npm i -D playwright && npx playwright install chromium
node scripts/finish.mjs examples/oscilla/index.html
```

## Sending a change

Method changes should include the reason and the behavior they are intended to improve. Update the tests and docs when a script or reference changes. Pull requests should keep the suite green and update `CHANGELOG.md` under an Unreleased heading.

## Cutting a release

1. Update version metadata and add a dated changelog section.
2. Run the full suite and review the final diff.
3. Tag and publish the release from the repository's release workflow.
