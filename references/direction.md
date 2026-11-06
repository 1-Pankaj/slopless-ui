# Product understanding and design direction

Use this for a new product, a new page with meaningful design freedom, or a substantial redesign. A one-line component correction does not need a full design brief.

## Inspect before proposing

For an existing product, examine the narrowest useful scope first: route and neighboring screens, component patterns, tokens, typography, icons and imagery, real content/data, key actions, and existing responsive behavior. Check the implementation and tests before assuming the screenshot tells the whole story. Keep brand and interaction conventions that are working.

For greenfield work, use the brief and available product materials. Do not pretend to know facts the user has not supplied. Ask when an unknown blocks a consequential decision; otherwise state a modest assumption and avoid building fake proof around it.

## Greenfield work and the /slopless-create protocol

When building a product, landing page, portfolio, or web application from scratch, trigger or follow `/slopless-create` (or `/slopless-ui create`). The discovery flow is governed by three strict rules to guarantee high taste while eliminating user annoyance:

### 1. The Context Pre-Check (Zero-Annoyance Rule)
Before asking ANY questions, inspect the user's prompt, uploaded documents (e.g., resumes, PRDs, specs), and workspace files:
- Did the user already supply project details, background history, target audience, preferred visual references, or key deliverables?
- **If YES:** **DO NOT ASK QUESTIONS.** Asking questions about details the user already provided is an immediate failure and frustrates the user. Extract the details silently, define the thesis, and jump directly to the Design Contract.

### 2. The Permission Gate (Never Ambush the User)
If the prompt is minimal or open-ended (e.g. "Build me a portfolio" with no other details):
- Never unleash a barrage of unprompted interview questions.
- Take permission first:
  > *"I have a strong baseline in mind, but to ensure this feels exactly right for you, would you like me to ask 2–3 quick questions to customize the mood and color palette, or should I propose a bespoke design contract right away?"*

### 3. Restrained, Tailored Customization (Max 2–3 Focused Choices)
If the user grants permission or explicitly asks to customize the direction, ask at most 2–3 high-value questions (using `ask_question` or multiple-choice options):
- **Question 1 (Atmosphere & Mood):** E.g. Warm Editorial Luxury vs. High-Trust Utilitarian vs. Architectural Brutalism vs. Tactile Artisanal.
- **Question 2 (Unexpected Premium Color Universe):** E.g. Roasted Espresso & Champagne Gold vs. Midnight Lapis & Pearl Ivory vs. Fired Terracotta & Bone vs. Deep Forest Moss & Chalk.
- **Question 3 (Primary Focus & Layout):** E.g. Direct Artifact Showcase vs. Typographic Statement with Split Spec vs. Interactive Product Flow.

Once answered, translate the choices immediately into the Design Contract and begin execution.

## Creative worldbuilding and conceptual art direction

The difference between competent generic software and an unforgettable digital experience is **creative worldbuilding**. A generic site arranges cards on a background. An exceptional site constructs an **atmospheric world** with its own physical rules, kinetic cadence, and sensory immersion.

### 1. The Core Creative Metaphor
Anchor the visual and interactive architecture in a singular creative metaphor rooted in the product's authentic domain:
- **The Oceanic Descent & Living Immersion:** A physical sensory journey through light and depth. The scroll position is tied directly to immersion depth meters (`#dp`), procedural shader surfaces shift dynamically, and generative Web Audio creates an ambient drone.
- **The High-Trust Developer Engine:** Terminal transparency, interactive code playgrounds, verifiable system topology diagrams, and live latency benchmarks with zero performative terminal fluff.
- **The Architectural Atelier:** Raw concrete and structural grid-lines, monumental display typography, tactile material textures, and sliding mechanical drawers.
- **The Bespoke Editorial Monograph:** High-contrast serif headlines, asymmetric column rhythms, pull-quotes, and quiet tactile paper tones.
- **The Sovereign Financial Ledger:** Audited precision tables, sober institutional contrast, immutable state badges, and transparent arithmetic previews.
- **The Scientific Observatory:** Deep optical fields, focal reticles, dynamic coordinate badges, and precise interactive telemetry.

