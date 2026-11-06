---
name: slopless-ui
description: Professional UI design, implementation, and review system. Eliminates generic AI aesthetics, interchangeable templates, and boilerplate styling by enforcing distinctive visual identities, bespoke typography, unexpected premium color palettes, product-specific information architecture, and automated verification. Includes the /slopless-create scratch workflow with a zero-annoyance context check and permission gate. Use whenever creating new UI, components, landing pages, portfolios, or fixing generic/AI-generated interface designs.
license: MIT
---

# Slopless UI

Eliminate generic "AI slop" and interchangeable boilerplate interfaces. Every user interface must possess a distinctive visual identity, an intentional type and color hierarchy, and an information architecture rooted strictly in the product's domain and user tasks—never defaulting to generic templates, synthetic device mockups, or unexamined trends.

---

## 1. Reject the Default AI Slop Trait Patterns

Modern language models have strong pre-trained biases toward producing generic, cookie-cutter UI. You must consciously reject these default traits unless the user's brief explicitly demands them:

1. **The SaaS Card-Kit Default:** Do not chop all content into identical 3-column rounded cards (`grid-cols-3` + `rounded-2xl` + soft drop shadow) where every card shares the identical badge, padding, and bottom links. Use diverse, content-driven structures: full-width kinetic editorial lists, tables for comparisons, timelines for sequences, split viewports, queues, or asymmetric layouts. See [references/foundations.md](references/foundations.md).
2. **The Floating Gradient & Glow Crutch:** Do not use decorative purple/violet/pink radial background blobs, `bg-clip-text text-transparent bg-gradient-to-r`, or glowing neon box shadows. Use purposeful, solid surface values and semantic borders.
3. **Template Chrome & Eyebrow Badges:** Do not prefix every heading with an all-caps, tracked-out eyebrow tag (e.g., `✦ FEATURES ✦` or `01 / OVERVIEW`). Do not center every single headline and paragraph by default.
4. **Icon Spam:** Do not attach a Lucide or Heroicon symbol inside a colored rounded square to every feature, metric, or list item. Use icons only when they communicate a specific action or unmistakable navigation category. See [references/icons-and-buttons.md](references/icons-and-buttons.md).
5. **Fabricated Proof & AI Jargon:** Never invent metrics (`99.9% uptime`, `10x faster`, `50k+ active developers`), fake customer testimonials, or synthetic logo walls. Never use buzzwords like *unleash*, *supercharge*, *seamless*, *delve*, or *next-gen*. See [references/copy.md](references/copy.md).
6. **Arbitrary Heading Decoration:** Do not accent a single random word in a headline with italics, underline, or a gradient color. Keep headlines cohesive.
7. **Decorative Infinite Loops:** Do not add `@keyframes` for floating, pulsing, glowing, or bobbing without a functional user-state reason. See [references/motion.md](references/motion.md).
8. **The Fake Terminal & Sci-Fi/HUD Trope (STRICTLY BANNED):** Do NOT produce futuristic, sci-fi, cyberpunk, or neon "HUD" interfaces with pitch-black obsidian backgrounds, glowing electric cyan/lime card borders, particle spiderwebs, or synthetic monospace chrome. Specifically forbid:
   - Monospace numbered section headings (e.g. `01 // OVERVIEW`, `02 // ARCHITECTURE`, `// 01`).
   - Fake terminal syntax, bracket tags, and status pills (e.g. `CORE_ENGINE // OS • SYNCED`, `SYS SPEC INDEX [64]`, `[RUNTIME_ENV]`, or `• SYSTEM OPERATIONAL...`).
   - Robotic developer jargon: `RUNTIME MATRIX`, `TAXONOMY BLUEPRINT`, `SENSOR TELEMETRY`, `PERSISTENCE ARCHITECTURE`.
   Unless building an actual command-line terminal emulator or shell tool, interfaces must use natural semantic typography, human labels, and genuine headings.
