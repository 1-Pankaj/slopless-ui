# Anti-slop catalogue

The patterns that make output look machine-made, why each one reads that way, and what to do instead. Open this when something you built feels familiar in a bad way, and run it as a review checklist before delivery. `scripts/foldcheck.py` catches many of these mechanically; this file catches the rest.

Status: this is a maintained opinion list, not a measurement. When you find a new pattern in your own output, add it here and, if it is mechanical, add a rule to foldcheck.

## Motion and light

| Pattern | Why it reads as slop | Do instead |
|---|---|---|
| A page with no motion at all | The assembled-template look: a layout nobody was present for | The motion budget ([motion.md](motion.md)): press answers on every control, one entrance, quiet reveals, at most one named signature ambient |
| Blinking, pulsing, or bouncing dots (typing indicators, "live" badges, status dots) | Fake liveness on static content; the first thing the eye finds and cannot stop watching | Motion only when a real state exists (uploading, saving). A calm label often beats any dot. |
| Floating, drifting, or glowing orbs behind content | Light with no source; present on every generated hero since the same week | Whitespace and a border. Sections separate with space, not atmosphere. |
| Shimmer on static text, spinning rings, pulsing badges, tickers of adjectives | The page is performing instead of working | The only loops that ship are loading states, content tickers carrying real names, and the one signature ambient named in the brief. Tickers pause on hover; everything holds still under reduced motion. |
| Fade-and-slide on every section, identical timing | The rhythm of ten thousand generated pages | One deliberate entrance moment for the signature; the rest reveal once, quietly, with varied stagger |
| Hover scale or shadow bloom on non-clickable things | Implies interactivity that is not there | Hover states only on things that respond; one property change |
| Animating width, height, top, left | Jank on real hardware | Transform and opacity (grid-template-rows for accordions is the one exception) |

## Color and light effects

| Pattern | Why it reads as slop | Do instead |
|---|---|---|
| Purple-to-blue / indigo-to-fuchsia hero gradient | The most common generated background in existence | One flat color, or a palette from [color.md](color.md) |
| Rainbow hue-to-hue gradients (orange-to-teal banners, multicolor section washes) | Loudness in place of a decision, and it dates the page on arrival | One flat color, or a barely visible material shift |
| Gradient-filled headline text | Dates instantly, usually fails contrast | Solid ink; let the typeface carry the headline |
| Neon greens, cyberpunk, glitch, synthwave, vaporwave, holographic, "matrix" styling | A theme-store preview, not a product | Style from print, packaging, tools, wayfinding |
| Glow shadows (large colored blurs), neon borders, dark mode as black plus neon | Loudness substituted for hierarchy | Tinted neutrals, one considered accent, elevation from subtle shadow or border |
| Rainbow status dots (red/green/blue chips everywhere) | Color without meaning | Semantic colors only for meaning, paired with text or icon |
| Default framework palette, unmodified | Nothing was decided | Tint neutrals toward a material; one accent with a job |
| Glassmorphism by default | Legibility suffers; every card looks wet | Solid surfaces; blur only on overlays where it aids reading |

## Typography

| Pattern | Why it reads as slop | Do instead |
|---|---|---|
| Inter / Roboto / Arial / system stack as the identity font | The default is a decision not to decide | A display voice plus a workhorse body ([typography.md](typography.md)) |
| Gradient, glowing, or outlined display text | Costume jewelry | Size, weight, and the typeface's own character |
| All-caps eyebrow label above every heading | Template rhythm | One label style at most, only when it carries information |
| Sizes too close together (18px next to 20px) | Looks like a mistake, is one | A scale with 25 percent or more between adjacent sizes |
| Text below 12px anywhere, captions included | Unreadable, and it reads as careless, not compact | A 12px floor, held everywhere |
| Centered paragraphs, centered everything | Generated pages center out of fear | Left-align text blocks; center only short single lines |

## Layout and structure

| Pattern | Why it reads as slop | Do instead |
|---|---|---|
| Three identical feature cards (icon, title, blurb) | Nobody decided anything | Make one thing primary and large; list the rest as text |
| Uniform card grids for content that is not cards | Boxes replace hierarchy | Spacing and dividers; cards only for distinct objects you open or act on |
| Hero + features + testimonials + pricing + footer, in that order, always | The default template has no product in it | Start from the product's most characteristic content |
| Everything full-bleed with no max-width | Reading lines of 140 characters | A content column; let one or two elements break the grid on purpose |
| Rounded pill everything (border-radius 9999px on all controls) | Shape as fashion, not meaning | A radius scale of two or three values matched to element size |
| A dashboard of four KPI cards, one line chart, one table | The default dashboard, no decision behind it | Lead with the decision the viewer makes here |

## Content

| Pattern | Why it reads as slop | Do instead |
|---|---|---|
| Em dashes everywhere | The signature punctuation of machine text | Periods, commas, colons, parentheses ([copy.md](copy.md)) |
| "Seamless", "revolutionary", "unlock", "elevate", "delve", "tapestry" | Words standing where information should be | Say what it does, concretely |
| Lorem ipsum, "coming soon", TODO markers visible in UI | Unfinished, and it looks it | Real copy, even two honest sentences |
| "10,000+ happy customers", fake testimonials, fake logos | Fabrication the viewer can smell | Omit, or mark clearly as placeholder |
| Stock-photo or placeholder-service hotlinks | Break, change, are not yours | Local assets, SVG or CSS compositions, labeled placeholders |
| Random smooth chart lines with no axes or units | Obviously fake data | Realistic values with noise, labeled axes, units |
| Emoji as icons, bullets, or chrome | No control of size, weight, or platform | One icon set, or plain text |

## Interaction and systems

| Pattern | Why it reads as slop | Do instead |
|---|---|---|
| A button on every action, buttons in nav, buttons on buttons | No hierarchy, no decisions | One filled button per view; links and quiet controls for the rest |
| Icon soup (an icon on every card heading, mixed sets, broken weights) | Decorative noise, looks unmaintained | Icons only where they carry meaning; one set, one weight |
| Placeholder text as the field label | Disappears on focus; fails accessibility | Visible label above every field |
| Whole-page spinner for a partial refresh | Hides what already loaded | Skeletons matching the layout, or inline progress |
| `alert()`, `confirm()`, `prompt()` for product UI | Breaks flow, cannot be styled | Inline confirmation, dialogs, toasts with `role="status"` |
| Raw hex values scattered through components | Cannot retheme or audit | Role tokens in the design contract |
| Happy path only | Looks finished until the first empty list | Empty, loading, error, and long-content states designed like the rest |
