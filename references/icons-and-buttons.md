# Icons, links, and actions

Use icons and control styles to clarify meaning and affordance, not to fill empty space.

## Actions

- Use a link for navigation and a button for an operation. Preserve native semantics and expected keyboard behavior.
- Make the label name the outcome: "Book a fitting" or "Download the guide", not "Submit", "Click here", or "Get started". Emphasize actions according to their role and consequence; a screen can have multiple important actions, but they should not all compete equally.
- Separate destructive or irreversible actions from safe actions and identify their consequence. Ask for confirmation only when it helps prevent a meaningful mistake.
- Provide visible focus and appropriate hover, pressed, disabled, loading, and error feedback for the controls and flow that actually support those states.
- Follow the applicable platform accessibility requirements and provide comfortable targets for the intended device. Do not confuse CSS pixels, device-independent pixels, and points.

## Icons

An icon is useful when it improves recognition, labels a compact category, or communicates state. It is redundant when it repeats a nearby word without helping scanning or interaction. Do not put a stock icon in a colored rounded square next to every feature, metric, or list item. Choose a consistent icon set and weight when the product uses icons, and match the stroke weight to the type. Prefer a small set of custom inline SVG glyphs drawn for the subject, or typographic marks (arrows, numerals, asterisks set in the display face), over a default library, or use no icons at all. Give icon-only controls an accessible name and make their purpose discoverable.

Emoji may be appropriate as content in a product whose tone supports it; do not assume it will behave like a consistent icon asset across platforms. Confirm that any image or icon renders and has the right accessible treatment (meaningful alternative text or hidden from assistive technology when decorative).

Review the interface at actual size and with keyboard focus. Remove only the decoration that does not help a user understand, navigate, or act.

## Physical feedback

Give a press the feel of a press. A short, designed response makes controls feel crafted:

```css
.btn { transition: transform 140ms cubic-bezier(0.22, 1, 0.36, 1); }
@media (hover: hover) { .btn:hover { transform: translateY(-2px); } }
.btn:active { transform: translateY(1px) scale(0.985); transition-duration: 60ms; }
```

Gate hover with `(hover: hover)` so touch devices do not keep a stuck hover state, keep `:focus-visible` clearly visible, and never make hover the only way to reach content or an action. More recipes are in [motion.md](motion.md).