9. **Synthetic AI Illustrations & Fake Device Mockups (STRICTLY BANNED):** Never generate fake SVG/CSS tablet or phone frames filled with artificial telemetry dials, fabricated progress bars (e.g. `99.9% OPTIMIZED`, `100% SECURE`, simulated battery meters, synthetic sensor rings, or fake device telemetry gauges). Do not produce cartoonish geometric "mockups" to simulate product screens. Present real artifacts: authentic screenshots, interactive working components, verified architecture diagrams, clean code samples, or high-craft editorial summaries.
10. **Predictable AI Palettes vs. Unexpected Premium Color Systems:** Strictly avoid the generic AI palette: pitch-black obsidian (`#050505`) + neon cyan (`#00f0ff`) + electric mint or purple neon. Instead, use unexpected, high-taste color systems that catch people off guard with their warmth, depth, and tactile luxury: roasted espresso with champagne gold, midnight lapis with crisp ivory, fired terracotta with bone and charcoal, deep forest moss with warm chalk, or abyssal ocean indigo with coral flare.
11. **Responsive Navigation & Layout Rigor:** Navigation bars and header elements MUST NEVER overlap or wrap awkwardly on mobile viewports (320px–390px). Mobile layouts must be designed with intrinsic flexibility—stacking navigation, using fluid typography clamps, and testing that no elements collide or create accidental horizontal scrollbars. See [references/responsive-design.md](references/responsive-design.md).

For an exhaustive audit of recurring cues and how to replace them, consult [references/anti-slop.md](references/anti-slop.md).

---

## 2. The Creative Art Direction & Worldbuilding Standard

Eliminating bad habits (anti-slop) is only the baseline floor—it prevents embarrassment, but does not achieve greatness. Avoiding bad things without an artistic vision simply yields bland, timid, corporate boilerplate. True human craft demands **audacity, intentionality, and a unifying conceptual world**.

When designing any website, digital product, or application—whether a SaaS platform, developer tool, e-commerce storefront, creative studio, media publication, or high-concept experience—apply the Creative Worldbuilding standard:

### 1. Unifying Conceptual Metaphor (The World)
Anchor the visual and interactive architecture in a singular creative metaphor rooted in the product's authentic domain, rather than reaching for generic web components:
- **Developer Tools & Infrastructure Platforms:** High-trust engineering clarity, authentic interactive playgrounds, real topology diagrams, live API response explorers, and zero performative terminal fluff.
- **SaaS & Enterprise B2B:** Task-first operational clarity, dense data tables, transparent feature matrices, real workflow timelines, and clear role-based hierarchy.
- **E-Commerce & DTC Flagships:** Physical craftsmanship, tactile editorial lookbooks, warm artisanal paper tones, authentic material textures, and friction-free purchase flows.
- **FinTech, Banking & Legal:** Authoritative typographic weight, sober precision palettes, audited calculation previews, and clear institutional credibility.
- **Creative Studios & Agencies:** Architectural structural planes, monumental display typography, bespoke kinetic cadence, and asymmetric editorial showcases.
- **Editorial, Media & Publications:** High-contrast serif headlines, disciplined column rhythm, pull-quotes, and rich tactile paper tones.
- **High-Concept Interactive Experiences:** Living sensory canvases, dynamic environmental state shifts (e.g. Day/Night transitions), and procedural background depth.

See [references/direction.md](references/direction.md) for full worldbuilding frameworks.

### 2. Monumental Sculptural Typography
Display type is structural architecture. It commands the space and sets the emotional tone:
- Scale primary headlines with fluid, responsive typography: `clamp(3.5rem, 12vw, 14rem)`.
- Use heavy, unapologetic grotesque poster weights (**Dela Gothic One**, **Syne 800**, **Fraunces 900**, or **Mona Sans 800**) that catch people off guard with their audacity.
- Anchor display faces with disciplined, highly legible humanist body typography (**Epilogue**, **Mona Sans**, or **Inter**). See [references/typography.md](references/typography.md).

### 3. Sensory & Living Canvases
Static CSS cards feel lifeless. High-craft digital products breathe:
- **Procedural WebGL Shaders:** Fluid caustics, volumetric lighting, atmospheric particle fields, or mathematical noise fields (`fBm`) rendered on background canvas with zero main-thread lag.
- **Web Audio Ambient Synthesis:** Minimalist, generative ambient audio or subtle tactile click feedback via Web Audio API oscillators, with user-controlled mute/unmute toggles.
- **Living Environment Transitions:** Coordinated lighting shifts (e.g., Day to Night) recalculating shader uniforms, lighting vectors, and text hues in real time.
- **Continuous Immersion Tracking:** Dynamic depth or progress meters (e.g. contextual scroll meters or status indicators).

