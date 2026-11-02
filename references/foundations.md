# Foundations

The laws underneath the taste. A style direction is an opinion; this file is the part that is not negotiable, because it comes from how people actually see, read, and move through interfaces. Generated UI breaks these laws constantly, which is why it reads as generated. Open this at step 3 or 4, whenever you are deciding layout, spacing, hierarchy, or behavior.

Some of the rules here carry names because researchers documented them. Jon Yablonski's Laws of UX (lawsofux.com) is a good public collection with sources; Material Design and the Apple Human Interface Guidelines document the same physics from the platform side. Nothing in this file is invented.

## Space: the scale is the law

- **Work on a 4 or 8 point grid.** Every padding, margin, and gap is a multiple of 4 (or 8): 4, 8, 12, 16, 24, 32, 48, 64, 96. Off-scale values are how pages start looking accidental. Material Design's layout grid runs on 8dp; most mature design systems run on the same idea.
- **Spacing is a relationship.** Things that belong together sit closer than things that do not. Space groups before borders do: if you need a box to make two things look related, move them closer and delete the box (the Gestalt law of proximity, in one line).
- **Spacing scales with importance.** Inside a component: 4 to 16. Between sibling components: 16 to 32. Between sections of a page: 48 to 96. A section title 12px above its section is a lie about the structure.
- **Density follows mode.** Persuade and Experience pages breathe (generous space, few elements). Operate pages compress (dense rows, tight padding, alignment does the work). Read pages get one comfortable column and stop.

## Layout: one grid, one column, one axis

- **Pick a layout system before placing anything.** A 12-column grid, or a single centered content column with a maximum width. Elements snap to it or deliberately break it once, with intent.
- **Reading columns hold 45 to 75 characters** (`max-width: 65ch` is a good default). A paragraph spanning 1400px is a bug, not a style.
- **Left-align text blocks.** Centered paragraphs force the eye to hunt for a new line start every line. Center only short, single lines: a hero statement, a figure caption.
- **Scanning follows known shapes.** Text-heavy pages scan in an F; posters and landing pages scan in a Z. Put the first thing people need where the scan already goes: top-left to top-right, then down.
- **Align to one axis per region.** Left edges line up across sections; gutters stay the same width. One misaligned edge reads as broken even when nobody can say why.

## Hierarchy: one thing must be loudest

- **Every view has exactly one focal point.** Size, weight, color, and space create it. Boxes and backgrounds do not; they flatten hierarchy by giving everything a container.
- **The isolation effect (von Restorff):** the item that differs from its surroundings is the one people remember. This is why one accent color with one job works, and why four uniform feature cards with icons do not.
- **Adjacent levels must be distinct.** Sizes in a scale differ by at least 25 percent, and a page uses at most 5 or 6 levels. An 18px heading over 16px body text reads as an accident.
- **Order of operations when a page feels flat:** more space around the focal point, then more size contrast, then more weight contrast. Color is the last lever, not the first.

## The named laws, and what each one costs you when ignored

| Law | What it says | Consequence in UI |
|---|---|---|
| Jakob's law | People spend most of their time on other products and expect yours to work the same way | Put the logo top left, the primary action top right, search where search always is. Invent convention only when you are paid in attention |
| Fitts's law | Time to hit a target depends on its size and distance | Primary actions are large and near the cursor's likely position. Touch targets at least 44 by 44 pixels (Apple's floor; Material asks 48dp) |
| Hick's law | Each added choice costs decision time | One primary action per view. Navigation holds 5 to 7 items. Settings pages are the only place for walls of options |
| Miller's note on memory | People hold only a few chunks in working mind at once (the classic 1956 paper says 7 plus or minus 2; later work argues for fewer) | Group digits in phone numbers and cards, chunk forms into steps, never demand a list be held in the head |
| Doherty's threshold | Systems feel responsive when they react in well under about 400 ms | Hover states instant, skeletons before spinner, optimistic updates where safe |
| Tesler's law of conservation of complexity | Every system has complexity that cannot be removed, only moved | Move it into defaults, smart starting points, and sensible limits, not into the user's first five minutes |
| Serial position effect | The first and last items in a sequence are remembered best | Key navigation items go first and last; the primary call to action gets the end of the page |
| Aesthetic-usability effect | People read attractive interfaces as easier to use, which buys patience for small friction | It earns goodwill, it does not fix broken flows. Polish after the flow works, never instead |

## States: a component is not done until all of them exist

Every interactive component carries eight states, each designed, even if three of them turn out to look identical:

1. **Rest** (the default)
2. **Hover** (pointer over it)
3. **Focus-visible** (keyboard arrival, always a visible ring, never `outline: none` without a replacement)
4. **Active** (being pressed)
5. **Disabled** (greyed and unclickable, with the reason nearby when it matters)
6. **Loading** (the same footprint as the content, so nothing jumps)
7. **Empty** (what this area looks like with zero items, plus the first action)
8. **Error** (what it looks like when the data or the input is wrong)

The long-content state is ninth: the table with 400 rows, the heading that wraps to three lines, the name in a language twice as long as the design assumed. Sample data rules live in [copy.md](copy.md).

## Elevation, borders, and depth

- **Borders before shadows, shadows before blur.** A 1px border in the ink color at low opacity is the honest way to separate. Elevation shadows stay small (4 to 16px blur, low opacity, near-black, never colored glow).
- **Z-index is a scale, not a number salad.** Three or four named tiers (base, raised, overlay, toast) defined as tokens. Two hundred unspecified z-indexes is how dropdowns end up under modals.
- **Dark mode is a translation.** See rule 6 in [color.md](color.md). Shadows stop working on dark backgrounds; borders and surface lightness take over.

## Motion physics (summary; full rules in [motion.md](motion.md))

- Transform and opacity only. 100 to 200ms for hover and focus, 240 to 400ms for entrances with a strong ease-out, exits faster than entrances, nothing loops unless it reports a real state, and the reduced-motion fallback ships every time.

## Focus, keyboard, and the small print

- Every interactive element is reachable by Tab, in reading order, with a visible focus ring (`:focus-visible`). Dialogs trap focus and close on Escape.
- Every page offers a skip link to the main content. It is invisible until focused, and it is one line of HTML.
- Text never drops below 12px, anywhere, for any reason. Captions included.
- WCAG 2.1 AA is the floor, not the goal: 4.5:1 for body text, 3:1 for large text and for the boundaries of the controls people must find.

## Performance is part of design

- Two font families, at most three weights total, loaded with `display=swap` and a fallback stack that matches metrics closely enough to avoid a visible jump.
- Images get explicit width and height so the layout does not shift when they arrive. Full-bleed heroes get a background color that matches the image's average, so the arrival is quiet.
- Animation touches `transform` and `opacity` only; anything else is jank on real hardware.

## Tokens, again

If a value in this file just decided something for you, write it down as a token in the design contract ([direction.md](direction.md)): the space scale, the elevation tiers, the z-index tiers, the focus ring style. A law applied once by hand and lost is a law the next session will break.
