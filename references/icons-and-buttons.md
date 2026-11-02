# Icons and buttons

Actions and their decoration. Generated interfaces pile up both: an icon on every heading and a button on every action. The discipline here is small and it changes how finished a screen feels. Open this when adding or reviewing any control.

## Buttons are commitments

A button says "this changes something". Treat each one as a decision someone has to defend:

- **One filled (primary) button per view.** This is normal, not minimal. If two elements look equally important, neither is.
- **Secondary actions are quieter:** an outlined button, or a plain text link. Navigation is always a link, never a button dressed as one.
- **Repeated row actions are text links** or labeled icon buttons, not a strip of buttons per row.
- **Destructive actions never wear the primary style.** They sit apart from the safe action and are confirmed by name ("Delete 3 invoices").
- **Three or more buttons side by side is a redesign signal.** Rank the actions and demote all but one.
- **Every interactive control has hover, focus-visible, active, and disabled styles.** Disabled controls say why nearby, or do not render. Touch targets are at least 44 by 44 pixels.
- **Buttons use verbs and name the object** (see [copy.md](copy.md)).

Quick ranking table:

| Situation | Control |
|---|---|
| The one main action of the view | Filled button |
| Real but secondary action | Outlined button or text link |
| Repeated list/row action | Text link, or icon button with a label |
| Navigation | Link |
| Destructive action | Text or outlined button, placed apart, confirmed |

## Icons are furniture

Most screens need fewer icons than an agent wants to add. Words are clearer, and a screen with no icons is a legitimate, often superior choice.

An icon earns its place when it does at least one of these: marks an action the muscle memory already knows (save, close, copy), signals a state, or labels a category in a dense tool. Headings, feature blurbs, marketing sections, and empty states almost never need icons.

Rules:

1. **One set per project.** Mixing icon families is instantly visible and reads as broken. Pick one library or draw inline SVGs, and record the choice in the design contract.
2. **One stroke weight, one corner style, one size grid** (16, 20, 24px). An icon that is thinner or rounder than its neighbors looks damaged.
3. **Icon-only controls need an accessible name** (`aria-label`) and, unless the symbol is universal, a visible label or tooltip. Unlabeled icon rows are unlearnable.
4. **Never ship an icon you have not seen render.** A missing glyph box is worse than no icon. In the finishing pass, every icon gets looked at.
5. **Never use emoji as icons.** Emoji are content, not chrome; they render differently on every platform and they cannot hold a consistent weight or size.
6. **Brand marks are not yours to improvise.** Use the official mark for a brand, or use the brand's name as text.
7. **Icon libraries are not the slop.** The slop is the default habit: an icon tile above every card heading, a bolt on every feature, a sparkle on everything new. If a region contains more than three decorative icons, remove the decorations and keep at most the functional ones.

## The squint check for controls

Squint at the view. Exactly one control should appear loudest. If two compete, demote one. If none does, the view has no primary action and the layout does not know what it is for.