### 4. Kinetic Editorial Layouts
Break free of uniform card boxes:
- **Kinetic Editorial Lists:** Full-width index rows (`.pj a:hover`) that slide laterally with custom cubic-bezier curves (`cubic-bezier(0.16, 1, 0.3, 1)`).
- **Sticky-Split Viewports:** Sticky anchors (`.sp2` with `.stk`) pairing persistent category headers with scrolling narrative content.
- **Atmospheric Micro-Interactions:** Difference-blended magnetic cursors (`#cu` with `mix-blend-mode: difference`) and Houdini `@property --a` rotating conic gradients for active borders. See [references/motion.md](references/motion.md) and [references/foundations.md](references/foundations.md).

---

## 3. The `/slopless-create` Scratch Creation Protocol

When asked to design a new website, landing page, web application, or interface from scratch—or when the user invokes `/slopless-create` (or `/slopless-ui create`)—you must follow this three-step protocol designed to maximize craft while never annoying the user:

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
Before asking ANY questions, inspect the user's prompt, uploaded files (e.g., project folders, PRDs, specs), and prior context:
- Does the prompt include project goals, target audience, desired tone, or aesthetic references?
- **If YES:** **DO NOT ASK QUESTIONS.** Asking questions when information was already provided is an immediate failure and frustrates the user. Extract the details silently and move directly to the Design Contract.

### Rule 2: Permission Gate (Never Ambush the User)
If the user's request is completely blank (e.g., just "build a web app" or "make a landing page" without details):
- **Never barrage the user with an unsolicited interrogation.**
- Ask permission first:
  > *"I have a strong baseline in mind, but to ensure this feels exactly right for your product, would you like me to ask 2–3 quick questions to customize the mood and color palette, or should I propose a bespoke design contract right away?"*

### Rule 3: Restrained, Tailored Customization (Max 2–3 High-Impact Choices)
If the user explicitly asks for customization or grants permission, ask at most 2–3 concise, high-value questions (using `ask_question` tool if available, or clean multiple-choice format):
1. **Atmosphere & Visual Personality:**
   - (A) *High-Trust Engineering & Dev Tools* — Clean typographic hierarchy (Mona Sans), crisp slate/blueprint tones, authentic architecture diagrams.
   - (B) *Warm Editorial Luxury & DTC* — Newsreader + Mona Sans, rich espresso/champagne gold, tactile paper, quiet prestige.
   - (C) *Architectural Brutalism & Creative Studio* — Bold geometric display (Syne), deep tactile contrast, sculptural layout.
   - (D) *Monumental High-Concept Living Canvas* — Dela Gothic One + Epilogue, procedural WebGL shader backdrop, living environmental shifts.
   - (E) *Authoritative FinTech & Institutional* — Libre Caslon Text + Figtree, sober precision tones, dense data tables.
   - (F) *Tactile Artisanal & Consumer* — Warm bone/terracotta tones, humanist serifs, physical product credibility.
2. **Color Universe (Unexpected & Premium):**
   - (A) *Roasted Espresso & Champagne Gold* (`#120F0D` / `#F7F4EE` / `#D4AF37`) — Deep organic warmth, luminous gold.
   - (B) *Midnight Lapis & Pearl Ivory* (`#0A1128` / `#FCFCFA` / `#E6A15C`) — Deep oceanic navy, warm amber.
   - (C) *Fired Terracotta & Warm Bone* (`#FBF9F5` / `#1E2224` / `#A84B2C`) — Earthy Mediterranean clay, charcoal slate.
   - (D) *Deep Forest Moss & Chalk* (`#131A14` / `#F4F6F0` / `#7E9F6E`) — Atmospheric dense pine, muted olive.
   - (E) *Twilight Sea & Coral Flare* (`#2A0E6E` / `#38168C` / `#F6F0E4` / `#E8826A`) — Deep twilight ocean, warm sand ink, coral accent.
   - (F) *Night Sea & Bioluminescent Cyan* (`#070B2A` / `#0E1442` / `#E9EFFF` / `#6FE8FF`) — Abyssal midnight ocean, icy white ink, cyan accent.
   - (G) *Primer High-Trust White & Emerald* (`#FFFFFF` / `#F6F8FA` / `#1F2328` / `#1F883D`) — High-trust SaaS, dev tools, clean product.
