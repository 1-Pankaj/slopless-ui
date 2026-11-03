# Verification

The finishing pass. Nothing is presented to the user until it has been checked by code and looked at with eyes. Open this at step 5, every time, including for small changes.

## The rule

Code that looks right in the editor often renders wrong: overflow, clipped text, weak contrast, a missing state. Checking is one pass. Shipping unchecked work costs the user a round trip, which costs more.

## Honesty labels

End every piece of UI work with exactly one of these labels, and never claim more. The report's last line is the label, verbatim:

- `verification: verified visually`: rendered in a real browser, screenshots inspected at desktop and phone widths.
- `verification: verified statically (no browser available)`: scripts run and code reviewed, but no browser was available.
- `verification: not verified: <reason>`: neither happened. Rare, and the reason is mandatory.

Never describe work as "pixel-perfect" or "fully tested". Say what you did.

## The pass, in order

### 1. Static audit (always, it is cheap)

```bash
python3 scripts/foldcheck.py <changed files and folders>
```

Fix every error. Review every warning and either fix it or note in one line why it is intentional. A clean run is permission to look, not proof of quality.

### 2. Contrast (every pair you introduced or changed)

```bash
python3 scripts/contrast.py "<foreground>" "<background>"
```

Body text needs 4.5:1 or better. Large text (24px and up, or 19px bold and up) and UI boundaries need 3:1. Muted text on tinted panels is the most common failure; measure it, do not eyeball it.

### 3. Render and screenshot

Use the browser tool the environment provides first: a built-in agent browser (several agent IDEs drive one), a headless CLI, or a dev server plus screenshots. `node scripts/finish.mjs ./index.html` is the fallback when the host has no browser tool and Playwright is installed.

finish.mjs screenshots at 1440px and 390px, collects console errors, page errors, and failed requests, and fails on horizontal overflow. Whatever tool you use, the two screenshots are required, and the phone shot gets checked for horizontal overflow by eye. The point is looking, not the tool.

Start the dev server if the project has one (`package.json` scripts), or serve static files (`python3 -m http.server`), or open the file directly.

### 4. Look

Work the following list against each screenshot. Note findings as **must**, **should**, or **nice**.

- **Squint test:** blur your eyes or view the screenshot thumbnail-sized. Focal point, reading order, and the primary action must survive. Gray soup means the hierarchy is broken; fix size, weight, and space before anything else.
- **First glance:** does the page say what it is and what to do, without reading everything?
- **Edges:** left edges aligned across sections, consistent gutters, nothing orphaned or crowding, no horizontal scroll at 390px.
- **Type:** hierarchy clear, nothing under 12px, line length 45 to 75 characters for reading text, long words and numbers wrap or truncate as intended.
- **Color:** accent used only where it matters, no state shown by color alone, text readable over every surface and image.
- **Controls:** exactly one loud button, hover and focus states exist, icons all render and match in weight.
- **Motion:** controls answer on press, transitions run on both the enter and leave path, one entrance moment, reveals fire once and never re-hide, nothing loops except real states and the named ambient, and the page was loaded once with reduced motion on with everything still readable.
- **Content:** real copy everywhere, sample data varied (long, short, zero, missing), no invented proof.
- **Console:** zero errors, zero failed requests, no font or icon load failures, no layout shift after fonts arrive.

### 5. States and keyboard (interactive work)

Trigger empty, loading, and error states if the app allows; mark any you could not trigger as unverified. Tab through the main flow: reachable order, visible focus, dialogs trap focus and close on Escape.

### 6. Fix, re-check, stop

Fix all **must** and **should** findings, re-capture only the views that changed, and stop when no **must** findings remain or after three fix passes, whichever comes first. Leave **nice** findings in the report instead of chasing them.

## The stranger test

Last, before the report: look at the final screenshot as a stranger would, for three seconds. Would they guess it was made by a machine? If yes, find the tell in [anti-slop.md](anti-slop.md), fix it, and re-check that view. This is the pass that protects the work; do not skip it.

## Reporting

Eight lines or fewer: what was built, the feeling from the brief, what the pass actually ran, what was fixed, what remains and why, what could not be checked. The last line is the verbatim label from the honesty labels above.
