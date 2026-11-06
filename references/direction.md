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
- **Question 2 (Unexpected Color Universe):** E.g. a bold shock-color palette (Tomato Lagoon, Cobalt Lemon) vs. Midnight Lapis & Pearl Ivory vs. Deep Forest Moss & Chalk vs. Roasted Espresso & Champagne Gold. Every list accepts "describe your own", and the chosen option should be mutated toward the product rather than copied.
- **Question 3 (Primary Focus & Layout):** E.g. Direct Artifact Showcase vs. Typographic Statement with Split Spec vs. Interactive Product Flow.

### 4. Non-interactive hosts
If the host cannot ask questions or the user is unavailable, skip the gate, state your assumptions in one line, write the Design Contract, and build.

Once answered, translate the choices immediately into the Design Contract and begin execution.

## Creative worldbuilding and conceptual art direction

The difference between competent generic software and an unforgettable digital experience is **creative worldbuilding**. A generic site arranges cards on a background. An exceptional site constructs an **atmospheric world** with its own physical rules, kinetic cadence, and sensory immersion.

### 0. Find the world, then commit to one signature

1. Write down what this is, who uses it, and **six concrete nouns from its world**: materials, objects, tools, slang, places, textures. A coffee roaster gives you chaff, burlap stencils, a thermometer dial, a roast curve. A freight company gives you pallet labels, hazard diamonds, dock numbers.
2. Convert each noun into a possible decision. A thermometer dial can become the section divider. Burlap stencil lettering can drive the display face. A roast curve can become a scroll-linked line that ties sections together.
3. Write **three directions** in one line each that differ on at least two axes (density, color temperature, type contrast, layout structure, tone): one loud, one quiet, one strange. Pick one.
4. Name its **signature**, the single memorable thing, and keep everything else quieter so it can carry the page. If you removed it, the page should become interchangeable with others. If not, it is not strong enough.
5. Run the **transplant test** (see Uniqueness check below).

### 1. The Core Creative Metaphor
Anchor the visual and interactive architecture in a singular creative metaphor rooted in the product's authentic domain. These are examples, not a menu; invent a better one when the subject allows:
- **The Oceanic Descent & Living Immersion:** A physical sensory journey through light and depth. The scroll position is tied directly to a depth meter, procedural shader surfaces shift dynamically, and generative Web Audio creates an ambient drone. This is a world for aquatic or immersive subjects; do not reuse it for unrelated products.
- **The High-Trust Developer Engine:** Terminal transparency, interactive code playgrounds, verifiable system topology diagrams, and live latency benchmarks with zero performative terminal fluff.
- **The Architectural Atelier:** Raw concrete and structural grid-lines, monumental display typography, tactile material textures, and sliding mechanical drawers.
- **The Bespoke Editorial Monograph:** High-contrast serif headlines, asymmetric column rhythms, pull-quotes, and quiet tactile paper tones.
- **The Sovereign Financial Ledger:** Audited precision tables, sober institutional contrast, immutable state badges, and transparent arithmetic previews.
- **The Scientific Observatory:** Deep optical fields, focal reticles, dynamic coordinate badges, and precise interactive telemetry.

### 2. Typographic Gravity as Architecture
Do not hide behind timid, interchangeable sans-serifs. Exceptional design uses typography with physical weight:
- Pair an uncompromising display face (**Dela Gothic One**, **Syne 800**, **Fraunces 900**, **Bricolage Grotesque**) at monumental scale (`clamp(3.5rem, 13vw, 14rem)`) with a pristine, humanist body face (**Epilogue**, **Mona Sans**, **IBM Plex Sans**). Use tight tracking (about `-0.02em` to `-0.045em`) and tight leading (`0.92` to `1.05`), and rotate pairings between projects.
- Treat headlines as sculptural anchors that establish scale, depth, and shadow.

### 3. Sensory Immersion: Shaders and Sound (when the subject earns them)
Interfaces that impress can engage several sensory channels, but a sensory layer must be earned by the subject: immersive experiences, creative studios, entertainment, hospitality, editorial showpieces. Use at most one layer on a typical marketing page, and never on dashboards, forms, docs, or checkout. Budgets, fallbacks, and working code are in [motion.md](motion.md).
- **Procedural Canvas:** Custom WebGL fragment shaders for living surfaces (wave dynamics, atmospheric clouds, raymarched light) rather than video loops, always with a complete CSS fallback and a still frame for reduced motion.
- **Synthesized Audio:** The Web Audio API can generate low-overhead ambient drones, water soundscapes, or tactile click feedback. Mute by default, create the audio context only after a user gesture, and provide an unmistakable toggle.
- **Living Lighting Models:** Support dynamic state transformations, such as a Day/Night toggle that updates GLSL shader uniforms, sun vectors, and text hues across the entire experience.

### 4. Layout Choreography: Rejecting the Card Kit
- Use full-height (`100svh`) section stages that reward exploration.
- Replace card grids with kinetic editorial index rows that slide laterally on hover with custom cubic-bezier curves, and give them tap and keyboard-focus equivalents.
- Use sticky sidebar anchors to hold high-level context while detailed content streams past.

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

Avoid generic goals such as “premium,” “modern,” or “beautiful” unless you translate them into concrete choices (a typeface, a color collision, a layout move, a motion) and explain why they fit this product. Distinctiveness can come from real content, information density, composition, materials, voice, or boldness. Every bold move needs a reason you can say in one sentence.

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
- The world (six nouns), the chosen direction, and the signature moment
- Information order and chosen composition
- Type roles and semantic color roles
- Spacing, sizing, surface, and component conventions
- Asset/icon direction and what each prominent visual element communicates
- Motion plan: one load sequence, a few named interactions, and any sensory layer with its fallback
- Responsive and interaction behavior
- Assumptions that could change the result

The contract should be small enough to check against while implementing. Use semantic tokens when creating or changing a design system, but do not force identical values across roles that need distinct hierarchy.

## Uniqueness check

Before implementation, run the **transplant test**: replace the product name with an unrelated one (a dentist, a crypto exchange, a children's museum). If the palette, type, layout, signature, and motion would still work unchanged, you have made a template. Change at least two of them so they come from this product's world, tied to its actual content, brand, or task.

Do not respond by adding random asymmetry or novelty for its own sake. Boldness belongs in one place and the rest of the page stays calm enough to let it land. Familiar patterns remain right where people must recognize something quickly, such as navigation, forms, and checkout.
