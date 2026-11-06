# Color

Color helps communicate identity, hierarchy, state, and relationships. Use this reference when creating or reviewing a palette; existing brand and product tokens take precedence.

## Contents

- [The structure](#the-structure)
- [Rules](#rules)
- [Authored palettes](#authored-palettes)
- [Adapting a palette](#adapting-a-palette)
- [Choosing fast](#choosing-fast)

## The structure

The palettes below organize a useful set of semantic roles. Use the roles that fit the interface; they are not a required six-color recipe:

| Role | Job |
|---|---|
| Background | The page. Usually the largest area by far. |
| Surface | Cards, panels, raised blocks. A step above the background. |
| Ink | Body text and headings; choose for the brand and applicable contrast. |
| Muted ink | Captions and secondary text; check the applicable contrast criterion. |
| Accent | An emphasis role; it may support several related actions or states. |
| Accent ink | The text color that sits on the accent. |

Treat area proportions as a composition tool, not a fixed ratio. Reserve emphasis color for elements whose role warrants it.

## Rules

1. **Connect color to the product.** Brand, content, setting, user expectations, and state are useful sources. Material metaphors can help, but are optional.
2. **Use semantic roles.** Define foreground, surface, border, emphasis, and state colors as the interface needs. Allow several emphasis colors when hierarchy and meaning call for them.
3. **Check contrast against the applicable standard.** WCAG 2.2 AA requires 4.5:1 for normal text and 3:1 for large text; non-text contrast has its own scope and exceptions. Use `contrast.py` as a calculation aid, not a conformance verdict.
4. **Do not convey state with color alone.** Pair color with text, shape, icon, or another perceivable cue where needed.
5. **Treat gradients, transparency, and dark surfaces as design choices.** Check legibility, context, performance, and product fit in rendered states. None is inherently a defect.
6. **Spend one color on surprise.** Choose a dominant color from the subject, then one shock accent: a pairing that feels slightly wrong by convention but resolves through strong value contrast (tomato on deep teal, lemon on cobalt). Keep it near 5 percent of the area so it lands. A "safe unexpected" palette is not unexpected.
7. **Do not take a palette by reflex.** Some clusters now read as machine-made because models reach for them constantly: espresso with champagne gold, cream or bone with terracotta, near-black with acid green or cyan, and any purple-to-pink gradient. Each is legitimate when the brief or brand asks for it. When the brief leaves color open, derive it from the subject instead, and mutate any preset you start from (shift hues 10 to 30 degrees) so the result is not a copy.

## Authored palettes

The authored palettes below are optional starting points, not a recommendation to avoid framework or brand colors. Palettes 27 to 34 are deliberately bolder; use them when the brief wants a color the visitor will not expect. Their documented pair ratios are recalculated by the repository test suite; test any adapted or newly introduced pair in its real context.

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

### 21. Espresso
Deep roasted organic coffee, warm cashmere alabaster, and champagne gold. Luxury editorial with depth, prestige, and tactile warmth. Modes: Experience, Persuade.

| Role | Hex |
|---|---|
| Background | `#120F0D` |
| Surface | `#1D1916` |
| Ink | `#F7F4EE` |
| Muted ink | `#A8A096` |
| Accent | `#D4AF37` |
| Accent ink | `#1A1408` |

Ink on background: 17.4:1. Muted on background: 7.4:1. Accent on background: 9.1:1. Accent ink on accent: 8.7:1.

### 22. Lapis
Deep oceanic navy, crisp pearl ivory, and radiant warm amber. Authority and quiet confidence that catches people off guard. Modes: Persuade, Operate.

| Role | Hex |
|---|---|
| Background | `#0A1128` |
| Surface | `#131B38` |
| Ink | `#FCFCFA` |
| Muted ink | `#97A3B6` |
| Accent | `#E6A15C` |
| Accent ink | `#1A1105` |

Ink on background: 18.2:1. Muted on background: 7.3:1. Accent on background: 8.6:1. Accent ink on accent: 8.5:1.

### 23. Terracotta
Earthy Mediterranean fired clay, warm bone, and crisp slate. Tactile grounded warmth with architectural balance. Modes: Read, Persuade.

| Role | Hex |
|---|---|
| Background | `#FBF9F5` |
| Surface | `#F3EDE2` |
| Ink | `#1E2224` |
| Muted ink | `#5A6266` |
| Accent | `#A84B2C` |
| Accent ink | `#FFF5F0` |

Ink on background: 15.3:1. Muted on background: 5.9:1. Accent on background: 5.4:1. Accent ink on accent: 5.3:1.

### 24. Forest
Dense atmospheric pine, muted sage, and warm chalk. Deep organic stillness with natural resonance and high taste. Modes: Experience, Operate.

| Role | Hex |
|---|---|
| Background | `#131A14` |
| Surface | `#1D261F` |
| Ink | `#F4F6F0` |
| Muted ink | `#95A396` |
| Accent | `#7E9F6E` |
| Accent ink | `#0E160F` |

Ink on background: 16.3:1. Muted on background: 6.7:1. Accent on background: 6.0:1. Accent ink on accent: 6.2:1.

### 25. Twilight Sea
Deep sunset indigo, sunset coral, and warm sand. Atmospheric oceanic immersion inspired by twilight coastlines and creative engineering portfolios. Modes: Experience, Persuade.

| Role | Hex |
|---|---|
| Background | `#2A0E6E` |
| Surface | `#38168C` |
| Ink | `#F6F0E4` |
| Muted ink | `#D4CCE0` |
| Accent | `#E8826A` |
| Accent ink | `#1A083B` |

Ink on background: 13.4:1. Muted on background: 9.8:1. Accent on background: 5.7:1. Accent ink on accent: 6.9:1.

### 26. Night Sea
Deep abyssal midnight, cold celestial ink, and bioluminescent electric cyan. High-concept creative technologist and nocturnal immersion. Modes: Experience, Operate.

| Role | Hex |
|---|---|
| Background | `#070B2A` |
| Surface | `#0E1442` |
| Ink | `#E9EFFF` |
| Muted ink | `#A3B6E0` |
| Accent | `#6FE8FF` |
| Accent ink | `#03071E` |

Ink on background: 16.7:1. Muted on background: 9.5:1. Accent on background: 13.5:1. Accent ink on accent: 13.9:1.

### 27. Tomato Lagoon
Warm and loud on deep teal. A shock pairing resolved by value contrast. Appetite, travel, hospitality. Modes: Persuade, Experience.

| Role | Hex |
|---|---|
| Background | `#0C3B3C` |
| Surface | `#134E4F` |
| Ink | `#FFF0DC` |
| Muted ink | `#9CC7BF` |
| Accent | `#FF6A45` |
| Accent ink | `#1D0A04` |

Ink on background: 11.0:1. Muted on background: 6.6:1. Accent on background: 4.3:1. Accent ink on accent: 6.7:1.

### 28. Butter Ultramarine
A butter-yellow page with a hard electric blue. Playful, but serious about its type. Modes: Persuade, Operate.

| Role | Hex |
|---|---|
| Background | `#FFE27A` |
| Surface | `#FFEFA8` |
| Ink | `#10176B` |
| Muted ink | `#3E4590` |
| Accent | `#2437FF` |
| Accent ink | `#FFFFFF` |

Ink on background: 12.1:1. Muted on background: 6.7:1. Accent on background: 5.4:1. Accent ink on accent: 6.9:1.

### 29. Plum Chartreuse
Night-market plum with one sharp chartreuse hit. Keep the accent to tiny, precise moments. Modes: Experience, Persuade.

| Role | Hex |
|---|---|
| Background | `#2B0F42` |
| Surface | `#3B1A58` |
| Ink | `#F7F1FF` |
| Muted ink | `#BBA6D8` |
| Accent | `#D6FF3D` |
| Accent ink | `#1C2400` |

Ink on background: 15.2:1. Muted on background: 7.6:1. Accent on background: 14.6:1. Accent ink on accent: 14.0:1.

### 30. Oxblood Pistachio
Deep oxblood with pistachio. Rich and a little unexpected, for premium goods that want to avoid black and gold. Mode: Persuade.

| Role | Hex |
|---|---|
| Background | `#3A0B16` |
| Surface | `#4D1424` |
| Ink | `#F6EEE2` |
| Muted ink | `#CBA5AB` |
| Accent | `#B9E98A` |
| Accent ink | `#192808` |

Ink on background: 14.7:1. Muted on background: 7.7:1. Accent on background: 12.2:1. Accent ink on accent: 11.2:1.

### 31. Cobalt Lemon
A full-bleed cobalt page with lemon. Rare and memorable; use big type and few elements. Modes: Experience, Persuade.

| Role | Hex |
|---|---|
| Background | `#1B28F0` |
| Surface | `#2A37FF` |
| Ink | `#F8F6EC` |
| Muted ink | `#DADDFF` |
| Accent | `#FFE14A` |
| Accent ink | `#0F1470` |

Ink on background: 7.4:1. Muted on background: 6.0:1. Accent on background: 6.2:1. Accent ink on accent: 11.9:1.

### 32. Pool Cherry
Pool-blue paper with cherry red. Summery and graphic. Retail, events, consumer products. Mode: Persuade.

| Role | Hex |
|---|---|
| Background | `#BDEFF3` |
| Surface | `#D6F7F9` |
| Ink | `#07262E` |
| Muted ink | `#2F5963` |
| Accent | `#D8002A` |
| Accent ink | `#FFFFFF` |

Ink on background: 12.7:1. Muted on background: 6.2:1. Accent on background: 4.3:1. Accent ink on accent: 5.3:1.

### 33. Moss Hot Pink
Botanical moss with hot pink. Loud wellness for brands that do not want beige. Modes: Persuade, Experience.

| Role | Hex |
|---|---|
| Background | `#1D2B1A` |
| Surface | `#273826` |
| Ink | `#F1F5DF` |
| Muted ink | `#A9BB9C` |
| Accent | `#FF4F94` |
| Accent ink | `#2B0614` |

Ink on background: 13.4:1. Muted on background: 7.3:1. Accent on background: 4.8:1. Accent ink on accent: 6.0:1.

### 34. Denim Marigold
Workwear denim with a marigold signal. Craft, trades, logistics, tools. Modes: Operate, Persuade.

| Role | Hex |
|---|---|
| Background | `#1F3A5F` |
| Surface | `#2A4A74` |
| Ink | `#FFF6E5` |
| Muted ink | `#AFC3DD` |
| Accent | `#FFB400` |
| Accent ink | `#2A1D00` |

Ink on background: 10.7:1. Muted on background: 6.4:1. Accent on background: 6.4:1. Accent ink on accent: 9.2:1.

## Adapting a palette

1. Keep the semantic distinctions your interface needs; add or remove roles as the product requires.
2. Recheck all changed pairs. A passing ratio does not ensure that two colors communicate distinct meanings.
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
- Kids and family: Crayon.
- A bold, unexpected look for a consumer or creative product: Tomato Lagoon, Butter Ultramarine, Cobalt Lemon, Pool Cherry, or Moss Hot Pink.
- A rich premium look that avoids black and gold: Oxblood Pistachio or Plum Chartreuse.
- Workwear, trades, logistics: Denim Marigold.
- If the brand already has colors, use them and enforce the structure and the contrast floor.
