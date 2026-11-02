# Typography

Type is the interface. Before color, before layout, a page is typography: size, weight, width, and rhythm decide whether it feels designed or assembled. Open this at step 3.

## Contents

- [License discipline](#license-discipline)
- [The two-voice rule](#the-two-voice-rule)
- [Pairings](#pairings)
- [The scale](#the-scale)
- [Rhythm rules](#rhythm-rules)
- [Loading](#loading)

## License discipline

Recommend and load only fonts with licenses that permit free commercial use and redistribution: SIL Open Font License (OFL) or Apache. Every family named in this file was verified, in November 2026, against the canonical google/fonts repository (github.com/google/fonts), where each family carries a `METADATA.pb` declaring `license: "OFL"`. To re-verify a family, open `https://github.com/google/fonts/tree/main/ofl/<family-name>` and read the license line. When a project brings its own brand font, use it and stop. Never hotlink fonts from random CDNs, never bundle font files without their license file, and never ship a font you cannot name the license of.

## The two-voice rule

Use at most two families: a display voice with character for headings, and a workhorse voice for body and UI. Two weights each is a normal budget; five is a redesign waiting to happen. One family doing both jobs is also fine when the family has a real weight range.

- Inter, Roboto, Arial, and the system stack are fine as body faces. As the identity font they are the fastest way to look generated. If you must use one, pair it with a display face that carries the personality.
- System fonts are acceptable for internal tools where speed beats voice, and always as fallbacks.
- Display faces live at large sizes. Many are single-weight or turn fragile below 24px. Read the family's page before using it small.

## Pairings

All verified OFL. Each pairing states its voice and where it is strong. Load from Google Fonts or self-host; always keep the fallback stack.

### Editorial and reading

| # | Display | Body | Voice | Strong for |
|---|---|---|---|---|
| 1 | Gloock | Public Sans | High-contrast poster serif over a civic sans | Editorial landing pages, publications |
| 2 | Newsreader | Spline Sans | Reading serif with a fresh, slightly technical sans | Docs, essays, long-form products |
| 3 | Crimson Pro | Work Sans | Book-face serif, honest grotesque | Reading-heavy sites, research, essays |
| 4 | Literata | Source Sans 3 | Screen-first book serif, plain sans | Knowledge bases, manuals, long guides |
| 5 | Playfair Display | Source Sans 3 | Newspaper elegance over a plain workhorse | Culture, archives, magazines |
| 6 | Libre Caslon Text | Figtree | Old-style authority, clean geometric body | Legal, finance, institutional trust |
| 7 | Marcellus | Mulish | Roman inscription caps, neutral friendly body | Hospitality, galleries, premium services |

### Product and consumer

| # | Display | Body | Voice | Strong for |
|---|---|---|---|---|
| 8 | Gabarito | Schibsted Grotesk | Rounded geometric display, precise body | Consumer products that want character without noise |
| 9 | DM Serif Display | DM Sans | Tight display serif, geometric body | Startup marketing, product sites |
| 10 | Young Serif | Instrument Sans | Chunky warm serif, neutral sans | Farm shops, food brands, friendly retail |
| 11 | Fraunces | Hanken Grotesk | Wonky old-style serif, soft grotesque | Bakeries, restaurants, warm DTC brands |
| 12 | Baloo 2 | Nunito Sans | Rounded and friendly, humanist body | Kids, family products, toy brands |

### Technical and data

| # | Display | Body | Voice | Strong for |
|---|---|---|---|---|
| 13 | Zilla Slab | Onest | Slab warmth, modern body | Developer tools with a human side |
| 14 | Space Grotesk | IBM Plex Sans | Technical grotesque, engineered body | Dev-facing SaaS, technical product pages |
| 15 | IBM Plex Sans | IBM Plex Mono | One engineered house, mono for data | Dashboards, internal tools, Operate mode |
| 16 | Sora | JetBrains Mono | Geometric display, code-native body | Developer landing pages, API products |
| 17 | Spline Sans Mono | Spline Sans | Mono-forward for data-dense screens | Terminals, logs, dense tables |

### Display and voice

| # | Display | Body | Voice | Strong for |
|---|---|---|---|---|
| 18 | Cormorant Garamond | Karla | Delicate display serif, plain sturdy sans | Fashion, portfolios, Experience mode |
| 19 | Bodoni Moda | Archivo | Didone fashion voice, engineered sans | Luxury retail, editorial fashion |
| 20 | Syne | Outfit | Art-institution display, clean geometric | Agencies, exhibitions, campaigns |
| 21 | Oswald | Barlow | Condensed poster voice, neutral body | Sports, transit, industrial |
| 22 | Bebas Neue | Libre Franklin | All-caps poster face, franklin body | Events, film, box offices, posters |

### Special purposes

| # | Display | Body | Voice | Strong for |
|---|---|---|---|---|
| 23 | Atkinson Hyperlegible | Atkinson Hyperlegible | One family, built for legibility | Civic, healthcare, education, accessibility-first |
| 24 | Bricolage Grotesque | Bricolage Grotesque | One quirky grotesque across all weights | Personal sites, newsletters, indie products |
| 25 | Silkscreen | Space Grotesk | Pixel face for tiny accents only | Game UI labels, retro touches, badges |

Notes:

- 23 and 24 are single-voice systems. Use weight and size for hierarchy.
- 15 and 17 keep one house style for UI and data. Set numbers with `font-variant-numeric: tabular-nums`.
- 25 is a seasoning, not a body face: Silkscreen below 14px is unreadable, and it never sets sentences.
- For anything read by many people, test at 200 percent zoom and at 390px width before shipping.

Fallback stacks end in a generic family and prefer faces the reader already has:

```css
--font-display: "Gloock", "Georgia", serif;
--font-body: "Public Sans", "Helvetica Neue", Arial, sans-serif;
```

## The scale

Pick 5 or 6 sizes and never leave them. Adjacent sizes must differ by at least 25 percent or they read as a mistake. A working scale for product UI (base 16):

| Token | Size | Use |
|---|---|---|
| display | 44 to 64px | one per view, the signature |
| h1 | 32px | page title |
| h2 | 24px | section title |
| h3 | 18px | card or group title |
| body | 16px | paragraphs, UI text |
| small | 13px | captions, labels, never below 12px |

For marketing display type, `clamp()` keeps it fluid: `font-size: clamp(40px, 6vw, 64px)`.

## Rhythm rules

- Body line height 1.5 to 1.7. Headings 1.1 to 1.3.
- Line length 45 to 75 characters. A full-width paragraph on a desktop screen is a bug; set `max-width: 65ch` on reading columns.
- Left-align text blocks. Centered paragraphs and centered buttons-on-center are the most reliable tells of generated layout. Center only short, single-line elements: a hero line, a figure caption.
- Tracking: slightly negative on display sizes (about -0.02em), zero on body, slightly positive on small all-caps labels (about 0.08em).
- All-caps is a costume. Use it for one small label style at most, never for whole sentences, never for accessibility-critical text.
- Numbers in tables and metrics: tabular figures so columns align.
- Never name a font you have not loaded, and always declare a fallback. Test with fonts blocked; the page must still be legible.

## Loading

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Gloock&family=Public+Sans:wght@400;600&display=swap" rel="stylesheet">
```

Two families, two or three weights total, `display=swap`. Self-host (Fontsource packages or your own files) when the product must not depend on a third party. Every extra weight is a real network cost on a phone.
