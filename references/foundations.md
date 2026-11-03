# Information and component foundations

Use these checks when shaping a page, dashboard, or complex component. They guide decisions; they are not a fixed visual system.

## Let the task determine the structure

Start with the questions a user needs to answer and the actions they need to take. Map content relationships before choosing components.

| Content relationship | Useful starting structures |
|---|---|
| Compare attributes or values | Table, aligned rows, or comparison columns |
| Follow events or ordered work | Timeline, agenda, stepper, or queue |
| Find and manage a collection | Searchable list, board, table, or grouped collection |
| Inspect independent objects | Cards when separation improves scanning or action |
| Work with place, time, or hierarchy | Map, calendar, or tree when those relationships matter |

The same content may support several valid structures. Choose based on the user's task, amount of data, and interaction, not visual novelty. Use progressive disclosure when it reduces complexity without hiding information users need to decide.

## Build hierarchy from meaning

- Give urgent, actionable, and identity-setting content the emphasis it needs. Several things may deserve attention; do not force exactly one focal point when the task requires comparison.
- Group related content with proximity, alignment, headings, or surfaces. Use borders, color, and elevation where they clarify grouping, state, or interaction.
- Vary density by use. An operations view may need compact aligned rows; a reading view needs comfortable measure; a campaign page may use large imagery and display type.
- Use familiar conventions where they reduce learning effort. Break conventions only when the product context makes the benefit clear.
- Treat a repeated pattern as a signal to inspect hierarchy, not as proof that the pattern is wrong. Cards, badges, icons, labels, dividers, grids, and repeated layouts can be appropriate.

## Components and real behavior

Use native elements and existing design-system components where they fit. Make links navigate and buttons perform actions. Label form fields visibly and connect errors to their fields. Keep state names, feedback, and recovery consistent with the product vocabulary.

Implement only the states relevant to the actual flow. Check an empty collection, pending action, failed request, validation error, disabled action, success, selection, permissions, or unusually long content when that state can occur. A static icon or color change does not make a control functional.

Every visible element should have a reason a reviewer can name: information, hierarchy, identity, orientation, interaction feedback, or deliberate emotional tone. Remove or simplify elements that have no useful role, but do not remove necessary context merely to make a screen sparse.

## Content and data

Content is part of the interface model. Use real product terminology, meaningful labels, units, date formats, and realistic variation. Do not fabricate metrics, customer logos, testimonials, availability, live status, or capabilities. Clearly label synthetic data in prototypes. Check long names, missing values, zero states, and large quantities where they could change layout or interpretation.

## A concise critique

Review the proposal and rendered result against the same product thesis:

- Can a user identify the primary task and next action?
- Does information order match urgency and decision relevance?
- Do chosen components express the actual relationships?
- Does the page contain unsupported proof or decoration without a job?
- Is there consistency with enough variation to preserve hierarchy?
- Can the user understand outcomes, status, and recovery?

Record observable problems and their impact. Keep preference differences separate from usability or implementation defects.
