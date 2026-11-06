# Generic-interface review cues

These are the recurring tells of a generated interface. Each is a real signal: when you find one, replace it, or be able to say in one sentence why it serves this product. A pattern that repeats without a reason is the problem, and the replacement should come from the subject's world, not from the opposite fashion. Rows marked strict in `SKILL.md` (fake terminal chrome, fake device telemetry) are not up for negotiation unless the product really is a terminal or a device.

| Signal | Review question | Possible response when it has no good answer |
|---|---|---|
| The same card grid appears in every section | Are these distinct objects that benefit from separate scanning or actions? | Use a list, table, timeline, grouped text, or another structure that reflects the content. |
| Every feature has an icon, title, and short paragraph | Do the icons distinguish useful categories or aid recognition? | Remove redundant icons and let content hierarchy do the work. |
| Every heading has an eyebrow label or all-caps caption | Does the label add category, navigation, or status information? | Remove repeated decorative labels or use one only where it carries meaning. |
| A familiar gradient, glow, badge, pill, or shadow repeats | Does it establish identity, state, depth, or focus for this product? | Keep the best-supported instance and simplify the rest. |
| Every section is centered or follows the same hero/features/proof sequence | Does that composition serve the content and primary task? | Reorder around the information users need and use alignment appropriate to each section. |
| Numbers, charts, testimonials, logos, or activity make a page feel credible | Is each item sourced, current, and useful to a real decision? | Remove unsupported claims; label synthetic demo data clearly. |
| Buttons appear on every link or every action has equal emphasis | Do these actions perform distinct roles? | Use a link for navigation and reserve visual emphasis for the action priority the task supports. |
| Motion appears on every section or loops in a static context | Does it communicate a state or respond to an action? | Remove it or make the state and purpose clear; respect reduced-motion settings. |
| Copy uses polished but vague claims | Can it name the action, object, outcome, or evidence? | Replace it with specific, truthful language. |
| Monospace numbered section headings (`01 //`, `02 //`, `// SYSTEM`) | Does the interface model an actual CLI, terminal, or debugger tool? | Strictly eliminate faux-terminal section numbering. Use clean semantic headings (`<h2>`, `<h3>`) with natural sentence case and intentional typographic hierarchy. |
| Synthetic device mockups with fake telemetry dials (fake battery meters, simulated sensor rings, artificial gauges) | Is this an authentic product screenshot or real interactive application component? | Strictly eliminate artificial phone/tablet SVG bezels and fake gauge illustrations. Present real artifacts: authentic screenshots, interactive demos, verified architecture diagrams, clean code blocks, or editorial summaries. |
| Robotic developer jargon (`RUNTIME MATRIX`, `TAXONOMY BLUEPRINT`, `SENSOR TELEMETRY`) | Do these terms describe actual domain concepts or performative developer theater? | Replace with clear, human, authoritative explanations of what was engineered, how it performs, and why it matters. |
| Pitch-black obsidian paired with neon cyan/mint card borders and purple glows | Does this palette reflect an authentic brand or an unexamined AI sci-fi stereotype? | Derive a palette from the subject's world: one dominant color plus one shock accent resolved by value contrast (see `color.md`, e.g. Tomato Lagoon or Cobalt Lemon). |
| A selected typeface, palette, layout, or component repeats across unrelated products | Is it inherited from a real brand or chosen for a task-specific reason? | Revisit the design thesis rather than choosing an equally fashionable opposite. Do not take the first row of a table. |
| Cream or bone with terracotta, espresso with champagne gold, or near-black with acid green chosen by reflex as the "premium" look | Does the brief or brand ask for it? | A shock pairing from the subject's world. Keep these palettes for briefs that really fit them. |
| Space Grotesk, Inter, or Syne as the unexamined default display or body face | Was it chosen for this product, or is it the first font the model reaches for? | Rotate through the pairings in `typography.md` and choose by voice. |
| A fade-up on every section and a hover lift on every card | Does each one show a state change or answer an action? | One orchestrated load sequence, then scroll motion that varies by element (see `motion.md`). |
| The page is perfectly "clean" but has no memorable moment | Could anyone say in one sentence what this page is known for? | Find the signature (see `direction.md`) and build one moment with care. |

## A useful diagnostic

Imagine replacing the product name with an unrelated one. Which layout, labels, metrics, imagery, and interactions would remain unchanged? Those portions are generic and are candidates for revision. Tie important decisions to the real domain, data, user task, brand, or an established convention that helps users.

Removing tells does not make a design good. After the review, confirm the page still has a memorable first screen, a palette with a surprise in it, type with personality, and motion that feels like one system. A page that only lacks tells is merely neutral.

`foldcheck.py` detects a subset of code-level patterns. Read each finding with its location and context. It can miss rendered problems and flag valid choices; it cannot measure overall design quality or infer who created a page.
