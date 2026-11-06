---
name: slopless-ui
description: Professional UI design, implementation, and review system that makes interfaces look authored by a human designer, not generated. Enforces a unifying creative concept, distinctive typography, surprising color, crafted motion, human-sounding copy, flawless responsive behavior, and a verified in-browser pass before handoff. Includes the /slopless-create scratch workflow with a zero-annoyance context check and permission gate. Use whenever creating, redesigning, restyling, polishing, or reviewing a website, landing page, portfolio, dashboard, app screen, or component, when the user says "make it look better", and whenever an interface looks generic, templated, or AI-made.
license: MIT
---

# Slopless UI

Eliminate generic "AI slop" and interchangeable boilerplate interfaces. Every user interface must have a distinctive visual identity, an intentional type and color hierarchy, and an information architecture rooted in the product's domain and user tasks, never defaulting to generic templates, synthetic device mockups, or unexamined trends.

## The bar

Someone opening the result should not be able to tell a model made it. Three tests decide that, and all three run before handoff:

- **Three-second test.** Something on the first screen is memorable. One thing, not five.
- **Phone test.** Flawless at 390px wide. Nothing overlaps, wraps badly, or scrolls sideways.
- **Squint test.** Blur your eyes or shrink the screenshot. The hierarchy and the focal point still read.

Why slop happens: at every decision (font, palette, radius, layout, headline) a model picks the most probable option, and the sum is the average of the internet. Banning patterns only moves the model to the next most probable default. What works is deciding each thing from this product's own subject, on purpose, early, and then looking at the result. Spend boldness in one place and keep the rest disciplined: a page where everything shouts is as generic as one where nothing does.

---

## 1. Reject the Default AI Slop Trait Patterns

Modern language models have strong pre-trained biases toward generic, cookie-cutter UI. Consciously reject these default traits unless the user's brief explicitly demands them:

1. **The SaaS Card-Kit Default:** Do not chop all content into identical 3-column rounded cards (`grid-cols-3` + `rounded-2xl` + soft drop shadow) where every card shares the same badge, padding, and bottom links. Use content-driven structures: full-width kinetic editorial lists, tables for comparisons, timelines for sequences, split viewports, queues, or asymmetric layouts. See [references/foundations.md](references/foundations.md).
2. **The Floating Gradient & Glow Crutch:** Do not use decorative purple/violet/pink radial background blobs, `bg-clip-text text-transparent bg-gradient-to-r`, or glowing neon box shadows. Use purposeful solid surfaces and semantic borders.
3. **Template Chrome & Eyebrow Badges:** Do not prefix every heading with an all-caps, tracked-out eyebrow tag (e.g., `✦ FEATURES ✦` or `01 / OVERVIEW`). Do not center every headline and paragraph by default.
4. **Icon Spam:** Do not attach a Lucide or Heroicon symbol inside a colored rounded square to every feature, metric, or list item. Use icons only when they communicate a specific action or an unmistakable navigation category. See [references/icons-and-buttons.md](references/icons-and-buttons.md).
5. **Fabricated Proof & AI Jargon:** Never invent metrics (`99.9% uptime`, `10x faster`, `50k+ active developers`), fake testimonials, or synthetic logo walls. Do not use buzzwords like *unleash*, *supercharge*, *seamless*, *delve*, or *next-gen*. Write plain, specific copy a person would say, and do not use em dashes in interface copy unless the brand's own voice does. See [references/copy.md](references/copy.md).
6. **Arbitrary Heading Decoration:** Do not accent a single random word in a headline with italics, underline, or a gradient color. Keep headlines cohesive.
7. **Decorative Infinite Loops:** Do not add `@keyframes` for floating, pulsing, glowing, blinking, or bobbing without a functional user-state reason. A slow marquee of real items is fine. See [references/motion.md](references/motion.md).
8. **The Fake Terminal & Sci-Fi/HUD Trope (STRICTLY BANNED):** Do NOT produce futuristic, sci-fi, cyberpunk, or neon "HUD" interfaces with pitch-black obsidian backgrounds, glowing electric cyan/lime card borders, particle spiderwebs, or synthetic monospace chrome. Specifically forbid:
   - Monospace numbered section headings (e.g. `01 // OVERVIEW`, `02 // ARCHITECTURE`, `// 01`).
   - Fake terminal syntax, bracket tags, and status pills (e.g. `CORE_ENGINE // OS • SYNCED`, `SYS SPEC INDEX [64]`, `[RUNTIME_ENV]`, or `• SYSTEM OPERATIONAL...`).
   - Robotic developer jargon: `RUNTIME MATRIX`, `TAXONOMY BLUEPRINT`, `SENSOR TELEMETRY`, `PERSISTENCE ARCHITECTURE`.
   Unless building an actual command-line terminal emulator or shell tool, interfaces must use natural semantic typography, human labels, and genuine headings.
