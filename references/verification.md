# Verification and critique

Use this before delivery, scaled to the changed surface and available tools. Verification is several distinct checks, not a single visual pass.

## Choose checks that answer the risk

For a small CSS or content fix, inspect the changed view and run a focused check. For an interactive component, exercise its important state transitions. For a new page or substantial redesign, run the application, inspect the key flow, check relevant narrow and wide layouts, and run the project's tests. Do not spend time generating an eight-viewport matrix when it adds no useful coverage.

Prefer project commands and a browser already available in the agent environment. If browser automation is absent, use an available preview or screenshot mechanism. If no rendered view can be inspected, review the implementation statically and report that visual behavior remains unverified.

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

Inspect the page at its actual rendering size. Check first-glance comprehension, information priority, grouping, consistency, typography, asset quality, spacing, and whether each prominent element serves the product thesis. Look for generic repetition, unsupported credibility claims, and controls that merely look interactive. A gradient, card, font, or animation is not itself a defect.

If screenshots are used for comparison, keep viewport, browser, operating system, fonts, data, and state consistent where possible. A screenshot baseline can expose changes but cannot decide whether the interface is good.

## Fix and stop

Fix problems that block the task, mislead users, hide content, break interactions, or create serious responsive/accessibility issues before polishing subjective details. Re-run checks relevant to the fixes. Stop when important defects are resolved or when a blocker cannot be tested in the environment; state the limit plainly.

## Report what happened

Name the check and result, for example: “Ran `npm test` (pass); verified the invite flow in Chromium at 390px and 1280px; axe reported no critical violations. Screen-reader behavior was not checked.” Do not use a generic verification badge. Separate automated results, manual inspection, and unavailable checks. Never infer full accessibility, field performance, or user success from a local screenshot or one automated scan.