3. **Primary Focal Point & Information Architecture:**
   - (A) *Direct Artifact & Product Showcase* — Lead with working interactive components, verified architecture diagrams, and real feature demos.
   - (B) *Operational Dashboard & Data View* — Lead with dense data tables, live workflow queues, and contextual metric comparisons.
   - (C) *Editorial Lookbook & Story Narrative* — Lead with narrative photography, pull-quotes, and asymmetric magazine-style layouts.
   - (D) *Kinetic Editorial Showcase* — Lead with kinetic project rows (`.pj`), category index splits, and live links.

Once the user answers (or immediately if context was already present), synthesize the choices into the **Design Contract** and start building.

---

## 4. Core Token Systems (Ready to Use)

Do not invent arbitrary grey-and-indigo colors or default to system sans. Use these curated, contrast-verified presets or derive bespoke tokens following their structure.

### Curated Color Palettes (Tested for WCAG AA & AAA)

| Preset | Voice / Mode | `--bg` | `--surface` | `--ink` | `--muted` | `--accent` | `--accent-ink` |
|---|---|---|---|---|---|---|---|
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

*(For 14 additional tested palettes including Ledger, Peat, Harbor, Furrow, and Mulberry, consult [references/color.md](references/color.md) — 26 total palettes tested for WCAG AA & AAA).*

### Distinctive Typography Pairings

| Style | Display Face | Body Face | Best For | Google Fonts Import Format |
|---|---|---|---|---|
| **Monumental / Oceanic** | Dela Gothic One | Epilogue | Awwwards portfolios, creative technologist studios | `family=Dela+Gothic+One&family=Epilogue:ital,wght@0,300..900;1,300..900` |
| **High-Trust Developer** | Mona Sans | Mona Sans | Dev tools, SaaS, portfolios | `family=Mona+Sans:wght@400;500;600;700;800` |
| **Editorial Prestige** | Newsreader | Mona Sans / Inter | Luxury editorial, senior portfolios | `family=Newsreader:ital,opsz,wght@0,6..72,500;0,6..72,700;1,6..72,400&family=Mona+Sans:wght@400;500;600` |
| **Architectural Brutalist**| Syne | Mona Sans / Inter | Standout studios, creative tech | `family=Syne:wght@700;800&family=Mona+Sans:wght@400;500` |
| **Technical / Dev** | Space Grotesk | IBM Plex Sans | Dev tools, data tools | `family=Space+Grotesk:wght@500;700&family=IBM+Plex+Sans:wght@400;500` |
| **Modern Product** | Gabarito | Schibsted Grotesk | Consumer apps, modern tools | `family=Gabarito:wght@600;700&family=Schibsted+Grotesk:wght@400;500` |
| **Authoritative Serif** | Libre Caslon Text | Figtree | Finance, legal, institutions | `family=Libre+Caslon+Text:wght@700&family=Figtree:wght@400;500;600` |

*(For 20 additional curated pairings including Fraunces, Outfit, and Gloock, consult [references/typography.md](references/typography.md) — 27 total tested pairings).*

---

## 5. Mandatory 3-Phase Execution Protocol

You must work in three structured phases. Do not jump straight to generating code without completing Phase 1.

### Phase 1: The Design Contract (Define Before Coding)

