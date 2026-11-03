---
name: slopless-ui
description: Design, implement, review, or improve user interfaces so their structure, content, visual language, and behavior fit the actual product instead of defaulting to interchangeable templates. Use for new pages and components, redesigns, UI fixes, and reviews of generic or AI generated interface work.
license: MIT
---

# Slopless UI

Help the user get a product-specific, usable interface. Do not replace one fashionable style with another, force novelty, or treat cards, gradients, color, fonts, shadows, motion, or minimalism as inherently good or bad. A choice earns its place when it serves the product, the user task, the content, an established brand, or a clear interaction need.

## Scale the work

- **Small fix or focused review:** inspect the affected view and its surrounding conventions. Keep the change narrow. Check the relevant behavior, responsive state, and accessibility details; report only checks that matter and were actually performed.
- **New component or page:** understand its users, task, content, and place in the product before choosing structure and styling. Define a brief design direction, implement the real states and interactions in scope, and inspect the result.
- **New product or substantial redesign:** inspect the project and its design system, establish the product context and information hierarchy, then record a concise design contract before implementation. Verify the important user journeys across relevant viewport conditions and refine concrete defects.
- **Review only:** do not edit. Separate functional, accessibility, responsive, content, and visual findings. Rank by impact and distinguish defects from subjective preferences.

Do not impose a full redesign, written ceremony, screenshot set, or exhaustive state inventory on a small request. Ask only when a missing decision blocks useful work. Otherwise use evidence in the project, make a bounded assumption, and label it when it affects the result.

## Build from product evidence

For existing work, first inspect the affected routes/components, tokens, assets, content/data, interaction flow, and available checks. Preserve the current product identity and working patterns unless the request or an observed problem justifies a change.

For substantial work, establish a compact product fingerprint: audience and context, primary task, important domain objects and relationships, real actions, content/data provenance, success condition, platform constraints, and known unknowns. Then form a design thesis that connects the task and domain to information priority and visual direction. Specificity comes from this connection, not from adding an unusual font, ornament, or animation.

Choose information structures to fit relationships: for example, compare with aligned values or a table, show ordered events as a timeline, manage work in a queue or board, and use cards when each object benefits from independent scanning or action. These are starting points, not prescriptions. Make a design contract only for substantial work; include the thesis, hierarchy/composition, type and semantic color roles, component conventions, responsive behavior, interaction principles, assets, and assumptions that will affect implementation.

Never invent production claims, capabilities, customer proof, or live metrics. Use supplied content and assets. If sample data is needed for a prototype, label it as sample and keep it plausible and internally consistent. Visible controls should do the action they promise within the requested scope, with clear feedback and recovery.

## Implement with judgment

Use the project's framework, components, tokens, and conventions. When creating a new system, define a small set of semantic roles and scales, then allow meaningful hierarchy and controlled variation. Use visual devices only when they communicate information, hierarchy, identity, orientation, or interaction. Repeated cards, eyebrow labels, all caps, icon tiles, uniform radii, gradients, pills, shadows, or a fashionable palette are review cues only: keep them when the brief and content justify them; revise them when they are interchangeable decoration.

Implement states that the actual component and flow require. Consider loading, empty, error, success, disabled, selected, permission, and long-content cases where applicable; do not manufacture state theatre. Motion is optional. Use it when it clarifies a change, gives feedback, or supports an intentional brand moment, and honor reduced-motion preferences. Do not add ambient motion merely to make a static page appear finished.

## Verify the result

Treat these as separate questions: does the application run, can people complete the task, does it work at relevant sizes and input modes, is it accessible, and does the visual direction fit the product? A passing linter or attractive screenshot cannot answer all of them.

Use the project's available tests and browser tools when relevant. Inspect the rendered interface when a browser is available, try the key interactions, and check the narrow layout and any breakpoint or content condition likely to fail. Run accessibility automation when available, then manually review keyboard/focus and semantics for the important flow. Fix high-impact defects and recheck the affected views. If a tool or state is unavailable, say so; never imply a check ran or that automation proves full accessibility.

The bundled `foldcheck.py` is a heuristic prompt for reviewing recurring patterns, not a style gate or an AI-authorship detector. Inspect its findings in context and keep justified choices. Use `contrast.py` for introduced color pairs when useful. Use `finish.mjs` only when Playwright is installed and the host does not offer a suitable browser. See [scripts/README.md](scripts/README.md) and [references/verification.md](references/verification.md).

## References

- Read [references/direction.md](references/direction.md) for product understanding and a design contract on new or substantially changed interfaces.
- Read [references/foundations.md](references/foundations.md) for information hierarchy, component choice, and meaningful pattern review.
- Read [references/responsive-design.md](references/responsive-design.md) for responsive engineering and accessibility checks.
- Read [references/verification.md](references/verification.md) for task-scaled browser, interaction, and reporting guidance.
- Read [references/anti-slop.md](references/anti-slop.md) when an interface feels generic; treat each pattern as a question, not a ban.
- Read [references/typography.md](references/typography.md) or [references/color.md](references/color.md) when choosing or reviewing those systems. Their examples are options, not defaults.
- Read [references/motion.md](references/motion.md), [references/copy.md](references/copy.md), or [references/icons-and-buttons.md](references/icons-and-buttons.md) when the task needs detail in that area.
- Read [references/evaluation.md](references/evaluation.md) when measuring whether a change to this skill improves outputs.

## Delivery

Summarize what changed, the main product or design decisions, the checks actually performed and their results, and any important unverified area. Keep the report proportionate to the request. A browser screenshot is evidence only if the rendered page was actually inspected. Never claim visual verification, accessibility conformance, or a successful test that was not established.
