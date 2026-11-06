# Responsive and accessible interface checks

Use this for web interfaces where layout or input behavior changes across viewports. Choose test conditions from the content, supported devices, and interaction model.

## Responsive engineering

Responsive design adapts information, layout, and interaction to available space and input. It is not simply a desktop layout stacked into one column.

- Prefer intrinsic, flexible sizing for content that varies. Use fixed dimensions only where the content or interaction needs them; let text wrap and media retain its proportions.
- Add a breakpoint when the current composition stops working. Verify close to each breakpoint instead of relying only on named device widths.
- Use container queries when a reusable component needs to respond to its own available width; use media queries when the viewport or user preference is the relevant condition.
- Check realistic content variation: long names, large values, localization, empty collections, validation, and loading. Do not hide overflow to conceal the element causing it.
- Preserve useful density and task priority on small screens. Reorder, summarize, disclose, or provide a contained two-dimensional view when the task requires it.
- Ensure touch, keyboard, and pointer users can reach the same essential content and actions. Hover may enhance an interaction but cannot be its only access path.
- Check sticky headers, bottom bars, dialogs, and virtual keyboards for overlap and focus obscuring when the interface uses them.
- Honor user preferences such as reduced motion and increased text size where relevant.
- Use `100svh` or `100dvh` instead of `100vh` for full-screen sections, give images and video an `aspect-ratio`, and add `env(safe-area-inset-*)` padding under fixed bars on phones.
- Size display type with `clamp()` so a monumental headline holds from 320px to 1920px, and add `overflow-wrap: anywhere` as a safety net for long words.
- Give navigation a deliberate small-screen treatment (a compact bar with the brand and one action plus a full-height menu), not a row of links shrunk to fit.
- Simplify signature moments for touch: a cursor effect becomes a still composition, and a heavy shader or pinned sequence gets a lighter or static version.

## Practical test selection

As a default for new pages and redesigns, check 390 (phone), 768 (tablet), and 1440 (laptop), plus 320 for navigation and large type. Do not treat these as mandatory breakpoints. Select a representative narrow phone width, the product's common phone/tablet/desktop widths, a wide layout, and widths immediately around actual breakpoints. For web reflow work, include the 320 CSS pixel condition where applicable. Include orientation, touch emulation, or zoom when the task makes them relevant.

At each useful condition check:

- Essential information and actions remain available and understandable.
- Text, controls, images, and data fit without unintended clipping or page-level horizontal overflow.
- Navigation and dense content have a deliberate small-screen treatment.
- Focus remains visible and unobscured; sticky surfaces do not cover content.
- Forms remain usable when the on-screen keyboard is present.

An intentional horizontally scrollable table, map, timeline, or canvas may need two-dimensional interaction. Keep that scrolling local and preserve access to all relevant information; do not mislabel it as a page-level reflow success.

## Accessibility checks

Use WCAG 2.2 as a standards reference when conformance is in scope. For routine implementation, check the criteria applicable to the changed interaction and document what was not assessed. Contrast ratios, touch target sizes, and other criteria include specific definitions and exceptions; do not convert them into context-free pixel rules. As practical references, WCAG 2.2 AA sets a 24 by 24 CSS pixel minimum target size (criterion 2.5.8, with exceptions), and 44 by 44 is a comfortable touch floor that also matches the AAA target size criterion. Automated scans catch only part of accessibility problems. Pair them with keyboard, semantics, content, zoom/reflow, and assistive-technology checks appropriate to the product and risk.
