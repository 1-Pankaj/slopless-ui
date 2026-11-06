# Kinetic Life, Shaders, and Sensory Immersion

Motion and atmosphere transform an interface from a static document into a living, memorable one. There is a real difference between **decorative noise** (arbitrary pulsing blobs, floating orbs, generic button glows) and **intentional sensory immersion** (kinetic typography, scroll-driven sequences, procedural shaders, generative audio, and physical micro-interactions). Aim for the calm, precise feel of well-made native apps, built from a small number of moments that feel like one system.

## Principles

1. **One system.** Define easing and duration tokens once and reuse them everywhere.
2. **One choreographed load.** Under about 1.2 seconds total. After that, motion answers the person's actions and scroll position.
3. **Motion explains.** It shows where something came from, where it went, or what changed.
4. **Cheap properties only.** Animate `transform`, `opacity`, `clip-path`, and `filter`. Layout properties cause jank.
5. **Interruptible.** A new action cancels or reverses the current motion smoothly. Nothing blocks input.
6. **Content survives without it.** Reduced motion, slow devices, and failed scripts must still show everything. Content is visible by default and only hidden once motion is known to be allowed.

```css
:root {
  --ease-out: cubic-bezier(0.22, 1, 0.36, 1);     /* fast start, long calm settle */
  --ease-in-out: cubic-bezier(0.65, 0, 0.35, 1);  /* movement across the screen */
  --ease-spring: linear(0, 0.4 8%, 0.9 18%, 1.08 28%, 1.12 34%, 1.04 48%, 0.99 62%, 1.005 78%, 1);
  --t-fast: 140ms;   /* press, toggle */
  --t-base: 280ms;   /* hover, small state change */
  --t-slow: 520ms;   /* panel, modal, expand */
  --t-scene: 900ms;  /* hero and scroll entrances */
}
```

Never use the browser defaults `ease` or `linear` for designed motion. `cubic-bezier(0.16, 1, 0.3, 1)` (snappy settle) and `cubic-bezier(0.2, 0.8, 0.2, 1)` (luxury editorial slide) are good alternatives.

---

## 1. The Spectrum of Motion & Atmosphere

| Tier | Application | Technique | Role in the Experience |
|---|---|---|---|
| **Living Canvas** | Backgrounds & environments | WebGL fragment shaders, procedural noise, raymarching, caustics | Creates an immersive world (e.g. dynamic ocean swell, atmospheric light, twilight to night) |
| **Generative Audio** | Ambient feedback & soundscapes | Web Audio API oscillators, filtered noise | Evokes tactile physical presence and spatial awareness |
| **Kinetic Typography** | Headlines & editorial indexes | Lateral hover slides, staggered reveals, split-word masks | Commands visual gravity and rewards exploration |
| **Stateful Transitions** | Stage reveals & environment switches | Circular clip-path reveals, view transitions | Communicates momentous shifts in state and mode |
| **Functional Feedback** | Buttons, form controls, cursors | Physical press, magnetic easing, `mix-blend-mode: difference` | Clarifies cause and effect with tactile snap |

Most products need the bottom three tiers. The top two are for subjects that earn them (see section 4).

---

## 2. Core Recipes

### Masked headline reveal on load

Each line rises from behind a mask. Content is visible by default and only hidden when motion is allowed.

```html
<h1 class="display">
  <span class="line"><span style="--i:0">Packs light.</span></span>
  <span class="line"><span style="--i:1">Carries heavy.</span></span>
</h1>
```

```css
.line { display: block; overflow: hidden; padding-bottom: 0.08em; }
.line > span { display: block; }

@media (prefers-reduced-motion: no-preference) {
  .line > span {
    transform: translateY(108%);
    animation: line-up var(--t-scene) var(--ease-out) forwards;
    animation-delay: calc(var(--i) * 90ms + 120ms);
  }
  @keyframes line-up { to { transform: none; } }
}
```

Follow with the supporting copy and the primary action at 60 to 90ms steps behind the headline. Everything else is already in place.

### Scroll-driven entrance with a safe fallback

