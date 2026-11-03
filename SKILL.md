---
name: slopless-ui
description: Design direction, build discipline, and a verified finishing pass for any interface a person will see: pages, landing sites, dashboards, forms, components, app screens, emails, themes. Use it for every build or change that touches what the user sees, including small requests like changing colors, tweaking spacing or fonts, polishing a page, fixing responsiveness, or making it look modern. Use it too when the user says a page looks bad, generic, boring, template-made, or machine-made, or asks for a redesign or a review. A recolor-only change is a failed pass; a restyle means a new brief, a named direction, at least two structural changes, and the full finishing pass. The method: a four-line brief, decisions as tokens, layout and hierarchy laws, then foldcheck, contrast checks, and browser screenshots at desktop and phone widths before anything is presented.
license: MIT
compatibility: Agent Skills standard. Works in any agent that reads SKILL.md folders. Scripts are zero-dependency Python 3.8 or newer; the optional browser pass uses Node 18 or newer with Playwright.
---

# Slopless UI

This skill is a procedure, not an opinion. While it is active you owe five observable artifacts, and presenting work without them is a failed run no matter how good the page looks:

1. **The brief.** Four written lines (audience, feeling, signature, mode) in the chat and as a comment in the delivered file, before any code.
2. **A named direction.** Chosen from references/direction.md and recorded in the brief. "Clean and modern" is not a direction.
3. **The foldcheck output.** For every file you changed, pasted into the chat. A gate that ran silently did not run.
4. **Screenshots.** Desktop (1440) and phone (390) widths, from a real browser: the browser tool your environment provides first, `node scripts/finish.mjs` second. Squint them yourself before anyone else does.
5. **The label.** The report's last line, verbatim, one of:
   `verification: verified visually`
   `verification: verified statically (no browser available)`
   `verification: not verified: <reason>`

If you skip an artifact, name the skip and the reason in the report. Silent skipping is how slop happens.

Slop is the machine-made look: the default gradient hero, an icon on every heading, a button on every action, copy full of em dashes and adjectives. Generated interfaces rarely fail on broken markup anymore. They fail on being interchangeable: competent, polished, impossible to remember. This skill exists so an agent's output is not. It does not add more styling. It adds decisions, a pulse, and discipline, and then it checks the result.

## Which path are you on

Pick one before anything else. It decides how much of the method runs.

- **A new page, screen, or component.** The full method, steps 1 through 5.
- **A restyle.** Anything that asks for the page to look different or better: redesign, modernize, "make it pop", and yes, "just change the colors". The full method still runs: a new brief, a new named direction, at least two structural changes (hierarchy, layout, spacing rhythm, motion, or composition), then the whole finishing pass. Recoloring alone is a failed pass.
- **A small fix inside an existing design.** A bug, a broken state, one cramped section. Keep the existing system, touch only what the fix needs, and still run foldcheck and give the label.
- **A review, nothing to change.** Run foldcheck, look at screenshots if you can, and report findings ranked must, should, nice. Do not rewrite anything unless asked.

## The method

Work in this order. Each step has one job, and each step's details live in one reference file. Read a reference only when you reach the step that needs it.

### 1. Read the room

Before writing a line, find the decisions that already exist: a `DESIGN.md` or tokens file, the project's CSS variables, a `tailwind.config.*` or `@theme` block, the existing components. If the project already has a look, follow it exactly. Your job is consistency first, taste second. Restyle nothing unless the user asked for a restyle.

### 2. Write the brief

Four lines, written down before any code. They are a contract with yourself, and later steps check against them.

1. **Audience**: who uses this, and what are they doing here in ten seconds.
2. **Feeling**: one or two adjectives you could defend in a review (calm, dense, warm, exact).
3. **Signature**: the one thing a stranger will remember. If you cannot name it, the result will be generic. Pick one: an unusual typeface, one bold number, one unexpected color, one strong composition.
4. **Mode**: Persuade (landing, pricing), Operate (dashboard, app), Read (docs, article), or Experience (portfolio, gallery). Mode changes every later decision.