### 2. Typographic Gravity as Architecture
Do not hide behind timid, interchangeable sans-serifs. Exceptional design uses typography with physical weight:
- Pair an uncompromising display face (**Dela Gothic One**, **Syne 800**, **Fraunces 900**) at monumental scale (`clamp(3.5rem, 13vw, 14rem)`) with a pristine, humanist body face (**Epilogue**, **Mona Sans**, **IBM Plex Sans**).
- Treat headlines as sculptural anchors that establish scale, depth, and shadow.

### 3. Sensory Immersion: Shaders and Sound
Interfaces that impress engage multiple sensory channels:
- **Procedural Canvas:** Use custom WebGL fragment shaders (`<canvas id="gl"></canvas>`) for living surfaces (wave dynamics, atmospheric clouds, raymarched light) rather than flat static colors or video loops.
- **Synthesized Audio:** Use the Web Audio API to generate low-overhead ambient drones, water soundscapes, or tactile click feedback that gives physical presence to digital interactions.
- **Living Lighting Models:** Support dynamic state transformations—such as a Day/Night toggle that updates GLSL shader uniforms, sun vectors, and text hues across the entire experience.

### 4. Layout Choreography: Rejecting the Card Kit
- Use full-height (`100svh`) section stages that reward exploration.
- Replace card grids with kinetic editorial rows (`.pj a:hover`) that slide laterally on hover with custom cubic-bezier curves.
- Use sticky sidebar anchors (`.stk`) to anchor high-level context while detailed content streams past.

## Product fingerprint

Capture only the details that will change the interface:

- Who uses it, in what context, and with what constraints?
- What is the primary task? What secondary tasks are in scope?
- What domain objects, relationships, and states make this product specific?
- What information and actions are actually available?
- Which content/data is supplied, synthetic, assumed, or unavailable?
- What platform, brand, technical, accessibility, and performance constraints apply?
- What observable outcome means the user succeeded?

## Design thesis

Write one or two sentences connecting the user's task and domain to the information priority and visual direction. Example: “A small engineering team uses this release console to catch blocked deploys. Lead with environment, owner, and last transition; reserve warning color for a deploy that needs intervention.” This thesis can produce a restrained operations tool, a colorful console, or something else if the evidence supports it.

Avoid generic goals such as “premium,” “modern,” or “beautiful” unless you translate them into choices and explain why those choices fit this product. Distinctiveness can come from real content, information density, composition, materials, voice, or restraint. Do not add novelty as a quota.

## Information hierarchy and composition

Before styling, list the information and actions the user needs, then order them by urgency, task relevance, and relationship. Select a composition that makes those relationships legible. Ask:

1. What should a user understand first?
2. Which items belong together, compare, follow a sequence, or require action?
3. What is the next useful action, and what feedback follows it?
4. Which content deserves emphasis, and which can remain quiet?
5. What changes when the viewport or input method changes?

Use actual product nouns and content to shape the page. Do not fill a layout with generic metrics, placeholder testimonials, random charts, or repetitive feature blocks to make it look complete.

## Design contract for substantial work

Record a short implementation guide in the working notes or report. Do not require a source-code comment or a ceremonial document for small changes.

- Thesis and the task the design prioritizes
- Information order and chosen composition
- Type roles and semantic color roles
- Spacing, sizing, surface, and component conventions
- Asset/icon direction and what each prominent visual element communicates
- Responsive and interaction behavior
- Assumptions that could change the result

The contract should be small enough to check against while implementing. Use semantic tokens when creating or changing a design system, but do not force identical values across roles that need distinct hierarchy.

## Uniqueness check

Before implementation, inspect the proposal for choices that could be copied unchanged to an unrelated product. Replace only the unsupported choices with decisions tied to the actual product, content, brand, or task. Do not respond by adding random asymmetry, a signature animation, an unusual typeface, or an “unexpected” accent. A familiar pattern is appropriate when it helps users recognize and complete the task.
