# Color

Color is a decision about what matters. A palette is not a set of pretty swatches; it is a budget that says where attention goes. Open this at step 3.

## Contents

- [The structure](#the-structure)
- [Rules](#rules)
- [Authored palettes](#authored-palettes)
- [Adapting a palette](#adapting-a-palette)
- [Choosing fast](#choosing-fast)

## The structure

Every palette in this skill has six roles. Keep the roles even when you change every hue:

| Role | Job |
|---|---|
| Background | The page. Usually the largest area by far. |
| Surface | Cards, panels, raised blocks. A step above the background. |
| Ink | Body text and headings. Near-black, tinted, never pure `#000`. |
| Muted ink | Captions, secondary text. Must still pass 4.5:1. |
| Accent | The primary action and key emphasis. Gets one job. |
| Accent ink | The text color that sits on the accent. |

Budget roughly: 60 percent background, 30 percent ink and surface, 10 percent accent or less. An accent that appears everywhere stops being an accent.

## Rules

1. **Tint the neutrals.** Pure gray is a default. Warm neutrals (a touch of yellow or red) feel like paper and wood; cool neutrals (a touch of blue or green) feel like glass and steel. Choose on purpose and never mix warm and cool grays in one palette.
2. **Anchor the palette in a material.** Paper, clay, slate, moss, brass, sea foam. Material names keep hues honest; "vibrant" does not. This is also how you surprise: a harbor buoy orange, a bottle of oxblood ink, a patina green.
3. **One accent, one job.** Primary action, active state, the one number that matters. If a fourth element needs emphasis, the hierarchy is wrong, not the accent count.
4. **Contrast is not optional.** Body text at least 4.5:1 against its background, large text (24px or 19px bold and up) and UI boundaries at least 3:1. Gray text on colored panels almost always fails. Measure with `python3 scripts/contrast.py "<fg>" "<bg>"` instead of guessing.
5. **State colors are semantic and calm.** Success, warning, and danger appear only for meaning, always paired with text or an icon, never as the only signal. They do not glow.
6. **Dark mode is a translation, not an inversion.** Tinted dark neutrals (never pure black), surfaces rise by lightness, the accent keeps its hue but often loses saturation, and text is warm white rather than white. Re-check every pair.
7. **Gradients imitate material or they do not ship.** A barely visible light-on-paper shift can pass. A hue-to-hue banner, gradient text, and blurred color orbs cannot. If you cannot name the material the gradient imitates, delete it.
8. **The accent must survive its job.** Test the accent as button fill (accent ink on accent) and as text (accent on background). If either fails, adjust the accent, not the threshold.

## Authored palettes

Twenty starting palettes, none of them a default framework palette, all contrast-checked with the bundled script. Every ink-to-background pair below is 4.5:1 or better; where an accent sits below 4.5:1 against its background, the palette says so and restricts the accent to fills and large display text (3:1 or better, never body copy). The numbers shown are real, and the repository's test suite re-computes them from these tables so they cannot drift. Swap hues freely, keep the ratios.

### 1. Ledger
Warm paper and oxblood ink. Editorial, exact, trustworthy. Modes: Read, Persuade.

| Role | Hex |
|---|---|
| Background | `#F6F1E5` |
| Surface | `#FDFBF4` |
| Ink | `#201B12` |
| Muted ink | `#6D6455` |
| Accent | `#8E3B2F` |
| Accent ink | `#FDFBF4` |

Ink on background: 15.2:1. Muted on background: 5.2:1. Accent on background: 6.6:1. Accent ink on accent: 7.2:1.

### 2. Peat
A warm dark room with brass on the shelf. Dark mode that never touches neon. Mode: Operate.

| Role | Hex |
|---|---|
| Background | `#14110C` |
| Surface | `#1D1912` |
| Ink | `#EAE3D2` |
| Muted ink | `#99917D` |
| Accent | `#D2A24C` |
| Accent ink | `#1F1505` |

Ink on background: 14.7:1. Muted on background: 6.0:1. Accent on background: 8.1:1. Accent ink on accent: 7.7:1.

### 3. Harbor
Sea-foam gray, deep water ink, one buoy-orange signal. Calm competence with a surprise. Modes: Operate, Persuade.

| Role | Hex |
|---|---|
| Background | `#E7ECE9` |
| Surface | `#F7FAF8` |
| Ink | `#122622` |
| Muted ink | `#526864` |
| Accent | `#A8431F` |
| Accent ink | `#FFF6F0` |

Ink on background: 13.3:1. Muted on background: 5.0:1. Accent on background: 5.0:1. Accent ink on accent: 5.7:1.

### 4. Furrow
Flax and olive, a field after rain. Organic and grounded. Modes: Read, Persuade.

| Role | Hex |
|---|---|
| Background | `#F3EBDD` |
| Surface | `#FAF6EC` |
| Ink | `#2A2416` |
| Muted ink | `#6E6650` |
| Accent | `#4F5D26` |
| Accent ink | `#F7F8EE` |

Ink on background: 13.0:1. Muted on background: 4.8:1. Accent on background: 6.1:1. Accent ink on accent: 6.7:1.

### 5. Mulberry
Pale plaster with a deep berry accent. Premium without shouting. Modes: Persuade, Experience.

| Role | Hex |
|---|---|
| Background | `#F8F1F2` |
| Surface | `#FEFAFA` |
| Ink | `#291A20` |
| Muted ink | `#75606A` |
| Accent | `#6E2B4C` |
| Accent ink | `#FBF4F6` |

Ink on background: 14.9:1. Muted on background: 5.2:1. Accent on background: 8.9:1. Accent ink on accent: 9.2:1.

### 6. Verdigris
Gallery neutral with a patina-green accent. Lets content carry the color. Modes: Read, Experience.

| Role | Hex |
|---|---|
| Background | `#F0F0EA` |
| Surface | `#FAFAF5` |
| Ink | `#17251F` |
| Muted ink | `#586B61` |
| Accent | `#1F5C4D` |
| Accent ink | `#F2F7F4` |

Ink on background: 13.9:1. Muted on background: 5.0:1. Accent on background: 6.8:1. Accent ink on accent: 7.2:1.

### 7. Slate
Near-monochrome graphite with one seal-red signal. Stark, editorial, fast. Mode: Read.

| Role | Hex |
|---|---|
| Background | `#F2F2F0` |
| Surface | `#FBFBFA` |
| Ink | `#16181A` |
| Muted ink | `#5F6468` |
| Accent | `#C7361F` |
| Accent ink | `#FFF5F2` |

Ink on background: 15.9:1. Muted on background: 5.3:1. Accent on background: 4.7:1. Accent ink on accent: 4.9:1.

### 8. Reef
Deep water dark with coral on the rock. A second dark option, cool where Peat is warm. Mode: Operate.

| Role | Hex |
|---|---|
| Background | `#0F1517` |
| Surface | `#17211F` |
| Ink | `#E3EBE7` |
| Muted ink | `#8FA29B` |
| Accent | `#E8756A` |
| Accent ink | `#2A0F0C` |

Ink on background: 15.2:1. Muted on background: 6.9:1. Accent on background: 6.3:1. Accent ink on accent: 6.1:1.

### 9. Blueprint
Drafting paper with drafting-blue lines. Exact, technical, quiet. For architecture, real estate, engineering. Modes: Persuade, Experience.

| Role | Hex |
|---|---|
| Background | `#E9EEF2` |
| Surface | `#F7F9FA` |
| Ink | `#0F2029` |
| Muted ink | `#4E6470` |
| Accent | `#1D5C8F` |
| Accent ink | `#F2F7FA` |

Ink on background: 14.3:1. Muted on background: 5.3:1. Accent on background: 6.0:1. Accent ink on accent: 6.5:1.

### 10. Marquee
A dark theater, cream titles, brass footlights. For music, film, events, ticketing. Mode: Persuade.

| Role | Hex |
|---|---|
| Background | `#191410` |
| Surface | `#241D16` |
| Ink | `#F3EAD8` |
| Muted ink | `#A99C86` |
| Accent | `#E3A93C` |
| Accent ink | `#241500` |

Ink on background: 15.3:1. Muted on background: 6.8:1. Accent on background: 8.7:1. Accent ink on accent: 8.5:1.

### 11. Teller
Banknote paper and engraved green. Money that does not shout. For fintech, banking, insurance. Modes: Operate, Persuade.

| Role | Hex |
|---|---|
| Background | `#F4F2EA` |
| Surface | `#FBFAF3` |
| Ink | `#17251C` |
| Muted ink | `#5D6E60` |
| Accent | `#175A40` |
| Accent ink | `#F1F7F1` |

Ink on background: 14.2:1. Muted on background: 4.9:1. Accent on background: 7.3:1. Accent ink on accent: 7.5:1.

### 12. Darkroom
A warm dark room lit by one safelight. For photography, film, visual portfolios. Modes: Experience, Operate.

| Role | Hex |
|---|---|
| Background | `#141210` |
| Surface | `#1E1A17` |
| Ink | `#EDE6D9` |
| Muted ink | `#A2988A` |
| Accent | `#E08D3C` |
| Accent ink | `#261201` |

Ink on background: 15.1:1. Muted on background: 6.6:1. Accent on background: 7.2:1. Accent ink on accent: 6.9:1.

### 13. Scoreboard
Varsity cream, navy ink, one field-red signal. For sports, fitness, competition. Modes: Operate, Persuade.

| Role | Hex |
|---|---|
| Background | `#F3F0E7` |
| Surface | `#FBF9F1` |
| Ink | `#14203A` |
| Muted ink | `#5A6478` |
| Accent | `#B3271E` |
| Accent ink | `#FFF6F0` |

Ink on background: 14.2:1. Muted on background: 5.2:1. Accent on background: 5.7:1. Accent ink on accent: 6.1:1.

### 14. Apothecary
Plaster walls, dark moss ink, one amber tincture. For wellness, skincare, health products. Modes: Persuade, Experience.

| Role | Hex |
|---|---|
| Background | `#F5F2EA` |
| Surface | `#FCFAF3` |
| Ink | `#262B20` |
| Muted ink | `#666A58` |
| Accent | `#7A5A18` |
| Accent ink | `#FBF6EA` |

Ink on background: 13.0:1. Muted on background: 5.0:1. Accent on background: 5.7:1. Accent ink on accent: 5.9:1.

### 15. Atlas
Map paper, sepia ink, passport-stamp blue. For travel, tours, hospitality. Modes: Persuade, Operate.

| Role | Hex |
|---|---|
| Background | `#F1EDE1` |
| Surface | `#FAF7EC` |
| Ink | `#26241C` |
| Muted ink | `#6C6753` |
| Accent | `#2C5A7A` |
| Accent ink | `#F4F8FA` |

Ink on background: 13.3:1. Muted on background: 4.9:1. Accent on background: 6.3:1. Accent ink on accent: 6.9:1.

### 16. Zine
Photocopier white, near-black ink, one riso red. Loud voice, cheap materials, honest construction. For personal sites, newsletters, indie products. Modes: Read, Persuade.

| Role | Hex |
|---|---|
| Background | `#F4F3EF` |
| Surface | `#FBFAF7` |
| Ink | `#121212` |
| Muted ink | `#5E5C56` |
| Accent | `#C41F17` |
| Accent ink | `#FFF4EE` |

Ink on background: 16.9:1. Muted on background: 6.0:1. Accent on background: 5.3:1. Accent ink on accent: 5.5:1.

### 17. Crayon
Warm white paper, chocolate ink, one apple red. Playful without becoming a rainbow. For kids, family, toys, friendly consumer products. Modes: Persuade, Experience.

| Role | Hex |
|---|---|
| Background | `#FFF6E9` |
| Surface | `#FFFDF6` |
| Ink | `#33261B` |
| Muted ink | `#6E5F4E` |
| Accent | `#B3301C` |
| Accent ink | `#FFF3EC` |

Ink on background: 13.7:1. Muted on background: 5.8:1. Accent on background: 5.8:1. Accent ink on accent: 5.8:1.

### 18. Volt
Graphite with a green cast, warm off-white ink, one electric lime. Instrument-panel dark mode with a signal color. For developer products, APIs, audio and realtime tools. Modes: Persuade, Operate.

| Role | Hex |
|---|---|
| Background | `#0B0D0A` |
| Surface | `#13160F` |
| Ink | `#EEF3E3` |
| Muted ink | `#9AA78C` |
| Accent | `#C6F24E` |
| Accent ink | `#131A02` |

Ink on background: 17.3:1. Muted on background: 7.7:1. Accent on background: 15.1:1. Accent ink on accent: 13.8:1.

### 19. Signal
Cool paper white, dense ink, one safety orange. A workshop wall, not a coffee table. For studios, agencies, campaigns, anywhere confidence is the product. Modes: Experience, Persuade. The accent measures 3.1:1 on the background, so it works on fills, borders, and display text at 24px or larger, never on body copy; the accent ink passes on the fill at 5.5:1.

| Role | Hex |
|---|---|
| Background | `#F6F6F4` |
| Surface | `#FFFFFF` |
| Ink | `#16150F` |
| Muted ink | `#6F6E66` |
| Accent | `#FF4D00` |
| Accent ink | `#16150F` |

Ink on background: 16.9:1. Muted on background: 4.7:1. Accent on background: 3.1:1. Accent ink on accent: 5.5:1.

### 20. Nightbus
Blue-black, cool white ink, one mint-teal signal. Night transport and festival light on wet asphalt. For events, nightlife, music, streaming. Modes: Persuade, Experience.

| Role | Hex |
|---|---|
| Background | `#0A0D12` |
| Surface | `#10151C` |
| Ink | `#EAF1F4` |
| Muted ink | `#8E9DA9` |
| Accent | `#4FE3C1` |
| Accent ink | `#04211A` |

Ink on background: 17.0:1. Muted on background: 7.0:1. Accent on background: 12.1:1. Accent ink on accent: 10.6:1.

## Adapting a palette

1. Keep the six roles. If you need status colors, add them in the accent's saturation family and check them against the background too.
2. Swap the hue, keep the ratios. Any hue works if the numbers hold.
3. Pull from physical sources: packaging, transit signage, book covers, banknotes, tools. Not from other websites' heroes.
4. Dark variants: keep the accent hue, drop saturation 10 to 20 percent, darken the background, and re-run every pair through the contrast script.

## Choosing fast

- Reading-heavy product: Ledger, Slate, or Verdigris.
- Dashboard or tool (light): Harbor. Dark: Peat, Reef, or Darkroom.
- Developer product, API, technical marketing: Volt.
- Studio, agency, portfolio with personality: Signal.
- Events, nightlife, performance, streaming: Nightbus or Marquee.
- Marketing that must feel premium: Mulberry or Verdigris.
- Warm physical product or studio: Furrow, Ledger, or Apothecary.
- Money, legal, institutional trust: Teller, Ledger, or Notary formality (Slate).
- Architecture, engineering, technical services: Blueprint.
- Sports and competition: Scoreboard.
- Travel and maps: Atlas.
- Editorial with attitude: Zine.
- Kids and family: Crayon, held to one accent.
- If the brand already has colors, use them and enforce the structure and the contrast floor.
