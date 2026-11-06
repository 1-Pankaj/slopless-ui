# Generic-interface review cues

These are recurring signals to investigate, not forbidden ingredients or proof of AI authorship. Keep a pattern when it fits the product and improves the experience. Revise it when it repeats without communicating a useful difference.

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
| Pitch-black obsidian paired with neon cyan/mint card borders and purple glows | Does this palette reflect an authentic brand or an unexamined AI sci-fi stereotype? | Replace with unexpected, high-taste premium color systems (e.g. Roasted Espresso & Champagne Gold, Midnight Lapis & Crisp Ivory, Fired Terracotta & Bone, Forest Moss & Chalk). |
| A selected typeface, palette, layout, or component repeats across unrelated products | Is it inherited from a real brand or chosen for a task-specific reason? | Revisit the design thesis rather than choosing an equally fashionable opposite. |

## A useful diagnostic

Imagine replacing the product name with an unrelated one. Which layout, labels, metrics, imagery, and interactions would remain unchanged? Generic portions are candidates for revision, not automatic failures. Tie important decisions to the real domain, data, user task, brand, or an established convention that helps users.

`foldcheck.py` detects a subset of code-level patterns. Read each finding with its location and context. It can miss rendered problems and flag valid choices; it cannot measure overall design quality or infer who created a page.
