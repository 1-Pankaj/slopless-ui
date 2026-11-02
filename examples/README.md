# The examples

Three fictional businesses, each built twice: once the way a competent unguided model writes today, once with this skill. Each pair is a single self-contained HTML file. The finished pages ship one small dependency-free script, 150 lines or fewer, for their signature motion. No frameworks, no build step, and no assets beyond two font families.

| Pair | Category | Mode | Direction, adapted |
|---|---|---|---|
| [oscilla/](oscilla/) | realtime audio API | Persuade | Showroom, pairing 14, palette Volt |
| [outerform/](outerform/) | product studio | Experience | Broadside, pairing 20, palette Signal |
| [nocturne/](nocturne/) | music festival | Persuade | Marquee, pairing 16, palette Nightbus |

Every business is fictional and says so in its own footer. Phone numbers use Ofcom's reserved fictional range (01632 960xxx), emails use the reserved `.example` top level, and no metric is presented as real on a finished page. The before pages carry invented stats and testimonials on purpose: that is what the specimen documents.

## What is not wrong with the befores

Modern generated output cleaned up, and the befores reflect that. All three have semantic landmarks, visible or screen-reader labels, focus styles, passing contrast, no lorem ipsum, no alert dialogs, and nothing embarrassing. Two of the three are fully static, which is exactly how most unguided builds ship. A quick review would pass all of them. Passing is the problem: nothing in them could not be swapped to another business by changing the nouns.

## oscilla: a realtime audio API

`oscilla/before.html` vs `oscilla/index.html`.

| # | The before | The after | Rule |
|---|---|---|---|
| 1 | Inter as the identity font, one voice for everything | Space Grotesk for the voice, IBM Plex Mono for the instruments | [typography.md](../references/typography.md) |
| 2 | An indigo-to-fuchsia gradient on the headline word | Solid ink; the lime accent is reserved for the number the page is about | [anti-slop.md](../references/anti-slop.md) |
| 3 | "seamless", "effortless", "Ready to elevate" | "It lands in 31 ms." Units instead of adjectives | [copy.md](../references/copy.md) |
| 4 | Centered hero, centered section heads, centered everything | Left-aligned blocks, an asymmetric bento, whitespace with a job | [foundations.md](../references/foundations.md) |
| 5 | Three identical feature cards with icons | The actual quickstart in a copyable code block, live level meters, latency bars, a region list | [direction.md](../references/direction.md) |
| 6 | Zero motion; the page never answers | Masked line entrance, staggered reveals, count-ups, a magnetic CTA, and a waveform that follows the cursor | [motion.md](../references/motion.md) |
| 7 | "10,000+ developers", "50M+ minutes", invented and unbothered | Four numbers framed as measurements: "measured hourly from public probes. When a number slips, we publish it anyway." | [copy.md](../references/copy.md) |
| 8 | "Get Started Free", "Learn More" | "Start building", "See the numbers" | [icons-and-buttons.md](../references/icons-and-buttons.md) |
| 9 | No signature: swap the nouns and it is a cron-job vendor | The live waveform, named as the signature in the brief comment at the top of the source | [direction.md](../references/direction.md) |

## outerform: a product studio

`outerform/before.html` vs `outerform/index.html`. Experience mode: motion is part of the work.

| # | The before | The after | Rule |
|---|---|---|---|
| 1 | Inter, one voice, gray on white | Syne for the statement, Outfit for the body, Plex Mono for the meta | [typography.md](../references/typography.md) |
| 2 | Three portfolio tiles in purple gradients | Five covers drawn in CSS, one material each: teal card, orange poster, terminal, dunes, frequency bars | [anti-slop.md](../references/anti-slop.md) |
| 3 | "We craft seamless digital experiences that elevate your brand" | "SMALL STUDIO. LOUD WORK." A fragment that lands | [copy.md](../references/copy.md) |
| 4 | Services as three equal cards | Four capabilities in an accordion that opens with grid-template-rows | [direction.md](../references/direction.md) |
| 5 | A static page | A tilted capability ticker, an entrance for the headline, reveals, a cursor companion, and a work index whose covers chase the cursor | [motion.md](../references/motion.md) |
| 6 | "150+ projects", "98% client satisfaction", "12 design awards" | "26 products shipped, 9 people, 12 slides, deck maximum, 2 office dogs" | [copy.md](../references/copy.md) |
| 7 | A contact form that fakes submission with alert() | A mailto with an underline that draws; nothing pretends to have a backend | [anti-slop.md](../references/anti-slop.md) |
| 8 | "Get a Quote" | "Start a project", with an arrow that slides on hover | [icons-and-buttons.md](../references/icons-and-buttons.md) |
| 9 | No signature | The cursor-chasing preview, named in the brief; on touch it steps aside for inline covers | [motion.md](../references/motion.md) |

