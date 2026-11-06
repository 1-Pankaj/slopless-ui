# Verification and critique

Use this before delivery, scaled to the changed surface and available tools. Verification is several distinct checks, not a single visual pass.

## Choose checks that answer the risk

For a small CSS or content fix, inspect the changed view and run a focused check. For an interactive component, exercise its important state transitions. For a new page or substantial redesign, run the application, inspect the key flow, check relevant narrow and wide layouts, and run the project's tests. Do not spend time generating an eight-viewport matrix when it adds no useful coverage.

Prefer project commands and a browser already available in the agent environment. If browser automation is absent, use an available preview or screenshot mechanism. If no rendered view can be inspected, review the implementation statically and report that visual behavior remains unverified.

## Look first (new pages and redesigns)

Reading your own code does not show what the page looks like. For a new page or a substantial redesign, do this before the tracks below, using the host's browser tool if it has one:

1. Load the page at 390 (phone), 768 (tablet), and 1440 (laptop) wide, and add 320 when navigation or large type could be tight. Screenshot each.
2. Run the **three-second test** (is there one memorable thing on the first screen?), the **phone test** (nothing overlaps, wraps badly, or scrolls sideways; check `document.documentElement.scrollWidth <= innerWidth`), and the **squint test** (shrink or blur the screenshot; hierarchy and a focal point must still read).
3. Scroll to the bottom, hover and tab through the controls, trigger every animation, interrupt one halfway, and reload with reduced motion enabled. Nothing should be missing.
4. Confirm the chosen fonts actually render and not the fallback, and that images load and keep their aspect ratio.
5. Fix what looks off, then look again, because every fix can break something else.

If you cannot open a browser, say so and list what stayed unverified. Never describe a visual result you did not see.

## Independent acceptance tracks

### Runtime and function

- Does the app start or build using the repository's documented workflow?
- Do the main actions perform the advertised operation and show a clear result?
- Do validation and failure paths explain what happened and how to recover?
- Are there relevant loading, empty, disabled, selection, permission, and long-content conditions to exercise?
- Are there console errors, failed assets, broken routes, or blocked controls in the tested flow?

### Responsive behavior

- Resize the relevant view across the width where its layout changes, including just before and after actual breakpoints.
- Check narrow reflow, clipped or overlapping content, long words, images, forms, navigation, data-dense content, and fixed/sticky UI where present.
- Test touch behavior when touch is a target input. Essential content and actions must not require hover.
- For web pages, consider WCAG 2.2 reflow at 320 CSS pixels (subject to the standard's exceptions for content that requires two-dimensional layout) and browser text zoom when applicable.

### Accessibility

- Check semantic names, labels, headings, status/error associations, keyboard order, visible focus, and operability of the important flow.
- Measure the text and control contrast pairs that changed. WCAG 2.2 AA contrast criteria are 4.5:1 for normal text, 3:1 for large text, and 3:1 for relevant non-text UI components; apply the full criterion and its exceptions rather than treating a color script as conformance.
- Use automated checks such as axe when available, but treat results as partial coverage. Automated pass is not proof of accessibility or WCAG conformance.
- Respect `prefers-reduced-motion` if the interface includes non-essential motion. Verify focus is not hidden behind author-created sticky content.

### Visual and content fit

Inspect the page at its actual rendering size. Check first-glance comprehension, information priority, grouping, consistency, typography, asset quality, spacing, and whether each prominent element serves the product thesis. Look for generic repetition, unsupported credibility claims, and controls that merely look interactive. A gradient, card, font, or animation is not itself a defect, but a decorative one with no job is. Check that the signature moment works and reads well on a phone.

If screenshots are used for comparison, keep viewport, browser, operating system, fonts, data, and state consistent where possible. A screenshot baseline can expose changes but cannot decide whether the interface is good.

## Fix and stop

Fix problems that block the task, mislead users, hide content, break interactions, or create serious responsive/accessibility issues before polishing subjective details. Re-run checks relevant to the fixes. Stop when important defects are resolved or when a blocker cannot be tested in the environment; state the limit plainly.

## Report what happened

Name the check and result, for example: “Ran `npm test` (pass); verified the invite flow in Chromium at 390px and 1280px; axe reported no critical violations. Screen-reader behavior was not checked.” Do not use a generic verification badge. Separate automated results, manual inspection, and unavailable checks. Never infer full accessibility, field performance, or user success from a local screenshot or one automated scan.

## Reading `foldcheck.py` results

- **`[error]`** (`LOREM`, `ALERT-DIALOG`, `IMG-NO-ALT`): fix before handoff.
- **`[warn]`** (`OUTLINE-KILL`, `TODO-MARKER`, `COMING-SOON`, `HOTLINK`, `TINY-TEXT`, `LOOP-INFINITE`): fix, or state why it is right for this product.
- **`[info]`**: the checker reports most visual patterns at this level so legitimate work is not blocked. That does not make them fine. For `EM-DASH`, `TERMINAL-CHROME`, `FAKE-TELEMETRY`, `GRADIENT-HERO`, `JARGON`, `ICON-SPAM`, and `BUTTON-SPAM`, either fix the finding or be able to say in one sentence why it serves this product. Use `--allow-infinite` only for a deliberate, state-bound or slow ambient effect, and mention it in the handoff.