9. **Synthetic AI Illustrations & Fake Device Mockups (STRICTLY BANNED):** Never generate fake SVG/CSS tablet or phone frames filled with artificial telemetry dials, fabricated progress bars (e.g. `99.9% OPTIMIZED`, `100% SECURE`, simulated battery meters, synthetic sensor rings, or fake device gauges). Do not produce cartoonish geometric "mockups" to simulate product screens. Present real artifacts: authentic screenshots, working interactive components, verified architecture diagrams, clean code samples, or high-craft editorial summaries.
10. **Predictable AI Palettes, Including the "Premium" Ones:** Avoid pitch-black obsidian (`#050505`) + neon cyan or mint or purple as a default. Equally avoid reaching by reflex for the clusters that now read as machine-made: espresso with champagne gold, cream or bone with terracotta, near-black with acid green. The presets in section 4 are tested starting points, not answers. Derive the palette from the subject's world, pick one dominant color plus one **shock accent** (a pairing that feels slightly wrong by convention but resolves through strong value contrast, like tomato on deep teal or lemon on cobalt, used on about 5 percent of the area), and mutate any preset you start from by shifting hues 10 to 30 degrees. Twilight Sea and Night Sea are for oceanic, nocturnal, or aquatic subjects, never a stand-in for sci-fi HUD styling.
11. **Responsive Navigation & Layout Rigor:** Navigation bars and header elements MUST NEVER overlap or wrap awkwardly on mobile viewports (320px to 390px). Design mobile layouts with intrinsic flexibility: stacking navigation, fluid typography clamps, and a check that nothing collides or creates an accidental horizontal scrollbar. See [references/responsive-design.md](references/responsive-design.md).
12. **Preset Convergence:** Do not reuse the same preset, font pairing, or layout across unrelated projects, and do not take the first row of a table. If a choice would survive pasting onto an unrelated product unchanged, it is a default. Change it.

For an exhaustive audit of recurring cues and how to replace them, consult [references/anti-slop.md](references/anti-slop.md).

---

## 2. The Creative Art Direction & Worldbuilding Standard

Eliminating bad habits (anti-slop) is only the baseline floor. It prevents embarrassment but does not achieve greatness. Avoiding bad things without an artistic vision yields bland, timid, corporate boilerplate. True human craft demands **audacity, intentionality, and a unifying conceptual world**.

When designing any website, digital product, or application, apply the Creative Worldbuilding standard:

### 0. Find the world, then commit to one signature
1. Write down what this is, who uses it, and **six concrete nouns from its world** (materials, objects, tools, slang, places, textures). A freight company gives you pallet labels, bills of lading, hazard diamonds, dock numbers.
2. Write **three directions** in one line each, truly different from each other: one loud, one quiet, one strange. Pick one.
3. Name its **signature**: the single memorable thing (a type treatment, an interaction, a layout move, or a color collision). Everything else stays quieter so the signature can carry the page.
4. Run the **transplant test**: could this direction be pasted onto an unrelated product unchanged? If yes, discard it and redo steps 2 and 3.

Type, color, layout, and motion ideas come from the six nouns. A choice that cannot point to one of them, or to a real usability reason, is a default.

