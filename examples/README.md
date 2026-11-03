# Illustrative examples

These three pairs show possible implementations for fictional products. The “before” files are intentionally constructed specimens and the “after” files are authored examples. They are not controlled model runs, representative samples, or evidence that the skill alone caused a measurable improvement.

| Pair | Product | Example direction |
|---|---|---|
| [oscilla](oscilla/) | Fictional realtime audio API | Product demo, measurements, and quickstart |
| [outerform](outerform/) | Fictional product studio | Work index and studio identity |
| [nocturne](nocturne/) | Fictional music festival | Event schedule and ticket actions |

The pages identify the businesses as fictional. Before pages include intentionally fabricated claims as negative examples; do not treat them as real proof. Finished pages use fictional content for demonstration and should be read in that context.

## What to compare

Look at how the examples change the relationship between content and layout, the relevance of product details, the honesty of claims, and the behavior of visible controls. Do not use a choice of font, gradient, centering, or motion as a pass/fail rule. Those choices only matter in relation to the brief and product.

The examples were created to illustrate a particular design thesis. Other products could reasonably use different palettes, component patterns, typefaces, or motion. The examples are not a substitute for inspecting a real project's design system.

## Inspect the files

The finished HTML files can be opened directly or served from the repository. `docs/` contains screenshots captured for these examples. They are useful for seeing the pages, but should not be taken as evidence about user task success or accessibility conformance.

Optional checks:

```bash
python3 scripts/foldcheck.py examples/oscilla/index.html
python3 scripts/contrast.py "#EEF3E3" "#0B0D0A"
node scripts/finish.mjs examples/oscilla/index.html
```

The scanner emits contextual cues and implementation findings; inspect them in place. The browser check requires Playwright. See [the verification guidance](../references/verification.md) for what these checks do and do not establish.