One filled in, so the shape is unambiguous: `Audience: clinic front-desk staff checking today's queue. Feeling: calm, exact. Signature: the wait time as a huge readable number. Mode: Operate.`

Full guidance, the four modes, and a library of twenty-eight starting directions for common website categories: [references/direction.md](references/direction.md).

### 3. Make the decisions as tokens

Turn the brief into real values, not adjectives: two font families with weights and a fallback stack, one accent color with a job, a spacing scale, a radius scale, motion durations and easings. Write them as CSS variables or the framework's token format. "Clean and modern" is not a decision. `--accent: #8E3B2F` is.

Restyling is not recoloring. A requested restyle changes at least two of: type hierarchy, layout or grid, spacing rhythm, motion, or the focal composition. Color alone is a failed pass unless the brief says, in one line, why this page needs color and nothing else.

- Typography: [references/typography.md](references/typography.md)
- Color: [references/color.md](references/color.md)
- Motion: [references/motion.md](references/motion.md)

### 4. Build with the grain

Then apply the discipline rules while building:

- **The laws come first.** One grid, one column, 4 or 8 point spacing, one focal point per view, all eight component states, keyboard and contrast floors. These are not style; they are the physics every design system agrees on: [references/foundations.md](references/foundations.md).
- **Responsive is the build, not the patch.** Phone layout first: a single column with no media query, then `min-width` layers as content needs room, a fluid `clamp()` type scale, 44px touch targets, `min-width: 0` on every grid child. The mechanics and the computed scale: [references/foundations.md](references/foundations.md).
- **One focal point, one primary action per view.** Hierarchy comes from size, weight, and space, not from boxes.
- **Buttons are commitments.** One filled button per view is normal. Secondary actions are links or quiet buttons. If a region shows more than two buttons, redesign it: [references/icons-and-buttons.md](references/icons-and-buttons.md).
- **Icons are furniture.** Words are clearer. When icons earn a place, one set, one weight, consistent size: [references/icons-and-buttons.md](references/icons-and-buttons.md).
- **Copy is design.** Short sentences, concrete nouns, verb-first buttons, no em dashes, no jargon: [references/copy.md](references/copy.md).
- **Every state exists**: empty, loading, error, long content. Five perfect rows and a happy path is not a finished screen.
- **The page has a pulse.** Controls answer on press, transitions run out the way they ran in, one entrance choreographs the first second, and sections reveal once on scroll. At most one signature ambient, named in the brief. The motion budget and every curve it needs: [references/motion.md](references/motion.md).
- **Left-align text blocks.** Center only short, single-line elements.

### 5. Finish before delivery

Never present UI that you have not looked at. The finishing pass, in order:

1. `python3 scripts/foldcheck.py <changed files>`, fix every error, and paste the output into the chat. If you cannot run it, say so; do not pretend it ran.
2. `python3 scripts/contrast.py <foreground> <background>` for every text pair you introduced. Body text needs 4.5:1 or better; large text and boundaries need 3:1.
3. Screenshot at desktop (1440) and phone (390) widths. Use the browser tool your environment provides first; `node scripts/finish.mjs <url-or-file>` is the fallback. Check the phone shot for horizontal overflow. No browser anywhere means the label is "verified statically" at best.
4. Squint the screenshots: blur your eyes or scale them down. The focal point, reading order, and primary action must survive.
5. Fix, re-check the changed views only, and stop after three fix passes.

Copy this checklist into your working notes and tick items as you complete them:

- [ ] foldcheck run on every changed file, output pasted, all errors fixed
- [ ] contrast measured for every text pair I introduced
- [ ] desktop screenshot (1440) taken and actually looked at
- [ ] phone screenshot (390) taken, no horizontal overflow
- [ ] squint test passed: focal point, reading order, and primary action survive
- [ ] report ends with the verification label, verbatim

Full protocol, honesty labels, and reporting format: [references/verification.md](references/verification.md).