### 1. Unifying Conceptual Metaphor (The World)
Anchor the visual and interactive architecture in a singular creative metaphor rooted in the product's authentic domain, rather than generic web components. These are examples; invent a better one when the subject allows:
- **Developer Tools & Infrastructure Platforms:** High-trust engineering clarity, authentic interactive playgrounds, real topology diagrams, live API response explorers, and zero performative terminal fluff.
- **SaaS & Enterprise B2B:** Task-first operational clarity, dense data tables, transparent feature matrices, real workflow timelines, and clear role-based hierarchy.
- **E-Commerce & DTC Flagships:** Physical craftsmanship, tactile editorial lookbooks, authentic material textures, and friction-free purchase flows.
- **FinTech, Banking & Legal:** Authoritative typographic weight, sober precision palettes, audited calculation previews, and clear institutional credibility.
- **Creative Studios & Agencies:** Architectural structural planes, monumental display typography, bespoke kinetic cadence, and asymmetric editorial showcases.
- **Editorial, Media & Publications:** High-contrast serif headlines, disciplined column rhythm, pull-quotes, and rich tactile paper tones.
- **High-Concept Interactive Experiences:** Living sensory canvases, dynamic environmental state shifts (e.g. Day/Night transitions), and procedural background depth.

See [references/direction.md](references/direction.md) for full worldbuilding frameworks.

### 2. Monumental Sculptural Typography
Display type is structural architecture. It commands the space and sets the emotional tone:
- Scale primary headlines fluidly, e.g. `clamp(3.5rem, 12vw, 14rem)` for a poster-style signature, with tight tracking (about `-0.02em` to `-0.045em`), tight leading (`0.92` to `1.05`), and `text-wrap: balance`.
- Use heavy, unapologetic faces (**Dela Gothic One**, **Syne 800**, **Fraunces 900**, **Mona Sans 800**, **Bricolage Grotesque**) that catch people off guard with their audacity.
- Anchor display faces with disciplined, legible body typography (**Epilogue**, **Mona Sans**, **Hanken Grotesk**, or **Inter**). Rotate across projects instead of defaulting to one pairing. See [references/typography.md](references/typography.md).

### 3. Sensory & Living Canvases (use when the subject earns them)
Static CSS cards can feel lifeless, and the most memorable products breathe. But a sensory layer must be earned by the subject (immersive experiences, creative studios, entertainment, hospitality, editorial showpieces). Choose at most one layer for a typical marketing site, and never add shaders or audio to dashboards, forms, docs, or checkout flows.
- **Procedural WebGL Shaders:** Fluid caustics, volumetric lighting, atmospheric particle fields, or mathematical noise (`fBm`) on a background canvas, with bounded cost and a static fallback.
- **Web Audio Ambient Synthesis:** Minimal generative ambient audio or subtle click feedback, created only after a user gesture, muted by default, with an unmistakable mute toggle.
- **Living Environment Transitions:** Coordinated lighting shifts (e.g., Day to Night) that recalculate shader uniforms and text hues.
- **Immersion Tracking:** A depth or progress indicator tied to scroll position.

Rules, budgets, and code are in [references/motion.md](references/motion.md). On touch devices and under reduced motion, serve a simplified or still version that is still a complete design.

### 4. Kinetic Editorial Layouts
Break free of uniform card boxes:
- **Kinetic Editorial Lists:** Full-width index rows that slide laterally on hover with a custom curve (`cubic-bezier(0.16, 1, 0.3, 1)`), with a tap or focus equivalent on touch and keyboard.
- **Sticky-Split Viewports:** A persistent category header pinned beside scrolling narrative content.
- **Atmospheric Micro-Interactions:** Difference-blended magnetic cursors (fine pointers only) and Houdini `@property` rotating conic borders for active focus states. See [references/motion.md](references/motion.md) and [references/foundations.md](references/foundations.md).

---

## 3. The `/slopless-create` Scratch Creation Protocol

When asked to design a new website, landing page, web application, or interface from scratch, or when the user invokes `/slopless-create` (or `/slopless-ui create`), follow this protocol, designed to maximize craft while never annoying the user:

```
┌────────────────────────────────────────────────────────────────────────┐
│                     THE ZERO-ANNOYANCE DISCOVERY GATE                  │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
                                    ▼
       ┌─────────────────────────────────────────────────────────┐
       │ Did the user already provide enough context & details?  │
       │ (e.g. project details, PRD, aesthetic style, or brief)  │
       └────────────────────────────┬────────────────────────────┘
                                    │
                    ┌───────────────┴───────────────┐
                    │                               │
                 [ YES ]                         [ NO ]
                    │                               │
                    ▼                               ▼
       ┌────────────────────────┐      ┌─────────────────────────┐
       │   DO NOT ASK QUESTIONS │      │   PERMISSION GATE FIRST │
       │ Proceed immediately to │      │  Ask permission before  │
       │  Phase 1 Design Contract│     │  asking 2-3 questions   │
       └────────────────────────┘      └────────────┬────────────┘
                                                    │
                                                    ▼
                                       ┌─────────────────────────┐
                                       │ MAX 2-3 FOCUSED CHOICES │
                                       │ Mood, palette & focus   │
                                       └─────────────────────────┘
```

### Rule 1: Context Pre-Check (Zero-Annoyance Guarantee)
Before asking ANY questions, inspect the user's prompt, uploaded files (project folders, PRDs, specs, resumes), and prior context:
- Does the prompt include project goals, target audience, desired tone, or aesthetic references?
- **If YES:** **DO NOT ASK QUESTIONS.** Asking for information that was already provided is an immediate failure and frustrates the user. Extract the details silently and move directly to the Design Contract.

### Rule 2: Permission Gate (Never Ambush the User)
If the request is completely blank (e.g., just "build a web app" or "make a landing page"):
- **Never barrage the user with an unsolicited interrogation.**
- Ask permission first:
  > *"I have a strong baseline in mind, but to ensure this feels exactly right for your product, would you like me to ask 2–3 quick questions to customize the mood and color palette, or should I propose a bespoke design contract right away?"*

### Rule 3: Restrained, Tailored Customization (Max 2–3 High-Impact Choices)
If the user asks for customization or grants permission, ask at most 2–3 concise, high-value questions (using an `ask_question` tool if available, or a clean multiple-choice format). Every option list also accepts "describe your own": the options are starting points, and the chosen option should be mutated toward the product rather than copied.
1. **Atmosphere & Visual Personality:**
   - (A) *High-Trust Engineering & Dev Tools*: Clean typographic hierarchy (Mona Sans), crisp slate/blueprint tones, authentic architecture diagrams.
   - (B) *Warm Editorial Luxury & DTC*: Newsreader + Mona Sans, tactile paper, quiet prestige.
   - (C) *Architectural Brutalism & Creative Studio*: Bold geometric display (Syne), deep tactile contrast, sculptural layout.
   - (D) *Monumental High-Concept Living Canvas*: Dela Gothic One + Epilogue, procedural WebGL shader backdrop, living environmental shifts.
   - (E) *Authoritative FinTech & Institutional*: Libre Caslon Text + Figtree, sober precision tones, dense data tables.
   - (F) *Tactile Artisanal & Consumer*: Warm tones, humanist serifs, physical product credibility.
   - (G) *Loud & Playful Off-Guard*: A shock-color palette (Tomato Lagoon, Cobalt Lemon, Butter Ultramarine), Bricolage Grotesque, one big signature moment.
2. **Color Universe (Unexpected & Premium):**
   - (A) *Roasted Espresso & Champagne Gold* (`#120F0D` / `#F7F4EE` / `#D4AF37`): Deep organic warmth, luminous gold.
   - (B) *Midnight Lapis & Pearl Ivory* (`#0A1128` / `#FCFCFA` / `#E6A15C`): Deep oceanic navy, warm amber.
   - (C) *Fired Terracotta & Warm Bone* (`#FBF9F5` / `#1E2224` / `#A84B2C`): Earthy Mediterranean clay, charcoal slate.
   - (D) *Deep Forest Moss & Chalk* (`#131A14` / `#F4F6F0` / `#7E9F6E`): Atmospheric dense pine, muted olive.
   - (E) *Twilight Sea & Coral Flare* (`#2A0E6E` / `#38168C` / `#F6F0E4` / `#E8826A`): Deep twilight ocean, warm sand ink, coral accent.
   - (F) *Night Sea & Bioluminescent Cyan* (`#070B2A` / `#0E1442` / `#E9EFFF` / `#6FE8FF`): Abyssal midnight ocean, icy white ink, cyan accent. For aquatic or nocturnal subjects only.
   - (G) *Primer High-Trust White & Emerald* (`#FFFFFF` / `#F6F8FA` / `#1F2328` / `#1F883D`): High-trust SaaS, dev tools, clean product.
   - (H) *Tomato Lagoon* (`#0C3B3C` / `#FFF0DC` / `#FF6A45`): Warm and loud on deep teal, the shock-color option.
   - (I) *Cobalt Lemon* (`#1B28F0` / `#F8F6EC` / `#FFE14A`): Full-bleed blue with lemon, rare and memorable.
