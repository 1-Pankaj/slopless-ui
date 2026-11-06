# Evaluating changes to Slopless UI

Use this when assessing whether a revision to the skill improves actual work. A passing repository test suite confirms mechanics, not design effectiveness.

## Compare against a baseline

Run the same tasks with and without the skill using the same model/version, starting files, assets, tools, runtime, time or token budget, and evaluation criteria. Isolate each run in a clean copy. Record the condition, model and platform version, skill revision, tool versions, date, failures, and actual cost. Repeat noisy tasks; a small pilot helps debug the protocol but does not support strong general claims.

Include varied work: greenfield pages, data-dense interfaces, forms and workflows, mobile-first layouts, and changes inside an existing design system. Use some tasks that are not shown in examples as a holdout. Do not tune only for one landing-page prompt.

## Evaluate separate outcomes

Use independent tracks so visual polish cannot conceal functional problems:

- **Blind visual review:** randomize left/right order and ask reviewers about product fit, hierarchy, coherence, content fit, and execution. Do not tell them which version used the skill or ask only which looks AI-generated.
- **Function and usability:** exercise the advertised workflows; with representative users where possible, measure task completion, errors, recovery, and time.
- **Accessibility and responsive quality:** record automated findings and manual keyboard, focus, semantics, zoom/reflow, and viewport issues separately.
- **Engineering cost:** record time, iterations, tool calls, runtime failures, regressions, and maintenance impact.

Use more than one independent reviewer when possible and report disagreement. A proposed rubric or threshold is a team heuristic until validated; no one aesthetic preference, pattern count, or model self-rating proves quality.

## Optional starter rubric and prompts

This is a team heuristic until validated, useful for blind side-by-side review. Score each item 0 (generic), 1 (decent), or 2 (distinctive and well executed): memorable first screen, palette, typography, layout shaped by the content, motion as one system, human copy with nothing invented, flawless 390px behavior, states and details, and honesty of the handoff.

Starter prompts, to run at least twice per condition: a landing page for a luxury leather backpack brand (little context); a portfolio for a React Native developer from a supplied resume (real content); a redesign of a supplied generic dashboard (existing product); a pricing page for a log search tool (table versus card default, fake proof); a one-screen plant-watering app (small scope, states); and a loud site for a children's science museum (can it be bold without chaos).

Mechanical checks per run: no `lorem` or empty `alt`, no horizontal overflow at 320, 390, and 768, every text pair at AA contrast, no em dashes in visible copy, and no decorative infinite loops.

## Decide and maintain

Accept a change when it improves product-specific decisions or observable quality without materially harming task success, accessibility, responsiveness, performance, or cost. Keep failed cases and justified exceptions. Refresh tasks over time, preserve an untouched holdout, and revisit visual pattern cues as trends and model defaults change. A static detector may surface evidence for review; it must not infer authorship or declare an interface good or bad by itself.

## Research and practice references

- [UI-Bench](https://arxiv.org/abs/2508.20410) uses expert pairwise comparisons to evaluate generated interface design. Borrow the comparison method; its results do not establish this skill's effectiveness.
- [Sun and Baber, “How well can generative AI design and evaluate user interfaces?”](https://publications.ergonomics.org.uk/publications/how-well-can-generative-ai-design-and-evaluate-user-interfaces) reports a bounded study in which generative-system evaluations did not reliably align with human ratings. Do not rely on model self-critique as the sole evaluator.
- [Anthropic's frontend-design skill](https://github.com/anthropics/skills/tree/main/skills/frontend-design) is a maintained practitioner example of product-grounded visual choices and critique. It is a design reference, not an experiment proving effectiveness.
