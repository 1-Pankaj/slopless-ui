# Motion

Motion is half the craft of a modern interface. A page where nothing moves reads as a template: the layout was assembled, but nobody was present when it shipped. A page where everything moves reads as a demo reel. The target is between those: a page with a pulse. It answers when touched, it arrives with intention, and it holds still when asked.

Open this for any animation or transition work, and before you call a build finished: a motion pass is part of finishing, not a garnish.

The physics underneath is public knowledge, not invention. Apple's Designing Fluid Interfaces talk (WWDC 2018) put response, interruptibility, and spatial consistency on record; Material's motion guidance argues the same points from the other side. What follows translates those habits into CSS, a little JavaScript, and numbers you can defend in review.

## Contents

- [The purpose test](#the-purpose-test)
- [The motion budget](#the-motion-budget)
- [Respond before you animate](#respond-before-you-animate)
- [Tokens](#tokens)
- [The interaction table](#the-interaction-table)
- [Entrance choreography](#entrance-choreography)
- [Scroll choreography](#scroll-choreography)
- [Hover choreography](#hover-choreography)
- [The signature ambient](#the-signature-ambient)
- [Tickers and marquees](#tickers-and-marquees)
- [Pointer flourishes](#pointer-flourishes)
- [Springs and weight](#springs-and-weight)
- [Frames and performance](#frames-and-performance)
- [Canvas work](#canvas-work)
- [Enter and exit take the same path](#enter-and-exit-take-the-same-path)
- [Reduced motion](#reduced-motion)
- [Working snippets](#working-snippets)
- [Verification](#verification)

## The purpose test

Before adding motion, say in one sentence what it explains:

- "The panel grows from the button that opened it" explains cause and effect. Keep it.
- "The cards float because it looks alive" explains nothing. Remove it.

Motion that reports a real state (loading, saved, arriving) is information. Motion that decorates is noise. Generated interfaces are easy to recognize because they choose noise; great ones spend motion like money.

## The motion budget

Every page gets a motion pass, and the pass has four lines in it. Think of them as a budget that forces priorities:

1. **Answers.** Every control gives press feedback and a hover state. This is the minimum; a page missing it feels dead regardless of layout.
2. **One entrance.** The signature element arrives with intention (a masked line rise, a scale from the trigger). One, not one per section.
3. **Quiet reveals.** Sections and rows below the fold may fade-and-rise once, 20px, staggered. This is stagecraft, not decoration; it directs the eye down the page.
4. **One ambient.** At most one continuously living element, named in the brief as the signature (see [The signature ambient](#the-signature-ambient)). Marketing and Experience pages earn it. Dashboards and docs do not.

If a fifth request for motion arrives, it must displace an existing line or be refused. Interfaces that spend everywhere spend nothing.

## Respond before you animate

The feeling of directness comes from response speed, not from animation. Three rules that matter more than any curve:

- **Feedback lands on press, not release.** The control answers on `:active` or pointer-down: a 1px push, a slight scale, a pressed border. Waiting for the click event to show any reaction feels dead, even when the transition that follows is beautiful.
- **Nothing blocks input while it moves.** A user who clicks during a transition has said something. Never disable the interface while an animation finishes; redirect it or drop it.
- **Transitions start from the value on screen.** In CSS this is mostly free: a transition animates from wherever the element currently is. The failure mode is JavaScript that sets a start value first, which makes an interrupted transition jump. If you script motion, read the live transform before you animate.

## Tokens

Define durations and easings once, next to your color tokens:

```css
:root {
  --motion-fast: 140ms;  /* hover, focus, press, small state changes */
  --motion-base: 300ms;  /* enters, exits, panels, reveals */
  --motion-slow: 600ms;  /* the entrance, page-level moments, rare */
  --ease-out:   cubic-bezier(0.22, 1, 0.36, 1);   /* things arriving */
  --ease-in:    cubic-bezier(0.55, 0, 0.68, 0.19); /* things leaving */
  --ease-sheet: cubic-bezier(0.32, 0.72, 0, 1);    /* overlays, sheets, accordions */
}
```

Rules of thumb:

- Hover, focus, and press respond in 100 to 200ms. Slower feels broken; instant feels flickery.
- Entrances 300 to 500ms with a strong ease-out. The element decelerates into place, like something set down, not dropped.
- Exits are faster than entrances (150 to 250ms, ease-in). People are already looking at the next thing.
- Overshoot and bounce come from the gesture, not from the stylesheet. A card the user flicked may settle with one small bounce; a menu that faded in may not.

## The interaction table

| Interaction | Duration | Curve | Notes |
|---|---|---|---|
| Hover / focus ring | 100 to 160ms | ease-out | One property; the leave path uses the same duration |
| Press (`:active`) | instant to 100ms | none or ease-out | The response is the state, not a transition |
| Link underline draw | 200 to 300ms | ease-out | scaleX from the left origin |
| Tooltip / popover | 160ms in, 120ms out | ease-out | Anchored to its trigger |
| Panel / drawer enter | 280 to 360ms | sheet curve | Exits along the same path, faster |
| Dialog | 200 to 280ms | sheet curve | Scrim fades, surface scales from 0.98, transform-origin at the trigger |
| Accordion / disclosure | 240 to 340ms | sheet curve | Animate `grid-template-rows` from 0fr to 1fr; no height math |
| Scroll reveal | 500 to 700ms | ease-out | 20 to 24px rise, once, staggered |
| Count-up | 900 to 1200ms | ease-out cubic | Once, on arrival; tabular numerals |
| Ticker | 30 to 45s per loop | linear | The one legal infinite loop besides loading states |
| Page-level entrance | at most one, 600 to 800ms | ease-out | The signature moment only |

## Entrance choreography

The first 800 milliseconds decide whether the page feels built or assembled. One entrance moment, above the fold, choreographed:

- **Pick the hero moment.** A display headline rising out of a mask, line by line, is the modern default and it works because it mimics speech: one line at a time. Stagger lines 80 to 140ms apart, total under 800ms.
- **Mask the lines.** Wrap each line in `overflow: hidden` and translate the inner span from 112% to 0. Nothing moves outside its line box, so the rhythm stays crisp.
- **Fade the supporting cast.** Eyebrow, lede, actions, and meta fade in behind the type with small delays. They support; they do not perform.
- **Everything else is simply there.** Content below the fold does not need an entrance ceremony. Sections use the quiet reveal below, once, and the page settles.
- **Cap the cast.** If more than three things animate in the first second, cut back to the headline and one supporting fade. Entrances lose meaning in crowds.

## Scroll choreography

Scrolling is the reader's gesture; motion should follow it, never fight it.

- **Reveal once, quietly.** An IntersectionObserver adds a class; the element transitions from opacity 0 and a 22px rise to rest. Fire at 10 to 20 percent visibility, unobserve after firing, and stagger siblings 60 to 90ms. Cap the stagger at the first 6 to 8 items; after that everything is simply present.
- **Parallax, if any, is a spice.** Background layers may drift a few percent against the scroll. If a parallax layer would take more code than the content it decorates, delete the layer.
- **Count-ups run once.** Numbers that matter (latency, totals, prices) count up on arrival over about a second with an ease-out, in tabular numerals so nothing reflows. Under reduced motion they render their final value immediately.
- **Progress bars and meters fill on arrival** from 0 to their value with a 900ms ease-out. This is a state change being reported, not decoration.
- **Sticky and pinned scenes** need an exit plan. If a section pins, the next one must be visibly waiting; a pin with no payoff is a trap.

## Hover choreography

Hover is a conversation, and it should be as short as possible:

- **One property, one direction.** A border brightens, an arrow nudges 5px, a row shifts 8px. Hover states that scale, bloom shadows, and rotate three things at once read as nervous.
- **Underlines draw, they do not blink.** For text links, a scaleX underline from the left origin at 200 to 300ms is the cleanest signal there is.
- **Rows gain a companion.** Work lists and menus may reveal an arrow, an index color, or a floating preview. The preview follows the cursor with a lerp (see [Pointer flourishes](#pointer-flourishes)); the row itself still changes one property.
- **Touch gets the truth.** Under `(hover: none)` hover states do not exist; make sure nothing important is reachable only by hover. Where a hover reveals content, offer a tap path.

## The signature ambient

At most one element on the page lives continuously, and it must earn the loop:

- **Name it in the brief.** "Signature: the live waveform in the hero" or "Signature: the room breathes behind the title." If the brief cannot name it, there is no ambient.
- **Tie it to the subject.** An audio API gets a waveform. A festival gets a slow field of light. A fintech gets nothing. The ambient demonstrates the product's material; it does not exist to prove the page has JavaScript.
- **Make it respond.** An ambient that answers the cursor (frequency follows the pointer, lights lean toward it) turns a spectator into a participant. This one feature separates crafted from pasted.
- **Keep it slow and dim.** Two or three percent of the page's contrast budget. Fast or bright ambient motion is the fastest way to exhaust a reader.
- **It holds still when asked.** Pauses when offscreen (IntersectionObserver) and when the tab is hidden (`visibilitychange`), renders one static frame under reduced motion, and pauses on hover where pausing makes sense.

## Tickers and marquees

The ticker is the one legal infinite loop besides loading states, because it carries content (client names, capabilities, dates) instead of decorating emptiness:

- Real content only: names, dates, categories. A ticker of adjectives is a banner ad.
- 30 to 45 seconds per loop, linear, duplicated track translating to exactly -50 percent so the seam is invisible.
- Pause on hover (`animation-play-state: paused`), collapse to a wrapped static list under reduced motion.
- One per page. Two tickers shouting in different directions is a times square, and not in the good way.

## Pointer flourishes

Desktop pointer work is where pages feel handmade. All of it is gated behind `(pointer: fine)` and disabled under reduced motion:

- **Magnetic buttons:** the primary action eases up to 6px toward the cursor with a per-frame lerp of about 0.16, and settles home on leave. The whole travel is small; it should feel like magnetism, not dragging.
- **Cursor companions:** a small dot or ring trails the cursor with `mix-blend-mode: difference`. It never replaces the native cursor, it grows on interactive targets, and it disappears on touch.
- **Hover-following previews:** over an index of work, a fixed-position card lerps toward the cursor with a slight rotation derived from its own velocity. Lerp at 0.12 to 0.16 per frame; snap rotation, never accumulate it.
- **Everything lerps home.** Every flourish returns to rest on pointerleave. A flourish that sticks is a bug wearing a bowtie.

## Springs and weight

When your framework offers springs (Motion, React Spring, SwiftUI-adjacent libraries), two parameters replace duration entirely:

- **Damping ratio** near 1.0 is the default: no overshoot, a clean settle. Drop to about 0.8 only when the gesture itself carried momentum (a flick, a throw, a drag release). Bounce on a menu that merely faded in reads as a toy.
- **Response** 0.3 to 0.4s covers most UI: how quickly the value reaches its target. Snappier for small controls, slower for large surfaces.
- **Interrupt first, always.** Springs re-target from the current on-screen value, which is why gesture-driven UI uses them instead of fixed-duration tweens. If a user can grab it, it is a spring; if they cannot, a transition is fine.

In plain CSS there are no springs; the sheet curve and a strong ease-out carry the same intent. Do not reach for a spring library to animate a hover.

## Frames and performance

Smoothness is what is in the frames:

- **Animate `transform` and `opacity` only.** Width, height, top, and left force layout on every frame. The one sanctioned exception is `grid-template-rows: 0fr to 1fr` for accordions, which browsers handle on the compositor.
- **`will-change` is a promise, not a perfume.** Set it on elements about to move, and drop it when they stop. A page where everything is `will-change: transform` helps nothing.
- **Respect the frame budget.** Anything per-frame (canvas, lerp loops, followers) runs in one `requestAnimationFrame` per element, reads layout once per frame, and stops when its work is done.
- **Cap devicePixelRatio at 2** for canvas work. Rendering at 3x DPR doubles the pixels for no visible gain on most screens.
- **Test on a real phone** before calling a scroll-driven page done. If a section stutters on a mid-range device, it ships without that section's motion.

## Canvas work

A canvas is the strongest tool for a signature ambient, and it has house rules:

- Size to the element times a capped DPR, and re-size on `resize` (or a ResizeObserver).
- Draw only while visible: an IntersectionObserver flips a flag; the loop checks it plus `document.hidden` before scheduling the next frame.
- One clear per frame, gradients built once per frame from cheap primitives. If the scene needs more than about a hundred draw calls per frame, pre-render layers offscreen and composite them.
- Under reduced motion: draw one representative frame and stop. The material stays; the clock stops.
- Give the canvas a `role="img"` and an `aria-label` that describes what it shows, and keep the page meaningful with JavaScript disabled.

## Enter and exit take the same path

Spatial consistency is what makes an interface feel like a place instead of a stack of slides:

- **A panel leaves the way it arrived.** Something that slid in from the right dismisses to the right. In from the right, out through the bottom reads as disconnected.
- **An overlay grows from its trigger.** Set `transform-origin` to the button or menu item that opened it, so the relationship between cause and effect is visible. A popover scaling from its own center is the generic version.
- **Mirror the curve on the way back.** A transition that decelerates in should accelerate out. The sheet and ease tokens pair up for this; use them as a pair.

## Reduced motion

Reduced motion does not mean no feedback. It means the travel goes, the meaning stays:

```css
@media (prefers-reduced-motion: reduce) {
  html { scroll-behavior: auto; }
  .js .mask > span, .js .fade-in { animation: none; transform: none; opacity: 1; }
  .js [data-reveal] { transition: none; opacity: 1; transform: none; }
  .ticker-track { animation: none; }
  .ticker-seq { flex-wrap: wrap; white-space: normal; }
}
```

- Revealed content must be visible without JavaScript and without motion: scope the hidden state behind a `js` class on the root element, and let the reduced-motion query force everything visible.
- For elements whose arrival carries meaning (a toast, a drawer), keep a short opacity cross-fade instead of the blanket kill, so the state change stays visible without moving anything.
- An accordion still opens, a tab still switches, a ticker still lists. Only the travel is removed.
- Load the page once with the setting on before you call the work done. This check catches more than any other single pass.

## Working snippets

The masked line rise, the modern entrance:

```css
.js .mask { display: block; overflow: hidden; }
.js .mask > span {
  display: block; transform: translateY(112%);
  animation: rise 760ms var(--ease-out) forwards;
  animation-delay: var(--d, 0ms);
}
@keyframes rise { to { transform: translateY(0); } }
```

The quiet reveal, staggered by a custom property:

```css
.js [data-reveal] {
  opacity: 0; transform: translateY(22px);
  transition: opacity 640ms var(--ease-out), transform 640ms var(--ease-out);
  transition-delay: var(--d, 0ms);
}
.js [data-reveal].in { opacity: 1; transform: none; }
```

```js
var io = new IntersectionObserver(function (entries) {
  entries.forEach(function (entry) {
    if (entry.isIntersecting) {
      entry.target.classList.add("in");
      io.unobserve(entry.target);
    }
  });
}, { threshold: 0.15, rootMargin: "0px 0px -6% 0px" });
document.querySelectorAll("[data-reveal]").forEach(function (el) { io.observe(el); });
```

Press feedback that costs one line:

```css
.btn:active { transform: translateY(1px) scale(0.99); transition-duration: 60ms; }
```

An accordion that animates without height math:

```css
.acc-body { display: grid; grid-template-rows: 0fr; transition: grid-template-rows 340ms var(--ease-sheet); }
.acc-item[data-open="true"] .acc-body { grid-template-rows: 1fr; }
.acc-body > * { overflow: hidden; }
```

A ticker with an invisible seam (two identical sequences, track translates -50%):

```css
.ticker-track { display: flex; width: max-content; animation: ticker-scroll 36s linear infinite; }
.ticker:hover .ticker-track { animation-play-state: paused; }
@keyframes ticker-scroll { to { transform: translateX(-50%); } }
```

A magnetic button with no library:

```js
el.addEventListener("pointermove", function (e) {
  var r = el.getBoundingClientRect();
  tx = (e.clientX - r.left - r.width / 2) * 0.14;
  ty = (e.clientY - r.top - r.height / 2) * 0.3;
  if (!raf) raf = requestAnimationFrame(step);   // step lerps x,y toward tx,ty at 0.16
});
el.addEventListener("pointerleave", function () { tx = 0; ty = 0; if (!raf) raf = requestAnimationFrame(step); });
```

A popover anchored to its trigger, symmetric on the way out:

```css
.popover {
  transform-origin: top left;            /* the corner of the button that opened it */
  transition: opacity var(--motion-fast) ease-out,
              transform var(--motion-fast) ease-out;
}
.popover[open] { opacity: 1; transform: scale(1); }
.popover:not([open]) { opacity: 0; transform: scale(0.96); }
```

## Verification

Motion is checked in the finishing pass, not by imagining it:

- Every control answers on press and has a hover state; both run on the enter and the leave path.
- Exactly one entrance moment, above the fold; reveals fire once and never re-hide.
- Nothing loops except a loading state, and the one named signature ambient; the ambient pauses offscreen, on hidden tabs, and under reduced motion.
- Count-ups and meter fills run once and land on their real values.
- Pointer flourishes are gated behind `(pointer: fine)`, return home on leave, and do not exist on touch.
- The reduced-motion view was actually loaded once with the setting on, and everything was reachable and readable in it.