3. **Primary Focal Point & Information Architecture:**
   - (A) *Direct Artifact & Product Showcase*: Lead with working interactive components, verified architecture diagrams, and real feature demos.
   - (B) *Operational Dashboard & Data View*: Lead with dense data tables, live workflow queues, and contextual metric comparisons.
   - (C) *Editorial Lookbook & Story Narrative*: Lead with narrative photography, pull-quotes, and asymmetric magazine-style layouts.
   - (D) *Kinetic Editorial Showcase*: Lead with kinetic project rows, category index splits, and live links.

### Rule 4: Non-Interactive Hosts
If the host cannot ask questions or the user is not available, skip the gate. State your assumptions in one line, write the Design Contract, and build.

Once the user answers (or immediately if context was already present), synthesize the choices into the **Design Contract** and start building.

---

## 4. Core Token Systems (Ready to Use)

Do not invent arbitrary grey-and-indigo colors or default to a system sans. Use these curated, contrast-checked presets as starting points, or derive bespoke tokens following their structure.

### Starter CSS (quality floor)

```css
:root {
  /* palette tokens from your Design Contract: --bg, --surface, --ink, --muted, --accent, --accent-ink */
  --font-display: "Your Display", Georgia, serif;
  --font-body: "Your Body", system-ui, sans-serif;
  --step-0: clamp(1rem, 0.96rem + 0.2vw, 1.125rem);
  --step-3: clamp(2.1rem, 1.7rem + 2vw, 3.4rem);
  --step-5: clamp(3.4rem, 1.8rem + 8vw, 9rem);
  --ease-out: cubic-bezier(0.22, 1, 0.36, 1);
  --ease-in-out: cubic-bezier(0.65, 0, 0.35, 1);
  --t-fast: 140ms; --t-base: 280ms; --t-slow: 520ms; --t-scene: 900ms;
}
*, *::before, *::after { box-sizing: border-box; }
html { -webkit-text-size-adjust: 100%; }
body { margin: 0; min-height: 100svh; background: var(--bg); color: var(--ink);
  font: var(--step-0)/1.6 var(--font-body); -webkit-font-smoothing: antialiased; }
img, svg, video { display: block; max-width: 100%; height: auto; }
h1, h2, h3 { font-family: var(--font-display); text-wrap: balance; margin: 0; }
p { text-wrap: pretty; max-width: 62ch; }
a { color: inherit; text-underline-offset: 0.2em; }
::selection { background: var(--accent); color: var(--accent-ink); }
:focus-visible { outline: 3px solid var(--ink); outline-offset: 3px; }
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after { animation-duration: 0.01ms !important; animation-iteration-count: 1 !important; transition-duration: 0.01ms !important; }
}
```

The focus ring must contrast with the surface it sits on; switch to `--bg` on dark accent areas. Reuse the easing and duration tokens everywhere, because inconsistent timing is what makes motion feel cheap.

### Curated Color Palettes (contrast-checked; exact ratios in [references/color.md](references/color.md))