Before authoring or modifying code, output a concise **Design Contract** in your response detailing:
- **Product Identity & Thesis:** 1–2 sentences defining what the product does, who uses it, and the specific emotional/visual direction (e.g. warm editorial luxury, high-trust engineering, artisanal tactile). See [references/direction.md](references/direction.md).
- **Color Palette (5–6 Tokens):** Explicitly name the hex codes for `--bg`, `--surface`, `--ink`, `--muted`, `--accent`, and `--accent-ink`. Select from the presets above, choose from [references/color.md](references/color.md), or define bespoke tokens with verified contrast.
- **Typography Stack:** Choose display and body families matching the product voice from the table above or [references/typography.md](references/typography.md).
- **Information Architecture:** The primary layout pattern chosen for the content (e.g., comparison table, asymmetric split view, interactive queue) instead of a generic card grid. See [references/foundations.md](references/foundations.md).
- **AI Defaults Avoided:** Name at least two generic patterns deliberately excluded for this brief (e.g., "no fake terminal section numbering `01 //`, no synthetic battery/step telemetry dials, no purple gradient text").

### Phase 2: Intentional Implementation

Implement the agreed Design Contract using clean, accessible, and responsive code:
- **Responsive Layout:** Must support viewports down to 390px mobile. Ensure `<meta name="viewport" content="width=device-width, initial-scale=1.0">` is present. See [references/responsive-design.md](references/responsive-design.md).
- **Accessibility & Contrast:** Text must meet WCAG 2.2 AA (minimum 4.5:1 for body text, 3:1 for large text). Every interactive element must have a visible `:focus-visible` state.
- **Motion Restraint:** All motion must respect `@media (prefers-reduced-motion: reduce)`. Keep animations purposeful and non-looping. See [references/motion.md](references/motion.md).
- **Real States:** Implement realistic empty, loading, error, and interactive states rather than static mockups.
- **Icon & Button Semantics:** Use links for navigation, buttons for actions. Do not put buttons on every link. See [references/icons-and-buttons.md](references/icons-and-buttons.md).

### Phase 3: Automated Verification Gate

Before completing the task, validate your work using the bundled validation scripts:
1. **Static Slop & Bug Scan:** Run [scripts/foldcheck.py](scripts/foldcheck.py) against all modified or created files:
   ```bash
   python "<skill-folder>/scripts/foldcheck.py" <target-file-or-dir>
   ```
   *(On Windows, use `py -3` if `python` is not on PATH).*
   If `foldcheck.py` returns any `[error]` findings (such as `LOREM`, `ALERT-DIALOG`, or `IMG-NO-ALT`) or critical warnings (`OUTLINE-KILL`, `TODO-MARKER`), you **must fix them** before concluding.
2. **Contrast Verification:** Use [scripts/contrast.py](scripts/contrast.py) to calculate exact ratios for newly introduced color pairings:
   ```bash
   python "<skill-folder>/scripts/contrast.py" "#fg" "#bg"
   ```
3. **Browser Diagnostics (Optional):** When Playwright is available in the project, run [scripts/finish.mjs](scripts/finish.mjs) for automated viewport screenshots, overflow checks, and console error detection. See [scripts/README.md](scripts/README.md) and [references/verification.md](references/verification.md).

---

## 6. Reference Library

When working on specialized aspects of the interface, consult the corresponding reference files:
- **Design Direction & Contracts:** [references/direction.md](references/direction.md)
- **Component Foundations & Hierarchy:** [references/foundations.md](references/foundations.md)
- **Color Systems & 26 Tested Palettes:** [references/color.md](references/color.md)
- **Typography Stacks & 27 Font Pairings:** [references/typography.md](references/typography.md)
- **Anti-Slop Pattern Catalog:** [references/anti-slop.md](references/anti-slop.md)
- **Responsive & Accessibility Rules:** [references/responsive-design.md](references/responsive-design.md)
- **Verification & Testing Protocol:** [references/verification.md](references/verification.md)
- **Copywriting & Voice:** [references/copy.md](references/copy.md)
- **Buttons, Links, & Icon Semantics:** [references/icons-and-buttons.md](references/icons-and-buttons.md)
- **Motion & Micro-interactions:** [references/motion.md](references/motion.md)
- **Quality Benchmarking & Evaluation:** [references/evaluation.md](references/evaluation.md)

---

## 7. Delivery & Reporting

Summarize what was designed or altered, detailing:
1. The **Design Contract** decisions (chosen palette, typography, and layout).
2. The anti-patterns rejected to protect the product's identity.
3. Verification results from [scripts/foldcheck.py](scripts/foldcheck.py) and contrast checks.
4. Any unverified boundary conditions or platform dependencies.
