# Direction

How to decide what a thing should look like before building it. Open this at step 2 of the method, on every new page, screen, or restyle.

## Contents

- [Why a brief comes first](#why-a-brief-comes-first)
- [The four lines](#the-four-lines)
- [Modes](#modes)
- [The modern register](#the-modern-register)
- [The style library](#the-style-library)
- [The design contract](#the-design-contract)
- [The stranger test](#the-stranger-test)

## Why a brief comes first

Without written decisions, an agent falls back to its defaults, and defaults are why generated interfaces all look alike. The brief is four lines. It costs one minute and it removes most revision rounds, because every later choice checks against it instead of against taste in the moment.

## The four lines

Write them as a comment, a plan note, or the top of your final report.

1. **Audience.** Who is here and what are they doing in ten seconds. "A project manager scanning yesterday's failures" is a brief. "Users" is not.
2. **Feeling.** One or two adjectives you could defend: calm, dense, warm, exact, sturdy, quiet. If the adjectives would describe any other product in this category, pick again.
3. **Signature.** The one thing a stranger remembers. An unusual typeface, one oversized number, one unexpected color, one strong composition, one honest sentence. A screen with one memorable decision beats a screen with ten safe ones.
4. **Mode.** Persuade, Operate, Read, or Experience (table below). Mode sets spacing, motion, density, and how loud the accent may be.

## Modes

| Mode | The person is | Typical surfaces | Consequences |
|---|---|---|---|
| Persuade | deciding whether to act | landing pages, pricing, marketing | Type and color may carry personality. One primary action. One entrance choreography, one signature ambient if the product has a material to show, and every control answers on press. |
| Operate | completing a task | dashboards, app screens, admin tools | Density is a feature. Everything aligns. Motion is nearly silent: press states, focus, panel transitions. No ambient. Accent only for meaning. |
| Read | understanding something | docs, articles, guides, email | The column is the interface. 45 to 75 characters. Almost no motion: link states, focus, one quiet reveal. Comfortable line height. |
| Experience | exploring the work | portfolios, galleries, showcases | Whitespace leads. Few elements. Motion is part of the work: a signature ambient, hover choreography, and transitions that carry the visitor between views. |

## The modern register

Every direction in the library is executed in the current web's register unless the brief genuinely asks for something else. The register is not a style; it is the floor:

- **Confident scale.** Display type that owns the first viewport, with real distance between scale steps. A page whose largest text is 28px has not decided anything.
- **A pulse.** The motion budget from [motion.md](motion.md): answers on every control, one entrance, quiet reveals, at most one named ambient. A fully static page in 2026 reads as a template.
- **Asymmetry on purpose.** Left-aligned text, grids with one element breaking them, whitespace that points somewhere. Centered-everything is the layout equivalent of a shrug.
- **Real content density.** The page carries the product's actual nouns: numbers with units, named rows, working microcopy. Marketing pages that are five headlines and three cards have no product in them.

Print-flavored devices (hairline rules, ledger tables, paper palettes, serif voices) are legitimate choices from the library below, made when the brief calls for them. They are not a default safety zone, and they are not an excuse for a page that never moves.

## The style library

Twenty-eight starting directions. They exist so that no two projects in different categories come out looking alike: a bakery and a bank should never share a stylesheet. Work like this:

1. Find your category in the router below and take its direction.
2. Treat the direction as a starting point, not a costume: change at least two things (a typeface from the pairing's group, the accent hue within its contrast budget, a layout move) until the choice is specific to this product.
3. If the project already has a brand, follow it and skip the library entirely.

### Router: category to direction

| You are building | Start with |
|---|---|
| SaaS or startup product site | Showroom |
| Dashboard, admin, internal tool | Instrument |
| Developer docs, knowledge base | Manuscript |
| Blog, newsletter, personal site | Zine |
| Fashion, jewelry, beauty retail | Atelier |
| Wellness, skincare, health products | Apothecary |
| Restaurant, cafe, bar | Brasserie |
| Food products, grocery, farm sales | Pantry |
| Travel, tours, hospitality | Atlas |
| Architecture, real estate, interiors | Blueprint |
| Education, courses, schools | Primer |
| Government, civic, nonprofit | Commons |
| Legal, compliance, professional services | Notary |
| Banking, fintech, insurance | Teller |
| Creative agency, studio, campaign | Broadside |
| Photography, film, visual portfolio | Darkroom |
| Art gallery, premium services | Gallery |
| Music, film, events, ticketing | Marquee |
| Sports, fitness, competition | Scoreboard |
| Games and playful products | Cartridge |
| Kids, family, toys | Crayon |
| Community, forum, membership site | Bulletin |
| Museum, archive, library | Catalogue |
| Industrial, automotive, manufacturing | Machine Shop |
| Sustainability, outdoors, climate | Greenhouse |
| Publications, long-form editorial | Ledger |
| Healthcare, utilities, high-stakes forms | Field Guide |
| Friendly consumer products | Counter |

### The directions

Each entry: who it is for, its modes, where to start in [typography.md](typography.md) (pairing numbers) and [color.md](color.md) (palette names), the one move that makes it recognizable, and the way it usually fails.

**The Ledger.** For publications, documentation, finance and anything that wants trust without warmth. Modes: Read, Persuade. Pairings 1, 5, 6. Palette: Ledger. The move: a strong reading column, hairline rules, numbered sections like an account book. Watch out: it slides into dullness unless the display face is genuinely confident.

**The Instrument.** For dashboards, internal tools, developer products. Modes: Operate. Pairings 15, 17, 14. Palettes: Harbor light, Peat or Reef dark. The move: tabular figures everywhere, hairline borders instead of shadows, a grid you could check with a ruler. Watch out: density is fine, misalignment is not. One misaligned column ruins the authority.

**The Print Shop.** For studios, makers, food, community, physical products. Modes: Persuade, Experience. Pairings 11, 10. Palette: Furrow. The move: warm paper, a characterful display face, real textures implied by type and rules rather than effects. Watch out: warmth without contrast fails accessibility; check every pair.

**The Gallery.** For premium services, hospitality, portfolios. Modes: Experience, Persuade. Pairings 7, 18. Palettes: Verdigris, Mulberry. The move: enormous whitespace, few elements, one deep accent, slow motion. Watch out: the fix for crowding is deletion, not smaller text.

**The Field Guide.** For civic services, healthcare, education, anything where mistakes cost. Modes: Read, Operate. Pairing 23. Palette: any, at maximum contrast. The move: generous legible type, status always paired with words, every element helping someone finish a task. Watch out: plain is the point, but plain is not brittle: it still gets all eight states.

**The Counter.** For friendly consumer products and brands with personality. Modes: Persuade. Pairings 8, 12. Palettes: Crayon, Harbor. The move: rounded display voice, tinted surfaces, one warm accent. Watch out: low-saturation palettes fail contrast; measure everything.

**The Showroom.** For SaaS products, hardware, startups. Modes: Persuade, Operate. Pairings 9, 14. Palettes: Harbor, Blueprint. The move: the product is the hero; one confident statement, one real screenshot or diagram, one button. Watch out: the purple gradient is the enemy you were born to fight; a flat material color reads more expensive.

**The Manuscript.** For docs, knowledge bases, manuals. Modes: Read. Pairings 2, 4. Palettes: Ledger, Slate, Verdigris. The move: a single tireless reading column, a table of contents that behaves, code blocks with real syntax styling. Watch out: navigation must never exceed two levels of depth on screen.

**The Zine.** For personal sites, blogs, newsletters, indie products. Modes: Read, Persuade. Pairing 24. Palette: Zine. The move: one loud voice, visible structure like a photocopied page, opinions in the copy. Watch out: quirky type still needs a scale; do not let the voice set the body text below 16px.

**The Broadside.** For agencies, campaigns, exhibitions. Modes: Persuade, Experience. Pairing 20. Palettes: Slate, Zine. The move: a poster's confidence in a web page: huge display type, one uncropped image, one action. Watch out: big type needs bigger discipline in line breaks and tracking.

**The Darkroom.** For photography, film, visual portfolios. Modes: Experience. Pairings 18, 7. Palettes: Darkroom, Reef. The move: dark warm neutrals so images glow by comparison, captions in small type, nothing competing with the work. Watch out: dark mode contrast rules from [color.md](color.md) apply twice as strictly.

**The Marquee.** For music, film, events, ticketing. Modes: Persuade. Pairing 22. Palette: Marquee. The move: poster typography, a date and a city treated like the headline, one gold accent on a dark room. Watch out: all-caps display is a costume; it stays on the poster line, never on sentences.

**The Atelier.** For fashion, jewelry, beauty, weddings. Modes: Experience, Persuade. Pairings 18, 19. Palette: Mulberry. The move: cloth-like space, hairline rules, a didone or garalde voice, photography with room around it. Watch out: luxury dies of clutter; delete until it hurts.

**The Apothecary.** For wellness, skincare, health products. Modes: Persuade, Experience. Pairings 3, 11. Palette: Apothecary. The move: plaster neutrals, measured serif voice, ingredient-style lists with tabular numbers. Watch out: the category drifts into pastel mush; keep the ink dark and the claims concrete.

**The Brasserie.** For restaurants, cafes, bars. Modes: Persuade, Experience. Pairings 11, 13. Palettes: Furrow, Mulberry. The move: a menu is a list, so set it like one: names left, prices right, dot leaders or a clean rule between. Watch out: centered hero paragraphs and star ratings clip art read as template; the menu itself is the design.

**The Pantry.** For food products, grocery, farm shops. Modes: Persuade. Pairings 10, 11. Palette: Furrow. The move: label typography, a shelf of real product shots, prices and weights in tabular figures. Watch out: rustic does not mean unreadable; hold the line at 16px body.

**The Atlas.** For travel, tours, hospitality. Modes: Persuade, Operate. Pairing 7. Palette: Atlas. The move: map-paper neutrals, routes and dates as first-class content, itinerary rows with tabular figures. Watch out: stock sunset photos are the category's slop; use typography and structure to carry the promise.

**The Blueprint.** For architecture, real estate, interiors. Modes: Persuade, Experience. Pairings 14, 6. Palette: Blueprint. The move: drafting discipline: a strict grid, measurements as decoration (real ones), drawings or floor plans as imagery. Watch out: blueprint-blue backgrounds are a costume; keep the paper light and the lines fine.

**The Primer.** For education, courses, schools. Modes: Read, Operate. Pairings 8, 23. Palettes: Harbor, Ledger. The move: clear steps, numbered lessons, one friendly accent, progress you can see. Watch out: playfulness belongs in illustration and copy, not in wobbly layouts.

**The Commons.** For government, civic groups, nonprofits. Modes: Read, Operate. Pairings 23, 6. Palettes: Verdigris, Ledger. The move: institutional clarity: high contrast, formal hierarchy, dates and deadlines impossible to miss. Watch out: clip-art handshakes and stock flags are slop here more than anywhere.

**The Notary.** For legal, compliance, professional services. Modes: Read, Persuade. Pairings 6, 5. Palettes: Ledger, Slate. The move: the document is the interface: numbered clauses, definitions set apart, a serif with authority. Watch out: no marketing gradients within a mile of a terms page.

**The Teller.** For fintech, banking, insurance. Modes: Operate, Persuade. Pairings 15, 1. Palette: Teller. The move: engraved-stationery calm: banknote neutrals, one deep green, balances in tabular figures with thousands separators. Watch out: money numbers never round, never animate for decoration, and always carry their currency.

**The Scoreboard.** For sports, fitness, competition. Modes: Operate, Persuade. Pairing 21. Palette: Scoreboard. The move: condensed type, live scores as tabular figures, one signal color on a varsity neutral. Watch out: athletic does not mean aggressive; do not shout in more than one place.

**The Cartridge.** For games and playful products. Modes: Persuade, Experience. Pairings 25, 16. Palettes: Crayon light, Reef dark. The move: one pixel-voice accent (Silkscreen for tiny labels only) over a solid modern layout. Watch out: the line between playful and cyberpunk is the ban list; glow and scanlines stay out.

**The Crayon.** For kids, family, toys. Modes: Persuade, Experience. Pairing 12. Palette: Crayon. The move: chunky rounded type, generous hit areas (bigger than 44px, kids' hands miss), color that comes from the palette, not the rainbow. Watch out: still one accent; children's design is not an excuse for every color at once.

**The Catalogue.** For museums, archives, libraries. Modes: Read, Experience. Pairings 5, 2. Palettes: Verdigris, Ledger. The move: accession-number discipline: every object gets a number, a caption, and room; the grid is the collection. Watch out: reverence is not grayness; keep contrast up and type confident.

**The Machine Shop.** For industrial, automotive, manufacturing. Modes: Operate, Persuade. Pairings 21, 14. Palette: Slate. The move: specification-sheet typography, tolerances and part numbers in mono, safety accents used only for safety. Watch out: this category earned its conventions; heavy borders and dense tables are correct, not dated.

**The Greenhouse.** For sustainability, outdoors, climate. Modes: Persuade, Read. Pairings 10, 3. Palettes: Furrow, Verdigris. The move: field-notebook layout, data tables that admit uncertainty (units, ranges, dates), imagery of the actual place. Watch out: leafy green gradients are the category's default slop; a flat furrow palette is more believable.

## The design contract

After the brief, write five decisions as real values before building. This is the contract later steps check against, and the file future sessions read:

```css
/* Example contract for oscilla, a realtime audio API landing page (Persuade).
   The full page is examples/oscilla/index.html. */
:root {
  --font-display: "Space Grotesk", "Helvetica Neue", sans-serif;  /* voice: engineered */
  --font-mono: "IBM Plex Mono", monospace;                        /* voice: instruments */
  --bg: #0B0D0A;            /* graphite with a green cast */
  --ink: #EEF3E3;
  --accent: #C6F24E;        /* electric lime, the signal color */
  --accent-ink: #131A02;    /* ink that sits on the accent */
  --space-unit: 8px;        /* scale: 8, 16, 24, 40, 64, 96 */
  --radius: 10px;
  --motion-fast: 140ms; --motion-base: 300ms;
  --ease-out: cubic-bezier(0.22, 1, 0.36, 1);
}
```

Rules for the contract:

- Five to eight values. A contract nobody rereads is decoration.
- Name fonts you will actually load, with a fallback stack, and load only the weights you use.
- The accent gets one job. If it appears on ten elements, it is not an accent.
- Check contrast on every text pair now, not after thirty components (see [verification.md](verification.md)).

## The stranger test

Before building, imagine showing the finished page to a stranger for three seconds, then asking: what is this, what does it want from me, and what do I press. If the stranger cannot answer, the composition needs work regardless of how finished the code looks. After building, run the same test on a screenshot (this is the squint test in [verification.md](verification.md)).