| Preset | Voice / Mode | `--bg` | `--surface` | `--ink` | `--muted` | `--accent` | `--accent-ink` |
|---|---|---|---|---|---|---|---|
| **Tomato Lagoon** | Warm & Loud on Deep Teal | `#0C3B3C` | `#134E4F` | `#FFF0DC` | `#9CC7BF` | `#FF6A45` | `#1D0A04` |
| **Butter Ultramarine** | Playful Tools, Hard Blue on Butter | `#FFE27A` | `#FFEFA8` | `#10176B` | `#3E4590` | `#2437FF` | `#FFFFFF` |
| **Cobalt Lemon** | Full-Bleed Cobalt, Big Type | `#1B28F0` | `#2A37FF` | `#F8F6EC` | `#DADDFF` | `#FFE14A` | `#0F1470` |
| **Oxblood Pistachio** | Rich Premium Without Black & Gold | `#3A0B16` | `#4D1424` | `#F6EEE2` | `#CBA5AB` | `#B9E98A` | `#192808` |
| **Twilight Sea** | Deep Twilight Ocean & Coral Flare | `#2A0E6E` | `#38168C` | `#F6F0E4` | `#D4CCE0` | `#E8826A` | `#1A083B` |
| **Night Sea** | Abyssal Midnight & Bioluminescent Cyan | `#070B2A` | `#0E1442` | `#E9EFFF` | `#A3B6E0` | `#6FE8FF` | `#03071E` |
| **Espresso** | Warm Editorial Luxury, Prestige | `#120F0D` | `#1D1916` | `#F7F4EE` | `#A8A096` | `#D4AF37` | `#1A1408` |
| **Lapis** | Deep Regal Navy & Warm Amber | `#0A1128` | `#131B38` | `#FCFCFA` | `#97A3B6` | `#E6A15C` | `#1A1105` |
| **Terracotta** | Earthy Mediterranean Clay, Bone & Charcoal | `#FBF9F5` | `#F3EDE2` | `#1E2224` | `#5A6266` | `#A84B2C` | `#FFF5F0` |
| **Forest** | Atmospheric Moss, Deep Pine & Chalk | `#131A14` | `#1D261F` | `#F4F6F0` | `#95A396` | `#7E9F6E` | `#0E160F` |
| **Primer** | Clean Developer, OSS, High-Trust Product | `#FFFFFF` | `#F6F8FA` | `#1F2328` | `#59636E` | `#1F883D` | `#FFFFFF` |
| **Blueprint** | Technical, Engineering, Dev | `#E9EEF2` | `#F7F9FA` | `#0F2029` | `#4E6470` | `#1D5C8F` | `#F2F7FA` |
| **Teller** | Fintech, Banking, Legal | `#F4F2EA` | `#FBFAF3` | `#17251C` | `#5D6E60` | `#175A40` | `#F1F7F1` |
| **Slate** | Editorial, Clean Modern | `#F2F2F0` | `#FBFBFA` | `#16181A` | `#5F6468` | `#C7361F` | `#FFF5F2` |
| **Apothecary** | Artisanal, Skincare, Warm DTC | `#F5F2EA` | `#FCFAF3` | `#262B20` | `#666A58` | `#7A5A18` | `#FBF6EA` |
| **Marquee** (Dark) | Media, Entertainment, Ticketing | `#191410` | `#241D16` | `#F3EAD8` | `#A99C86` | `#E3A93C` | `#241500` |

*(For 18 additional palettes including Ledger, Peat, Harbor, Furrow, Mulberry, Plum Chartreuse, Pool Cherry, Moss Hot Pink, and Denim Marigold, consult [references/color.md](references/color.md). 34 palettes in total, with every documented ratio recalculated by the test suite.)*

### Distinctive Typography Pairings

