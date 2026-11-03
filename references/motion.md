# Motion with a job

Motion is optional. Use it when it communicates a state change, connects cause and effect, guides attention, or expresses an intentional brand moment. A static interface can be complete; adding motion to satisfy a quota creates noise.

## Decide before animating

For each non-trivial effect, be able to answer:

- What moves or changes?
- What event triggers it?
- What does the motion help the user understand or feel?
- Can the user interrupt or repeat the action?
- What happens with `prefers-reduced-motion` enabled?

Prefer brief feedback for direct actions and restrained transitions for changes of context. Keep the result understandable when motion is disabled, skipped, delayed, or interrupted. Avoid motion that blocks input or conveys liveness that is not real.

## Match motion to the interface

Interaction feedback such as pressed, selected, expanded, saved, or dismissed can help clarify an outcome. A page-load entrance, scroll reveal, ambient animation, ticker, or cursor effect needs a specific reason and should not compete with the task. Do not apply the same fade-and-rise treatment to every section or hover effect to every card by default.

Use CSS transitions or the project's existing motion system where they are sufficient. Favor properties and techniques appropriate to the effect and target devices; profile expensive animation rather than treating one implementation recipe as universal. Ensure hover enhancements also have keyboard and touch equivalents where they expose information or action.

For reduced motion, remove or simplify non-essential movement while preserving state, content, and feedback. Do not merely hide content that was revealed only by animation.

## Review

Check motion during the actual interaction, not just in a source file. Verify enter and exit behavior where both exist, interruption and repeated activation where relevant, and the reduced-motion state. If the interaction is not improved by motion, leave it still.
