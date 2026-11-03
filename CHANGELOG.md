# Changelog

All notable changes to slopless-ui are documented here. The format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/); versioning follows
[SemVer](https://semver.org/).

## [Unreleased]

### Changed

- Reframed the skill around product understanding, task-specific hierarchy, real content and behavior, and task-scaled verification.
- Replaced mandatory style prohibitions with contextual review cues; visual choices are evaluated against the product and user task.
- Reworked `foldcheck.py` so visual preferences are informational rather than build failures, and added tests to guard that behavior.
- Added responsive/accessibility guidance and a controlled evaluation protocol; corrected README and contributor docs to describe the project's evidence honestly.
- A restyle rule: changing only colors is a failed pass unless the brief
  argues why the page needs color alone. A "What failure looks like" section
  names the recolor as the standard failure.
- The brief gained a filled example, and the finishing pass gained a copy-off
  checklist (foldcheck, contrast, both screenshots, squint test, label) so
  the expected output shape is unambiguous.
- The frontmatter description is retuned for triggering: it now matches the
  small requests that used to fall through to a bare recolor ("change the
  colors", "tweak spacing", "polish", "fix responsiveness", "make it look
  modern") and states the recolor rule before the skill is even opened.
- The unused `docs/squint.png` is removed.

## [1.1.0] - 2026-11-02

The motion release. The skill now treats motion as a first-class craft axis
instead of a list of things not to do, and the examples moved from an
editorial register to the modern one.

### Added

- A code of conduct and a security policy for the repository.

### Changed

- `references/motion.md` rewritten as a constructive animation system: the
  motion budget (answers, one entrance, quiet reveals, one named ambient),
  entrance and scroll and hover choreography with numbers, the signature
  ambient rules, ticker discipline, pointer flourishes, spring parameters,
  frame and canvas rules, and a reduced-motion pass that keeps meaning while
  removing travel.
- `SKILL.md` now requires a motion pass as part of finishing, and bans the
  fully static page alongside the other machine-made patterns.
- README install section rewritten: the registry command first, a manual
  route and a directory table second, no narration.
- examples/README.md claims corrected to measured values: the finished
  pages' inline scripts bound at 209 lines, and the only external requests
  named as Google Fonts.
- A before-page placeholder email moved to the reserved .example domain.
- `references/direction.md` gains "The modern register": confident scale, a
  pulse, asymmetry on purpose, real content density. Print-flavored devices
  stay available as deliberate choices, not defaults. The example design
  contract now points at a modern build.
- `references/copy.md` gains the humanizer pass: eight ordered steps that turn
  correct copy into copy a person would have written.
- `references/anti-slop.md` and `references/verification.md` updated to match.
- The three example pairs were rebuilt in the modern register. The editorial
  pairs (print shop, warehouse dashboard, restaurant) are retired; the new
  pairs are oscilla (realtime audio API, dark, live waveform signature),
  outerform (product studio, light, cursor-chasing work previews), and
  nocturne (music festival, night palette, breathing ambient field). Every
  finished page now ships a small dependency-free script for its signature
  motion, and each before page still fails foldcheck on real patterns.
- Three palettes added to `references/color.md` (Volt, Signal, Nightbus),
  taking the library to twenty. Signal documents a 3.1:1 accent restricted to
  fills and large display text.

### Fixed

- `scripts/foldcheck.py` exempts named content tickers (`marquee`, `ticker`)
  from the infinite-loop rule, with the carve-out documented in the rule text
  and in the motion reference. The rule count is unchanged at 27, and the
  suite now pins that number.
- The test suite grew from 16 to 29 checks: the rule-count pin, the ticker
  exemption, and reduced-motion and scroll-reveal checks on every finished
  page.

## [1.0.0] - 2026-11-02

Initial release.

### Added

- SKILL.md: the five-step method (read the room, write the brief, decide as
  tokens, build with the grain, finish before delivery), the non-negotiables,
  the squint test, and the reporting rules.
- Nine reference documents: direction, foundations, typography, color,
  motion, copy, icons and buttons, the anti-slop catalogue, and verification.
- `references/direction.md`: the four-line brief, four modes (Persuade,
  Operate, Read, Experience), and a library of twenty-eight named style
  directions with a router from website category to starting point (SaaS,
  restaurants, fintech, travel, sports, gaming, kids, museums, industry,
  climate, and more).
- `references/foundations.md`: the laws real design systems run on. Spacing
  scales and the 4/8 point grid, layout and reading measure, hierarchy and
  the isolation effect, the eight component states, elevation and z-index
  discipline, keyboard and contrast floors, and the named UX laws (Jakob,
  Fitts, Hick, Miller, Doherty, Tesler, serial position,
  aesthetic-usability), each with its practical consequence.
- `references/typography.md`: the two-voice rule, the type scale, and
  twenty-five type pairings, every family OFL and verified against the
  google/fonts repository in November 2026.
- `references/color.md`: six-role palettes and seventeen authored palettes,
  every contrast ratio computed by the bundled script.
- `scripts/foldcheck.py`: a zero-dependency static audit with 27 rules for
  machine-made patterns, including the indigo-family gradient check that
  covers the Tailwind indigos.
- `scripts/contrast.py`: WCAG 2.x contrast grading with a suggested passing
  shade.
- `scripts/finish.mjs`: the optional Playwright browser pass with graceful
  fallback instructions.
- `references/motion.md`: motion built on response before animation. Press
  feedback on pointer-down, an interaction table with durations and curves
  for every common control, enter and exit on the same path, overlays
  anchored to their trigger with transform-origin, interruptible
  transitions, and a reduced-motion pass that keeps meaning while removing
  travel. Grounded in Apple's Designing Fluid Interfaces (WWDC 2018) and
  Material's motion guidance, translated to plain CSS.
- `references/copy.md`: the cadence rules, the quiet tell of machine text:
  varied sentence length, paragraphs that breathe unevenly, contractions,
  specifics over adjectives, and breaking the pattern on purpose.
- Three before/after example pairs, one per mode: Quarry Lane Press (print
  shop, Persuade, Ledger), Millrace Analytics (warehouse dashboard, Operate,
  Instrument), and The Copper Kettle (restaurant, Persuade, Brasserie).
  Each before page is a realistic unguided build that fails foldcheck on
  real patterns (em dashes, gradient headline text, slop vocabulary, the
  default identity font); each after page is the same business rebuilt with
  the skill, using a documented palette and pairing, with the design
  contract in a source comment.
- `tests/check_ratios.py`: re-computes every contrast ratio documented in
  `references/color.md` from the palette tables, so doc numbers cannot drift
  from the script.
- A 16-check test suite in `tests/run_tests.sh` and a GitHub Actions
  workflow running it on every push and pull request.
- Captured screenshots: each pair at desktop width, mobile views, side-by-
  side comparisons, and squint thumbnails.
