# Kinetic Life, Shaders, and Sensory Immersion

Motion and atmosphere transform an interface from a static document into a living, unforgettable digital experience. There is a profound distinction between **decorative noise** (arbitrary pulsing blobs, floating orbs, and generic button glows) and **intentional sensory immersion** (procedural WebGL shaders, kinetic typography, generative audio, and physics-driven micro-interactions).

---

## 1. The Spectrum of Motion & Atmosphere

| Tier | Application | Technique | Role in the Experience |
|---|---|---|---|
| **Living Canvas** | Backgrounds & environments | WebGL fragment shaders, procedural noise, raymarching, caustics | Creates an immersive world (e.g. dynamic ocean swell, atmospheric light, twilight to night) |
| **Generative Audio** | Ambient feedback & soundscapes | Web Audio API oscillators, procedural white noise filters | Evokes tactile physical presence and spatial awareness |
| **Kinetic Typography** | Headlines & editorial indexes | Lateral hover slides, staggered character reveals, split-word masks | Commands visual gravity and rewards user exploration |
| **Stateful Transitions** | Stage reveals & environment switches | Circular clip-path reveals, conic-gradient rotating borders | Communicates momentous shifts in state and mode |
| **Functional Feedback** | Buttons, form controls, cursors | Magnetic easing, mix-blend-mode difference, floating labels | Clarifies cause and effect with tactile snap |

---

## 2. Living Canvas: Procedural WebGL & Shaders

When an interface demands an atmosphere that static CSS cannot achieve, mount a full-viewport canvas (`<canvas id="gl"></canvas>`) behind the content and drive it with GLSL fragment shaders:

1. **Procedural Surface Displacement:** Use multi-octave Fractional Brownian Motion (fBm) and noise functions to generate real-time fluid waves, terrain, or celestial clouds without external texture assets.
2. **Dynamic Lighting Models:** Tie shader uniforms (`uniform float N, T, Y;`) to user state:
   - Recalculate sun/moon elevation vectors when the user toggles Day/Night mode.
   - Shift underwater light attenuation and caustic sharpness as scroll depth increases.
3. **Low-Overhead Raymarching:** Keep raymarching step counts bounded (12–20 iterations) with adaptive step sizing to ensure consistent 60fps rendering across desktop and mobile.
4. **Graceful Fallback:** Always provide a high-contrast CSS gradient (`background: linear-gradient(...)`) on `html` or `body` so the interface remains visually complete if WebGL is disabled or unsupported.

---

## 3. Generative Web Audio API

Audio provides sensory weight that pixels alone cannot convey. Avoid heavy audio assets; synthesize sound procedurally using the Web Audio API:

```javascript
// Procedural ambient ocean wave sound synthesis
const ctx = new (window.AudioContext || window.webkitAudioContext)();
const bufferSize = ctx.sampleRate * 2;
const buffer = ctx.createBuffer(1, bufferSize, ctx.sampleRate);
const data = buffer.getChannelData(0);
for (let i = 0; i < bufferSize; i++) {
  data[i] = Math.random() * 2 - 1; // White noise
}
const noise = ctx.createBufferSource();
noise.buffer = buffer;
noise.loop = true;

const filter = ctx.createBiquadFilter();
filter.type = 'lowpass';
filter.frequency.setValueAtTime(280, ctx.currentTime);

const gain = ctx.createGain();
gain.gain.setValueAtTime(0.04, ctx.currentTime);

noise.connect(filter).connect(gain).connect(ctx.destination);
```

- **Mute by Default:** Always initialize audio in an off state. Provide an unmistakable toggle button (`#sg`) with clear visual state.
- **Micro-Interactions:** Synthesize subtle sine wave clicks or frequency sweeps on button presses and navigation transitions.

---

## 4. Kinetic Typography & Lateral Hover Reveals

Reject static card links. For portfolios, showcases, and editorial archives, use horizontal index rows that slide laterally on hover:

```css
.pj > a {
  display: grid;
  grid-template-columns: minmax(0, 1.2fr) minmax(0, 1fr) auto;
  gap: 1.5rem;
  align-items: baseline;
  padding: 1.6rem 0;
  border-top: 1px solid var(--border);
  transition: padding 0.5s cubic-bezier(0.2, 0.8, 0.2, 1), color 0.3s ease;
}

.pj a:hover {
  padding-left: 1.2rem;
  color: var(--accent);
}
```

- **Custom Bezier Curves:** Never use browser defaults like `ease` or `linear`. Use expressive curves such as `cubic-bezier(0.16, 1, 0.3, 1)` (snappy spring overshoot) or `cubic-bezier(0.2, 0.8, 0.2, 1)` (luxury editorial slide).
- **Staggered Character Reveals:** For major section titles, split text into inline words or spans and reveal them with staggered delays (`calc(var(--i) * 60ms)`).

---

## 5. Stateful Interactive Elements

### Circular Clip-Path Preloaders (`#ld`)
Reveal the application stage using geometric clip-path transitions rather than standard opacity fades:
```css
#ld {
  position: fixed;
  inset: 0;
  z-index: 100;
  clip-path: circle(150% at 50% 50%);
  transition: clip-path 1.4s cubic-bezier(0.76, 0, 0.24, 1);
}
#ld.out {
  clip-path: circle(0% at 50% 50%);
}
```

### Rotating Conic Gradient Focus Borders (`@property --a`)
Use CSS Houdini properties to drive smooth, hardware-accelerated border glows on active form fields:
```css
@property --a {
  syntax: '<angle>';
  initial-value: 0deg;
  inherits: false;
}

.field:focus-within::before {
  content: "";
  position: absolute;
  inset: -1px;
  border-radius: inherit;
  background: conic-gradient(from var(--a), transparent 0% 50%, var(--accent) 75%, transparent 100%);
  animation: spin-glow 3s linear infinite;
  z-index: -1;
}

@keyframes spin-glow {
  to { --a: 360deg; }
}
```

### Difference-Blended Magnetic Cursors (`#cu`)
```css
#cu {
  position: fixed;
  width: 18px;
  height: 18px;
  border-radius: 50%;
  border: 1.5px solid #fff;
  pointer-events: none;
  mix-blend-mode: difference;
  transition: transform 0.1s ease, width 0.4s cubic-bezier(0.2, 0.8, 0.2, 1), height 0.4s cubic-bezier(0.2, 0.8, 0.2, 1);
  z-index: 9999;
}
#cu.active {
  width: 72px;
  height: 72px;
  background: #fff;
}
@media (pointer: coarse) {
  #cu { display: none; }
}
```

---

## 6. Accessibility & The Reduced-Motion Contract

Audacious creative motion must NEVER compromise accessibility. When a user requests reduced motion:
1. Immediately bypass all cinematic transitions (`transition-duration: 0.01s !important; animation: none !important;`).
2. Keep all content visible and accessible immediately without requiring scroll reveals or clip-path finishes.
3. Automatically silence any ambient Web Audio synthesizer.