## nocturne: a music festival

`nocturne/before.html` vs `nocturne/index.html`.

| # | The before | The after | Rule |
|---|---|---|---|
| 1 | Inter everywhere, including prices and dates | Sora for the poster, JetBrains Mono for gates, stages, and euros | [typography.md](../references/typography.md) |
| 2 | A purple gradient on the title and a glow blob behind it | Solid ink with two teal letters; the one ambient is a slow field of light that breathes | [anti-slop.md](../references/anti-slop.md) |
| 3 | A countdown with frozen, fake numbers | Facts that do not tick: dates, doors, age limit in the meta row | [copy.md](../references/copy.md) |
| 4 | Three artist cards with an emoji where the photo goes | Three nights of named rows that fill with the accent on hover | [direction.md](../references/direction.md) |
| 5 | "World-class artists", "an atmosphere you will never forget" | "three nights, forty artists, one dockyard" | [copy.md](../references/copy.md) |
| 6 | Three "Buy Now" pills competing with each other | One filled "Get the full pass"; night and crew rows get quiet links | [icons-and-buttons.md](../references/icons-and-buttons.md) |
| 7 | "Limited availability. Prices increase soon!" | "prices rise 1 july. the full pass sold out in 2024 and 2025." Urgency from facts | [copy.md](../references/copy.md) |
| 8 | A static page | The ambient pauses offscreen and holds still under reduced motion; reveals, ticker, and hover choreography carry the rest | [motion.md](../references/motion.md) |
| 9 | No skip link, no reduced-motion story | Skip link, focus-visible styles, and a reduced-motion pass that keeps every fact readable | [verification.md](../references/verification.md) |

## What to notice in the afters, beyond the absence of slop

- **The brief is visible in the source.** The first CSS block of each after is the design contract from [direction.md](../references/direction.md), with the four-line brief and the signature named in a comment.
- **Each pair uses its direction's palette and pairing.** Volt with Space Grotesk; Signal with Syne and Outfit; Nightbus with Sora. The palettes and pairing numbers come straight from [../references/color.md](../references/color.md) and [../references/typography.md](../references/typography.md), adapted the way the direction text allows.
- **The motion budget is spent, not exceeded.** One entrance, quiet reveals, answers on every control, and exactly one signature ambient per page: the waveform, the cursor-chasing covers, the breathing field.
- **The copy passes the humanizer.** Units instead of adjectives, one aside with a pulse per page ("2 office dogs", "measured hourly, published even when a number slips", "the full pass sold out in 2024 and 2025").
- **Hierarchy survives the blur.** The squint thumbnails in [../docs/](../docs/).

## Verify it yourself

```bash
python3 scripts/foldcheck.py examples/oscilla/index.html     # passes, zero findings
python3 scripts/foldcheck.py examples/outerform/index.html   # passes, zero findings
python3 scripts/foldcheck.py examples/nocturne/index.html    # passes, zero findings
python3 scripts/foldcheck.py examples/oscilla/before.html    # fails, on real patterns
python3 scripts/foldcheck.py examples/outerform/before.html  # fails, on real patterns
python3 scripts/foldcheck.py examples/nocturne/before.html   # fails, on real patterns
python3 scripts/contrast.py "#EEF3E3" "#0B0D0A" "#16150F" "#F6F6F4" "#EAF1F4" "#0A0D12"
node scripts/finish.mjs examples/oscilla/index.html          # needs Playwright
```

Every finished page renders at 1440px and 390px with zero console errors, zero failed requests, and zero horizontal overflow. Screenshots live in [../docs/](../docs/).