| Style | Display Face | Body Face | Best For | Google Fonts Import Format |
|---|---|---|---|---|
| **Monumental / Oceanic** | Dela Gothic One | Epilogue | Awwwards portfolios, creative technologist studios | `family=Dela+Gothic+One&family=Epilogue:ital,wght@0,300..900;1,300..900` |
| **High-Trust Developer** | Mona Sans | Mona Sans | Dev tools, SaaS, portfolios | `family=Mona+Sans:wght@400;500;600;700;800` |
| **Editorial Prestige** | Newsreader | Mona Sans / Inter | Luxury editorial, senior portfolios | `family=Newsreader:ital,opsz,wght@0,6..72,500;0,6..72,700;1,6..72,400&family=Mona+Sans:wght@400;500;600` |
| **Architectural Brutalist** | Syne | Mona Sans / Inter | Standout studios, creative tech | `family=Syne:wght@700;800&family=Mona+Sans:wght@400;500` |
| **Technical / Dev** | Space Grotesk | IBM Plex Sans | Dev tools, data tools | `family=Space+Grotesk:wght@500;700&family=IBM+Plex+Sans:wght@400;500` |
| **Modern Product** | Gabarito | Schibsted Grotesk | Consumer apps, modern tools | `family=Gabarito:wght@600;700&family=Schibsted+Grotesk:wght@400;500` |
| **Authoritative Serif** | Libre Caslon Text | Figtree | Finance, legal, institutions | `family=Libre+Caslon+Text:wght@700&family=Figtree:wght@400;500;600` |

*(For 20 additional curated pairings including Fraunces, Outfit, Gloock, and Bricolage Grotesque, consult [references/typography.md](references/typography.md). 27 tested pairings in total.)* Space Grotesk, Inter, and Syne are the most overused faces in generated pages, so use them only when the brief fits, and rotate pairings between projects.

---

## 5. Mandatory 3-Phase Execution Protocol

Work in three structured phases. Do not jump straight to generating code without completing Phase 1. For a small fix (a bug, a single component), run lightly: match the surrounding design, apply the Phase 2 rules, and verify. When the user says "redesign", "make it look better", "unique", or "crazy", run all three phases in full.

### Phase 1: The Design Contract (Define Before Coding)

Before authoring or modifying code, output a concise **Design Contract** in your response (about 15 lines) detailing:
- **Product Identity & Thesis:** 1 to 2 sentences defining what the product does, who uses it, and the emotional and visual direction. See [references/direction.md](references/direction.md).
- **The World & Signature Moment:** The six nouns, the chosen direction, and the one memorable thing (and how it is built). The transplant test must pass.
- **Color Palette (5 to 6 Tokens + 1 shock):** Name the hex codes for `--bg`, `--surface`, `--ink`, `--muted`, `--accent`, and `--accent-ink`, and where the shock accent appears. Select and mutate a preset above, choose from [references/color.md](references/color.md), or define bespoke tokens with verified contrast.
- **Typography Stack:** Display and body families matching the product voice from the table above or [references/typography.md](references/typography.md), and what makes the display treatment special.
- **Information Architecture:** The primary layout pattern chosen for the content (comparison table, asymmetric split view, interactive queue) instead of a generic card grid, with a rough ASCII wireframe of the first screen. See [references/foundations.md](references/foundations.md).
- **Motion Plan:** The one load sequence plus three or four named interactions, and any sensory layer with its fallback.
- **Voice:** Three adjectives and two lines of real copy.
- **AI Defaults Avoided:** Name at least two generic patterns deliberately excluded for this brief (e.g., "no fake terminal numbering `01 //`, no synthetic battery dials, no purple gradient text, no espresso-and-gold by reflex").

### Phase 2: Intentional Implementation

Implement the Design Contract using clean, accessible, and responsive code. Write real content as you go: no lorem ipsum, no "Feature One", no gray boxes.
- **Responsive Layout:** Support viewports down to 390px, and check 320px for navigation and large type. Ensure `<meta name="viewport" content="width=device-width, initial-scale=1.0">` is present. Use `100svh` instead of `100vh`. See [references/responsive-design.md](references/responsive-design.md).
- **Accessibility & Contrast:** Text must meet WCAG 2.2 AA (minimum 4.5:1 for body text, 3:1 for large text). Every interactive element must have a visible `:focus-visible` state.
- **Crafted Motion:** Motion is part of the design, not a garnish. Use one orchestrated load sequence under about 1.2 seconds with staggered text masks, then let motion answer the person's actions and scroll position. Animate only `transform`, `opacity`, `clip-path`, and `filter`. Give hover, press, focus, open, close, and loading states designed feedback, gated with `@media (hover: hover)` for hover. Content is visible by default and only hidden once motion is known to be allowed. Everything respects `@media (prefers-reduced-motion: reduce)`. Recipes with code are in [references/motion.md](references/motion.md).
- **Human Copy:** Short, specific, plain. Buttons say what happens ("Book a fitting", not "Get started"). See [references/copy.md](references/copy.md).
- **Real States:** Implement realistic empty, loading, error, and interactive states rather than static mockups, plus a favicon, `theme-color`, social meta tags, a real `<title>`, and `::selection`.
- **Icon & Button Semantics:** Use links for navigation, buttons for actions. Do not put buttons on every link. See [references/icons-and-buttons.md](references/icons-and-buttons.md).
- **Images:** Use real project assets, SVG or CSS built for the subject, or a generation tool if the host has one. Never a broken URL, never a gray placeholder.

