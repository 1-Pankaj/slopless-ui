# Typography

Typography affects voice, hierarchy, readability, and density. Use this reference when choosing or reviewing a type system; existing product conventions take precedence.

## Contents

- [License discipline](#license-discipline)
- [The two-voice rule](#the-two-voice-rule)
- [Pairings](#pairings)
- [The scale](#the-scale)
- [Rhythm rules](#rhythm-rules)
- [Loading](#loading)

## License discipline

Use fonts whose license and delivery terms fit the project. The families listed here were checked in November 2026 against the Google Fonts repository as OFL. Before shipping any font, verify its current license and the terms for self-hosting or serving it through a provider. When a project supplies a brand font, follow its approved usage and stop treating this list as a requirement.

## Typeface roles

One family can serve the whole interface, or distinct families can serve different roles. Choose based on the product voice, readability, available weights, language coverage, rendering, licensing, and performance. More families and weights add cost and should have a clear purpose, but there is no universal family limit.

- Familiar families including Inter, Roboto, Arial, and system fonts can be appropriate when they suit the product, platform, or performance constraints. A typeface alone does not make an interface generic.
- System fonts are useful both as deliberate choices and as fallbacks.
- Display faces live at large sizes. Many are single-weight or turn fragile below 24px. Read the family's page before using it small.

## Pairings

The pairings below are starting points. Check the current license and supported weights for any font you choose. Load only resources the project can use reliably, and provide appropriate fallbacks.

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
| 23 | Dela Gothic One | Epilogue | Sculptural Japanese-grotesque poster weight, humanist sans | Awwwards portfolios, creative technologist studios, immersive web |
| 24 | Syne | Mona Sans | Bold architectural geometry, high-trust engineered body | Creative tech agencies, standout engineering studios |

### Special purposes

| # | Display | Body | Voice | Strong for |
|---|---|---|---|---|
| 25 | Atkinson Hyperlegible | Atkinson Hyperlegible | One family, built for legibility | Civic, healthcare, education, accessibility-first |
| 26 | Bricolage Grotesque | Bricolage Grotesque | One quirky grotesque across all weights | Personal sites, newsletters, indie products |
| 27 | Silkscreen | Space Grotesk | Pixel face for tiny accents only | Game UI labels, retro touches, badges |

Notes:

- 25 and 26 are single-voice systems. Use weight and size for hierarchy.
- 15 and 17 keep one house style for UI and data. Set numbers with `font-variant-numeric: tabular-nums`.
- 27 is a seasoning, not a body face: Silkscreen below 14px is unreadable, and it never sets sentences.
- For anything read by many people, test at 200 percent zoom and at 390px width before shipping.

Fallback stacks end in a generic family and prefer faces the reader already has:

```css
--font-display: "Gloock", "Georgia", serif;
--font-body: "Public Sans", "Helvetica Neue", Arial, sans-serif;
```

## The scale

Define text roles and a usable scale that fits the interface. These values are examples, not fixed limits. Closely sized levels can be useful when weight, spacing, or color distinguishes them.

| Token | Size | Use |
|---|---|---|
| display | 44 to 64px | one per view, the signature |
| h1 | 32px | page title |
| h2 | 24px | section title |
| h3 | 18px | card or group title |
| body | 16px | paragraphs, UI text |
| small | 13px | captions and labels; verify legibility in context |

For marketing display type, `clamp()` keeps it fluid: `font-size: clamp(40px, 6vw, 64px)`.

## Rhythm rules

- Body line height 1.5 to 1.7. Headings 1.1 to 1.3.
- Line length 45 to 75 characters. A full-width paragraph on a desktop screen is a bug; set `max-width: 65ch` on reading columns.
- Align text according to its content and context. Centering can suit short statements, labels, and some branded compositions; sustained reading text often benefits from a consistent left edge and moderate line length.
- Tracking: slightly negative on display sizes (about -0.02em), zero on body, slightly positive on small all-caps labels (about 0.08em).
- Use casing and tracking consistently. All caps can serve labels, brands, abbreviations, or display work; check readability and avoid using it as unexplained decoration.
- Numbers in tables and metrics: tabular figures so columns align.
- Never name a font you have not loaded, and always declare a fallback. Test with fonts blocked; the page must still be legible.

## Loading

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Gloock&family=Public+Sans:wght@400;600&display=swap" rel="stylesheet">
```

Use loading behavior and hosting that fit the product's reliability, privacy, and performance needs. Each additional font file has a transfer and rendering cost; weigh it against the visual and functional benefit.
