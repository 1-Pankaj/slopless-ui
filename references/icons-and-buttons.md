# Icons, links, and actions

Use icons and control styles to clarify meaning and affordance, not to fill empty space.

## Actions

- Use a link for navigation and a button for an operation. Preserve native semantics and expected keyboard behavior.
- Make the label name the outcome. Emphasize actions according to their role and consequence; a screen can have multiple important actions, but they should not all compete equally.
- Separate destructive or irreversible actions from safe actions and identify their consequence. Ask for confirmation only when it helps prevent a meaningful mistake.
- Provide visible focus and appropriate hover, pressed, disabled, loading, and error feedback for the controls and flow that actually support those states.
- Follow the applicable platform accessibility requirements and provide comfortable targets for the intended device. Do not confuse CSS pixels, device-independent pixels, and points.

## Icons

An icon is useful when it improves recognition, labels a compact category, or communicates state. It is redundant when it repeats a nearby word without helping scanning or interaction. Choose a consistent icon set and weight when the product uses icons. Give icon-only controls an accessible name and make their purpose discoverable.

Emoji may be appropriate as content in a product whose tone supports it; do not assume it will behave like a consistent icon asset across platforms. Confirm that any image or icon renders and has the right accessible treatment (meaningful alternative text or hidden from assistive technology when decorative).

Review the interface at actual size and with keyboard focus. Remove only the decoration that does not help a user understand, navigate, or act.