```css
.panel { opacity: 1; }

@supports (animation-timeline: view()) {
  @media (prefers-reduced-motion: no-preference) {
    .panel {
      animation: panel-in linear both;
      animation-timeline: view();
      animation-range: entry 0% cover 30%;
    }
    @keyframes panel-in {
      from { opacity: 0; transform: translateY(6vh) scale(0.97); }
      to   { opacity: 1; transform: none; }
    }
  }
}
```

Vary the entrance by element: one panel slides, one clips open with `clip-path: inset()`, one scales. The same fade-up on every section is the tell.

### Pinned scroll sequence

A tall track with a sticky stage. Scroll progress drives the scene. The default state is the finished state, so content is fully visible if the script never runs.

```html
<section class="track">
  <div class="stage"><!-- the thing that assembles, draws, or changes --></div>
</section>
```

```css
.track { --p: 1; height: 300svh; position: relative; }
.stage { position: sticky; top: 0; height: 100svh; overflow: hidden; }
.track.is-live { --p: 0; }
.stage .piece { transform: translateY(calc((1 - var(--p)) * 40vh)); opacity: var(--p); }
```

```js
const track = document.querySelector('.track');
if (track && !matchMedia('(prefers-reduced-motion: reduce)').matches) {
  track.classList.add('is-live');
  let ticking = false;
  const update = () => {
    const r = track.getBoundingClientRect();
    const p = Math.min(1, Math.max(0, -r.top / (r.height - innerHeight)));
    track.style.setProperty('--p', p.toFixed(4));
    ticking = false;
  };
  addEventListener('scroll', () => { if (!ticking) { ticking = true; requestAnimationFrame(update); } }, { passive: true });
  update();
}
```

Keep native scroll. Do not hijack the wheel or add inertia libraries unless the user asks.

### Buttons that feel physical

```css
.btn {
  transition: transform var(--t-fast) var(--ease-out), box-shadow var(--t-base) var(--ease-out), background-color var(--t-base) var(--ease-out);
}
@media (hover: hover) { .btn:hover { transform: translateY(-2px); } }
.btn:active { transform: translateY(1px) scale(0.985); transition-duration: 60ms; }
.btn:focus-visible { outline: 3px solid var(--ink); outline-offset: 3px; }
```

Hover effects only under `(hover: hover)`, so touch devices do not get stuck states.

### Cursor-reactive hero

The loop only runs while the hero is on screen and the pointer is still settling.

```js
const hero = document.querySelector('.hero');
const fine = matchMedia('(pointer: fine)').matches;
const calm = matchMedia('(prefers-reduced-motion: reduce)').matches;
if (hero && fine && !calm) {
  let tx = 0, ty = 0, x = 0, y = 0, raf = 0, visible = false;
  const tick = () => {
    x += (tx - x) * 0.08; y += (ty - y) * 0.08;
    hero.style.setProperty('--mx', x.toFixed(3));
    hero.style.setProperty('--my', y.toFixed(3));
    const moving = Math.abs(tx - x) > 0.001 || Math.abs(ty - y) > 0.001;
    raf = (visible && moving) ? requestAnimationFrame(tick) : 0;
  };
  hero.addEventListener('pointermove', e => {
    const r = hero.getBoundingClientRect();
    tx = (e.clientX - r.left) / r.width - 0.5;
    ty = (e.clientY - r.top) / r.height - 0.5;
    if (!raf && visible) raf = requestAnimationFrame(tick);
  });
  new IntersectionObserver(([e]) => { visible = e.isIntersecting; }).observe(hero);
}
```

Use `--mx` and `--my` in `transform: translate3d(calc(var(--mx) * 24px), calc(var(--my) * 24px), 0)`, with different multipliers per layer for depth. Touch devices get a still, well-composed hero.

### State and page changes

```js
function go(update) {
  if (!document.startViewTransition) return update();
  document.startViewTransition(update);
}
```

Style `::view-transition-old(root)` and `::view-transition-new(root)` with the same tokens, and name shared elements with `view-transition-name` so a card can grow into a detail view.

