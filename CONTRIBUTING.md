# Contributing

Small, sharp changes are welcome. This document is short on purpose.

## House rules

1. **Every new foldcheck rule ships with a fixture.** Add a file to
   `tests/fixtures/` that triggers the rule (or, for negative cases, a file
   that must stay clean) and extend `tests/run_tests.sh`. A rule without a
   fixture will misfire eventually.
2. **Prefer `warn` for new rules.** Promote a rule to `error` only after it
   has proven itself: you have run it on real projects and it has misfired at
   most once.
3. **Every contrast number in the docs comes from the script.** If you change
   a palette, run `python3 scripts/contrast.py` on every pair and paste the
   real numbers. Never estimate.
4. **One skill, one job.** SKILL.md holds the method; references hold depth;
   scripts hold mechanics. If a change makes SKILL.md longer, ask what can
   move to a reference instead.
5. **The repo follows its own rules.** No em dashes anywhere in this
   repository's text (CI checks; fixtures are the only exception), no emoji in
   documentation, no lorem ipsum, no invented numbers.
6. **Zero dependencies.** The Python scripts use the standard library only.
   `finish.mjs` treats Playwright as an optional, explicitly installed peer.

## Local development

```bash
bash tests/run_tests.sh        # the full suite, 29 checks
python3 scripts/foldcheck.py --rules
python3 scripts/foldcheck.py examples/oscilla/index.html   # the finished page passes
python3 scripts/foldcheck.py examples/oscilla/before.html  # the before page fails, on real patterns
python3 scripts/contrast.py "#201B12" "#F6F1E5"
python3 tests/check_ratios.py  # re-computes every ratio documented in color.md
```

To verify the example in a browser:

```bash
npm i -D playwright && npx playwright install chromium
node scripts/finish.mjs examples/oscilla/index.html
```

## Sending a change

Open an issue first for anything that changes the method, the non-negotiables,
or the meaning of an existing rule. Pull requests should keep the suite green
and update `CHANGELOG.md` under a new "Unreleased" heading.

## Cutting a release

1. Update the version badge in `README.md` and give `CHANGELOG.md` its new
   dated section.
2. Run the full suite. It must pass with zero failures.
3. Tag and publish:

```bash
git tag -a vX.Y.Z -m "slopless-ui vX.Y.Z"
git push origin vX.Y.Z
```

4. Create the GitHub Release from the tag, paste the matching CHANGELOG
   section into the notes, and attach the release zip (built without
   `__pycache__` and any local verification output).