## Non-negotiables

These patterns read as machine-made. Treat them as banned by default, even when a tutorial shows them:

- Blinking, pulsing, bouncing, or floating dots and decorations, including "typing" indicators and glowing status dots that nobody asked for.
- Cyberpunk, neon, glitch, synthwave, vaporwave, matrix, and holographic styling. Glow has no source, so it convinces no one.
- Purple-to-blue and indigo-to-fuchsia gradient heroes, gradient text, blurred color orbs behind content.
- Em dashes in any user-facing text. Use a period, a comma, or parentheses. Same for the AI jargon list in [references/copy.md](references/copy.md).
- Emoji used as icons, bullets, or UI chrome.
- An icon on every heading and a button on every action.
- Lorem ipsum, "coming soon", invented testimonials or metrics presented as real.
- Inter, Roboto, Arial, or the system stack as the identity font by default.
- A page that never moves. Static output reads as an assembled template; the motion budget in [references/motion.md](references/motion.md) is part of finishing, not garnish.

The full catalogue with fixes: [references/anti-slop.md](references/anti-slop.md).

## What failure looks like

The common failure is the recolor: layout untouched, palette swapped, "done". That is a failed pass. The artifacts are how you catch it in yourself: if the brief was never written, the direction never named, or foldcheck never pasted, the skill did not run. The same honesty applies to responsiveness: if you never looked at the 390px screenshot, you do not know whether the page works, and the label must say so.

## The squint test

Blur your eyes (or scale a screenshot to thumbnail size) and look again. Three things must survive the blur: the focal point, the reading order, and the primary action. If the page becomes gray soup, the problem is hierarchy, and no amount of polish will fix it. Fix spacing, size, and weight first. This test takes ten seconds and catches more bad design than any checklist.

## If the user asks for a banned pattern

Sometimes a person genuinely wants neon, heavy gradients, or a cyberpunk theme. Do not fight them and do not lecture. Build it well: real contrast, real hierarchy, working states, restrained motion. Say once, in one line, that the skill defaults against it and you went with their preference. The ban list guards unguided output, not expressed preference.

## Reference map

| File | Read when |
|---|---|
| [references/direction.md](references/direction.md) | Step 2, on every new page or restyle |
| [references/typography.md](references/typography.md) | Step 3, when choosing or checking fonts |
| [references/color.md](references/color.md) | Step 3, when choosing or checking color |
| [references/motion.md](references/motion.md) | Step 3 for tokens, Step 4 for the motion pass (budget, entrances, reveals, ambient, reduced motion) |
| [references/foundations.md](references/foundations.md) | Step 4, for layout, spacing, hierarchy, states, and the named laws |
| [references/copy.md](references/copy.md) | Step 4, whenever text is written |
| [references/icons-and-buttons.md](references/icons-and-buttons.md) | Step 4, for actions, controls, and icons |
| [references/anti-slop.md](references/anti-slop.md) | When output feels familiar in a bad way, or in review |
| [references/verification.md](references/verification.md) | Step 5, before saying anything is done |

## Reporting

End UI work with a short report: what was built, the brief's one-line feeling, what the finishing pass actually ran, what was fixed, and anything left undone. The last line is the label, verbatim: `verification: verified visually`, `verification: verified statically (no browser available)`, or `verification: not verified: <reason>`. Never call a result "pixel-perfect" or "fully tested". Say what you did.

## Scripts

Zero-dependency, no network calls, no telemetry. Paths are relative to this file's folder.

```bash
python3 scripts/foldcheck.py src/            # static audit for machine-made patterns
python3 scripts/contrast.py "#201B12" "#F6F1E5"   # WCAG contrast for a pair
node scripts/finish.mjs ./index.html          # browser pass: screenshots, console, overflow (needs Playwright)
```

`foldcheck` and `contrast` always run. `finish` is optional and degrades gracefully when Playwright is missing; use any browser tool your environment offers instead, because the point is looking, not the tool.