---

## 3. Kinetic Typography & Lateral Hover Reveals

Reject static card links. For portfolios, showcases, and editorial archives, use horizontal index rows that slide laterally on hover:

```css
.index-row {
  display: grid;
  grid-template-columns: minmax(0, 1.2fr) minmax(0, 1fr) auto;
  gap: 1.5rem;
  align-items: baseline;
  padding: 1.6rem 0;
  border-top: 1px solid currentColor;
  transition: padding var(--t-slow) var(--ease-out), color var(--t-base) ease;
}
@media (hover: hover) {
  .index-row:hover { padding-left: 1.2rem; color: var(--accent); }
}
.index-row:focus-visible { padding-left: 1.2rem; }
```

- Give every row a keyboard focus state and a tap behavior, because hover does not exist on touch.
- **Staggered Character Reveals:** For major section titles, split text into words or spans and reveal them with staggered delays (`calc(var(--i) * 60ms)`), following the masked-reveal recipe above.

---

## 4. Living Canvas: Procedural WebGL & Shaders

Use a shader when the subject earns it: an immersive experience, a creative studio, entertainment, hospitality, an editorial showpiece. Do not add one to a dashboard, a form, documentation, or a checkout flow. Use at most one sensory layer on a typical marketing page.

When an interface needs an atmosphere that static CSS cannot achieve, mount a full-viewport canvas behind the content and drive it with a GLSL fragment shader:

1. **Procedural Surface Displacement:** Multi-octave fractional Brownian motion (fBm) generates waves, terrain, or clouds with no texture assets.
2. **Dynamic Lighting Models:** Tie shader uniforms to state. Recalculate sun and moon elevation when the user toggles Day/Night, and shift light attenuation as scroll depth increases.
3. **Bounded Cost:** Keep raymarching to a small, fixed step count (roughly 12 to 20), cap the device pixel ratio, render at reduced resolution on small screens, and pause when the tab or the canvas is not visible. Test on a real phone; do not assume a frame rate.
4. **Graceful Fallback:** Put a complete CSS background on `html` or `body` so the interface still looks finished if WebGL is unavailable, and serve a still frame to users who prefer reduced motion.

A minimal working skeleton to build from:

```html
<canvas id="gl" aria-hidden="true"></canvas>
```

```css
#gl { position: fixed; inset: 0; width: 100%; height: 100%; z-index: -1; }
```