### Phase 3: Verification Gate

Do not call it done from reading your own code. Before completing the task:
1. **Look at it.** Open the page in a browser (the host's browser tool if it has one) at 390, 768, and 1440 wide. Scroll to the bottom, hover and tab through the controls, trigger the motion, and turn on reduced motion. Do the squint test. Fix what looks off, then look again. If you cannot open a browser, say so and list what stayed unverified. See [references/verification.md](references/verification.md).
2. **Static Slop & Bug Scan:** Run [scripts/foldcheck.py](scripts/foldcheck.py) against all modified or created files:
   ```bash
   python "<skill-folder>/scripts/foldcheck.py" <target-file-or-dir>
   ```
   *(On Windows, use `py -3` if `python` is not on PATH).*
   If `foldcheck.py` returns any `[error]` findings (such as `LOREM`, `ALERT-DIALOG`, or `IMG-NO-ALT`) or critical warnings (`OUTLINE-KILL`, `TODO-MARKER`), you **must fix them** before concluding. Most visual patterns are reported as info so legitimate work is not blocked. Do not let those pass silently: for `EM-DASH`, `TERMINAL-CHROME`, `FAKE-TELEMETRY`, `GRADIENT-HERO`, `JARGON`, `ICON-SPAM`, and `LOOP-INFINITE`, either fix the finding or be able to say in one sentence why it serves this product.
3. **Contrast Verification:** Use [scripts/contrast.py](scripts/contrast.py) to calculate exact ratios for newly introduced or mutated color pairings:
   ```bash
   python "<skill-folder>/scripts/contrast.py" "#fg" "#bg"
   ```
4. **Browser Diagnostics (Optional):** When Playwright is available in the project, run [scripts/finish.mjs](scripts/finish.mjs) for automated viewport screenshots, overflow checks, and console error detection. See [scripts/README.md](scripts/README.md).

---

## 6. Reference Library

When working on specialized aspects of the interface, consult the corresponding reference files:
- **Design Direction & Contracts:** [references/direction.md](references/direction.md)
- **Component Foundations & Hierarchy:** [references/foundations.md](references/foundations.md)
- **Color Systems & 34 Tested Palettes:** [references/color.md](references/color.md)
- **Typography Stacks & 27 Font Pairings:** [references/typography.md](references/typography.md)
- **Anti-Slop Pattern Catalog:** [references/anti-slop.md](references/anti-slop.md)
- **Responsive & Accessibility Rules:** [references/responsive-design.md](references/responsive-design.md)
- **Verification & Testing Protocol:** [references/verification.md](references/verification.md)
- **Copywriting & Voice:** [references/copy.md](references/copy.md)
- **Buttons, Links, & Icon Semantics:** [references/icons-and-buttons.md](references/icons-and-buttons.md)
- **Motion, Shaders & Micro-interactions:** [references/motion.md](references/motion.md)
- **Quality Benchmarking & Evaluation:** [references/evaluation.md](references/evaluation.md)

---

## 7. Delivery & Reporting

Summarize what was designed or altered, detailing:
1. The **Design Contract** decisions (world, signature, palette, typography, layout).
2. The anti-patterns rejected to protect the product's identity.
3. What you checked in the browser and at which widths, plus results from [scripts/foldcheck.py](scripts/foldcheck.py) and the contrast checks.
4. Any unverified boundary conditions or platform dependencies, and which content is invented and needs the user's real version. Never claim a check you did not run.
