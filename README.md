<div align="center">

<img src="docs/squeegee-icon.jpg" alt="slopless-ui icon" width="128" style="border-radius: 16px;">

# slopless-ui

**A product-first design and implementation skill for AI agents.**

It helps an agent understand the interface's purpose, choose structure from the user's task, implement real content and behavior, and inspect relevant results. It does not replace one visual trend with another or ban familiar design choices.

[![CI](https://github.com/1-pankaj/slopless-ui/actions/workflows/ci.yml/badge.svg)](https://github.com/1-pankaj/slopless-ui/actions/workflows/ci.yml)
[![license](https://img.shields.io/badge/license-MIT-8E3B2F)](LICENSE)
[![agent skills](https://img.shields.io/badge/agent%20skills-compatible-201B12)](https://agentskills.io)
[![GitHub stars](https://img.shields.io/github/stars/1-pankaj/slopless-ui?style=flat&color=8E3B2F)](https://github.com/1-pankaj/slopless-ui/stargazers)

<br>
<img src="docs/banner.png" alt="slopless-ui banner" width="100%" style="border-radius: 8px;">

</div>

---

## The problem it targets

Generated interfaces can look polished while still feeling interchangeable: generic information architecture, repeated components without a content reason, unsupported metrics, weak interaction states, or a desktop-first layout that was never inspected. The underlying issue is missing product-specific decisions, not a particular font, palette, card, gradient, shadow, or animation.

Slopless UI scales to the request. A focused fix stays focused. A new page starts from the audience, task, content, and product context. A substantial redesign gets a concise design contract and a relevant browser and interaction review. The skill reports what it actually checked and what remains unknown.

## How it works

1. Inspect the existing product, design tokens, content, assets, behavior, and tests where available.
2. Establish the audience, task, domain information, real actions, content provenance, constraints, and success condition.
3. Choose hierarchy, composition, components, typography, color, assets, and motion based on that evidence.
4. Implement the functionality and states that belong to the requested scope. Do not invent production claims.
5. Verify runtime, interaction, responsive behavior, accessibility, and visual fit as separate concerns. Use the checks that matter for the task and environment.

Cards, gradients, rounded corners, dark mode, all-caps labels, familiar fonts, motion, and minimalism are allowed when they serve the product. Repetition without a reason is a prompt to review, not an automatic failure.

## Install

```bash
npx skills add 1-pankaj/slopless-ui
```

Or copy the skill folder into an agent's skill directory. Antigravity supports workspace skills under `.agents/skills/`; Claude Code, Codex, Gemini CLI, and other compatible tools have their own discovery locations and conventions. Consult the host's current documentation and reload the agent after installation when required.

## Use it

Let a compatible agent discover the skill, or invoke it deliberately:

> Build a landing page for my developer tool. Use slopless-ui.

> This dashboard feels generic. Review the product context and improve the information hierarchy without changing the established brand.

> Fix the mobile layout of the checkout form and verify the relevant flow.

## Bundled tools

The optional scripts provide focused checks:

```bash
python3 scripts/foldcheck.py src/                 # heuristic review cues
python3 scripts/contrast.py "#201B12" "#F6F1E5"  # contrast calculation
node scripts/finish.mjs ./index.html              # screenshots and browser diagnostics with Playwright
```

`foldcheck.py` flags a subset of recurring patterns. Most visual findings are informational or warnings, not style bans. An error points to a likely implementation/content issue such as placeholder copy or missing image alternative text. Findings can still be false positives; inspect the source and rendered result. A clean output is not a quality score.

`contrast.py` calculates color ratios for the supplied pairs. The calculation is useful, but the applicable standard, context, and exceptions still matter.

`finish.mjs` is an optional Playwright-based check. A browser supplied by the host may be more appropriate. Screenshots and overflow checks help review a page but do not replace interaction, accessibility, or human visual assessment.

## Examples

The repository includes three illustrative before/after pairs: [oscilla](examples/oscilla/), [outerform](examples/outerform/), and [nocturne](examples/nocturne/). They show design directions, not a controlled study proving that the skill improves outcomes. The “before” files are deliberately constructed examples, not a representative sample of unguided model output. See [examples/README.md](examples/README.md) for the choices shown.

![Before and after example](docs/before-after.png)

## Tests

Run the repository suite with:

```bash
bash tests/run_tests.sh
```

The suite checks script behavior, example fixtures, contrast-table calculations, and selected implementation invariants. Passing it confirms those checks only; it does not establish visual quality, usability, accessibility conformance, or performance. See [references/evaluation.md](references/evaluation.md) for a controlled way to evaluate whether the skill itself improves results.

## Reference map

- [Product understanding and design direction](references/direction.md)
- [Information and component foundations](references/foundations.md)
- [Responsive and accessibility checks](references/responsive-design.md)
- [Verification and critique](references/verification.md)
- [Generic-interface review cues](references/anti-slop.md)
- [Typography](references/typography.md), [color](references/color.md), [motion](references/motion.md), [copy](references/copy.md), and [icons/actions](references/icons-and-buttons.md)
- [Evaluating changes to the skill](references/evaluation.md)

## Honest scope

An instruction file can shape decisions, but it cannot guarantee that every agent discovers or follows the skill, that a browser is available, or that a reviewer will prefer the result. The code-level checker is heuristic. The examples are illustrative. Measuring effectiveness requires controlled tasks, independent review, functional checks, and repeated runs.

## License

[MIT](LICENSE) (c) 2026 Pankaj Israni. Font pairings in the optional typography reference are suggestions; verify the chosen font's current license and loading requirements before use.

## Author

Built by [Pankaj Israni](https://github.com/1-pankaj).