```js
(function () {
  const canvas = document.getElementById('gl');
  const gl = canvas && canvas.getContext('webgl', { antialias: false, alpha: false });
  if (!gl) return;                                    // CSS background stays
  const calm = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const vs = 'attribute vec2 p; void main(){ gl_Position = vec4(p, 0., 1.); }';
  const fs = `precision mediump float;
    uniform vec2 uRes; uniform float uTime;
    float hash(vec2 p){ return fract(sin(dot(p, vec2(127.1, 311.7))) * 43758.5453); }
    float noise(vec2 p){ vec2 i = floor(p), f = fract(p); f = f*f*(3.-2.*f);
      return mix(mix(hash(i), hash(i+vec2(1,0)), f.x), mix(hash(i+vec2(0,1)), hash(i+vec2(1,1)), f.x), f.y); }
    float fbm(vec2 p){ float v = 0., a = .5; for (int i = 0; i < 5; i++){ v += a * noise(p); p *= 2.; a *= .5; } return v; }
    void main(){
      vec2 uv = gl_FragCoord.xy / uRes.xy;
      float n = fbm(uv * 3. + vec2(uTime * .03, uTime * .02));
      vec3 deep = vec3(.04, .12, .16), light = vec3(.95, .42, .27);
      gl_FragColor = vec4(mix(deep, light, smoothstep(.35, .85, n * (1. - uv.y * .6))), 1.);
    }`;
  const make = (type, src) => { const s = gl.createShader(type); gl.shaderSource(s, src); gl.compileShader(s); return s; };
  const prog = gl.createProgram();
  gl.attachShader(prog, make(gl.VERTEX_SHADER, vs));
  gl.attachShader(prog, make(gl.FRAGMENT_SHADER, fs));
  gl.linkProgram(prog);
  if (!gl.getProgramParameter(prog, gl.LINK_STATUS)) return;   // fall back to CSS
  gl.useProgram(prog);
  gl.bindBuffer(gl.ARRAY_BUFFER, gl.createBuffer());
  gl.bufferData(gl.ARRAY_BUFFER, new Float32Array([-1, -1, 3, -1, -1, 3]), gl.STATIC_DRAW);
  const loc = gl.getAttribLocation(prog, 'p');
  gl.enableVertexAttribArray(loc);
  gl.vertexAttribPointer(loc, 2, gl.FLOAT, false, 0, 0);
  const uRes = gl.getUniformLocation(prog, 'uRes'), uTime = gl.getUniformLocation(prog, 'uTime');
  const resize = () => {
    const scale = Math.min(devicePixelRatio || 1, 1.5) * (innerWidth < 700 ? 0.6 : 1);
    canvas.width = Math.max(1, Math.floor(innerWidth * scale));
    canvas.height = Math.max(1, Math.floor(innerHeight * scale));
    gl.viewport(0, 0, canvas.width, canvas.height);
  };
  addEventListener('resize', resize); resize();
  let raf = 0, t0 = performance.now();
  const frame = (now) => {
    gl.uniform2f(uRes, canvas.width, canvas.height);
    gl.uniform1f(uTime, calm ? 0 : (now - t0) / 1000);
    gl.drawArrays(gl.TRIANGLES, 0, 3);
    raf = calm ? 0 : requestAnimationFrame(frame);
  };
  document.addEventListener('visibilitychange', () => {
    if (document.hidden) { cancelAnimationFrame(raf); raf = 0; }
    else if (!raf && !calm) raf = requestAnimationFrame(frame);
  });
  raf = requestAnimationFrame(frame);
})();
```

Change the colors, the noise scale, and the motion to belong to the subject. Treat the sample as a starting point, never as the design.

---

## 5. Generative Web Audio API

Audio gives sensory weight that pixels cannot, but it is the easiest place to annoy people. Synthesize sound with the Web Audio API instead of shipping heavy files, and follow these rules:

- **Mute by default, create on gesture.** Browsers block audio until a user gesture. Build the `AudioContext` inside the click handler of an unmistakable sound toggle with a clear visual state, and call `resume()`.
- **Never autoplay**, and silence audio when the tab is hidden, when the toggle is off, and for users who prefer reduced motion unless they turn it on themselves.
- **Micro-interactions:** subtle sine clicks or short frequency sweeps on presses are acceptable once sound is on.

```html
<button class="sound-toggle" aria-pressed="false">Sound off</button>
```

```js
const toggle = document.querySelector('.sound-toggle');
let ctx, master;
function start() {
  ctx = new (window.AudioContext || window.webkitAudioContext)();
  const length = ctx.sampleRate * 2;
  const buffer = ctx.createBuffer(1, length, ctx.sampleRate);
  const data = buffer.getChannelData(0);
  for (let i = 0; i < length; i++) data[i] = Math.random() * 2 - 1;      // white noise
  const noise = ctx.createBufferSource();
  noise.buffer = buffer; noise.loop = true;
  const filter = ctx.createBiquadFilter();
  filter.type = 'lowpass'; filter.frequency.value = 280;                  // soft, distant wash
  master = ctx.createGain(); master.gain.value = 0;
  noise.connect(filter).connect(master).connect(ctx.destination);
  noise.start();
}
async function setSound(on) {
  if (!ctx) { if (!on) return; start(); }
  await ctx.resume();
  master.gain.setTargetAtTime(on ? 0.04 : 0, ctx.currentTime, 0.2);
  toggle.setAttribute('aria-pressed', String(on));
  toggle.textContent = on ? 'Sound on' : 'Sound off';
}
toggle.addEventListener('click', () => setSound(toggle.getAttribute('aria-pressed') !== 'true'));
document.addEventListener('visibilitychange', () => { if (document.hidden && ctx) setSound(false); });
```

---

## 6. Stateful Interactive Elements

### Circular clip-path preloader (JavaScript-created)

Reveal the stage with a geometric clip-path rather than an opacity fade. The preloader only exists when JavaScript runs and motion is allowed, so nothing is ever blocked, and it never waits more than about a second for fonts.

```css
.preloader {
  position: fixed; inset: 0; z-index: 100; background: var(--ink); pointer-events: none;
  clip-path: circle(150% at 50% 50%);
  transition: clip-path 1s var(--ease-in-out);
}
.preloader.out { clip-path: circle(0% at 50% 50%); }
```

```js
if (!matchMedia('(prefers-reduced-motion: reduce)').matches) {
  const pre = document.createElement('div');
  pre.className = 'preloader';
  document.body.prepend(pre);
  const reveal = () => requestAnimationFrame(() => {
    pre.classList.add('out');
    pre.addEventListener('transitionend', () => pre.remove(), { once: true });
    setTimeout(() => pre.remove(), 2000);
  });
  Promise.race([document.fonts.ready, new Promise(r => setTimeout(r, 900))]).then(reveal);
}
```

### Rotating conic focus border (`@property`)

A hardware-accelerated border for the focused field. The infinite animation is bound to a real state (focus), and reduced motion stops it.

```css
@property --angle { syntax: '<angle>'; initial-value: 0deg; inherits: false; }

.field { position: relative; isolation: isolate; }
.field::before {
  content: ""; position: absolute; inset: -2px; border-radius: inherit; z-index: -1; opacity: 0;
  background: conic-gradient(from var(--angle), transparent 0 50%, var(--accent) 75%, transparent 100%);
  transition: opacity var(--t-base) var(--ease-out);
}
.field:focus-within::before { opacity: 1; animation: spin-border 3s linear infinite; }
@keyframes spin-border { to { --angle: 360deg; } }
```

The pseudo-element extends 2px beyond the field, so keep fields inside a padded container or the page can gain a horizontal scrollbar. `foldcheck.py` reports this as `LOOP-INFINITE`. Because it is tied to focus, justify it in the handoff or run with `--allow-infinite`.

### Difference-blended magnetic cursor

```css
.cursor {
  position: fixed; top: 0; left: 0; width: 18px; height: 18px; margin: -9px 0 0 -9px;
  border: 1.5px solid #fff; border-radius: 50%;
  pointer-events: none; mix-blend-mode: difference; z-index: 9999; opacity: 0;
  transition: opacity var(--t-base) ease, width var(--t-base) var(--ease-out), height var(--t-base) var(--ease-out), margin var(--t-base) var(--ease-out), background-color var(--t-base) var(--ease-out);
}
.cursor.ready { opacity: 1; }
.cursor.active { width: 72px; height: 72px; margin: -36px 0 0 -36px; background: #fff; }
@media (pointer: coarse), (prefers-reduced-motion: reduce) { .cursor { display: none; } }
```

Move it with `transform: translate3d(x, y, 0)` from a `pointermove` handler, only when `(pointer: fine)` matches, add `.ready` on the first move so it never sits parked in a corner, and leave the native cursor visible so nothing is lost if the script fails.

---

## 7. Accessibility & The Reduced-Motion Contract

Audacious motion must never compromise accessibility. When a user requests reduced motion:

1. Bypass cinematic transitions and travel, parallax, and scroll-linked movement, using `transition-duration: 0.01ms !important; animation-duration: 0.01ms !important; animation-iteration-count: 1 !important`.
2. Keep all content visible immediately, without requiring scroll reveals or clip-path finishes.
3. Silence any ambient Web Audio synthesizer and serve a still shader frame.
4. Keep state feedback such as focus rings and color changes.

---

## 8. Review

Check motion while it plays, not only in the source. Watch the load sequence on a throttled CPU, tap and hold buttons, interrupt a transition halfway, confirm nothing flashes on first paint, and reload with reduced motion enabled. Verify on a real phone when a shader or audio layer is present, and report anything you could not test.
