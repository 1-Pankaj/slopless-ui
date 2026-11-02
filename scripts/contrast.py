#!/usr/bin/env python3
"""contrast.py: WCAG 2.x contrast ratios for color pairs.

Zero dependencies. Python 3.8+.

Usage:
    python3 contrast.py "#201B12" "#F6F1E5"              one pair: fg bg
    python3 contrast.py fg1 bg1 fg2 bg2 ...              several pairs, in order
    python3 contrast.py --pairs pairs.json               [["fg","bg"], ...]
    python3 contrast.py "#6D6455" "#F6F1E5" --suggest    show a nearest passing shade
    python3 contrast.py --min 3.0 "#C1502E" "#E7ECE9"    custom threshold (large text)

Exit code 0 when every pair reaches AA body text (4.5:1) or --min, else 1.
"""

import json
import sys

AA_BODY = 4.5
AA_LARGE = 3.0
AAA_BODY = 7.0


def parse_color(text):
    text = text.strip().strip("'\"")
    if text.startswith("#"):
        text = text[1:]
    if len(text) == 3:
        text = "".join(ch * 2 for ch in text)
    if len(text) != 6:
        raise ValueError("expected a hex color like #RRGGBB or #RGB, got {!r}".format(text))
    return tuple(int(text[i : i + 2], 16) for i in (0, 2, 4))


def channel_to_linear(value):
    value /= 255.0
    if value <= 0.04045:
        return value / 12.92
    return ((value + 0.055) / 1.055) ** 2.4


def relative_luminance(rgb):
    r, g, b = rgb
    return (
        0.2126 * channel_to_linear(r)
        + 0.7152 * channel_to_linear(g)
        + 0.0722 * channel_to_linear(b)
    )


def contrast_ratio(fg, bg):
    l1 = relative_luminance(fg)
    l2 = relative_luminance(bg)
    lighter, darker = max(l1, l2), min(l1, l2)
    return (lighter + 0.05) / (darker + 0.05)


def grade(ratio, minimum):
    if minimum <= AA_LARGE:
        return "pass" if ratio >= minimum else "fail"
    if ratio >= AAA_BODY:
        return "pass (AAA)"
    if ratio >= AA_BODY:
        return "pass"
    if ratio >= AA_LARGE:
        return "large text only"
    return "fail"


def rgb_to_hex(rgb):
    return "#{:02X}{:02X}{:02X}".format(*rgb)


def suggest_passing(fg, bg, minimum, step=8, max_steps=60):
    """Darken the foreground until it passes. If that fails, lighten it."""
    base = list(fg)
    for _ in range(max_steps):
        base = [max(0, value - step) for value in base]
        if contrast_ratio(tuple(base), bg) >= minimum:
            return rgb_to_hex(tuple(base))
    base = list(fg)
    for _ in range(max_steps):
        base = [min(255, value + step) for value in base]
        if contrast_ratio(tuple(base), bg) >= minimum:
            return rgb_to_hex(tuple(base))
    return None


def main(argv):
    args = argv[1:]
    minimum = AA_BODY
    suggest = False
    pairs_file = None
    values = []

    i = 0
    while i < len(args):
        arg = args[i]
        if arg == "--min":
            minimum = float(args[i + 1])
            i += 2
        elif arg == "--suggest":
            suggest = True
            i += 1
        elif arg == "--pairs":
            pairs_file = args[i + 1]
            i += 2
        elif arg in ("-h", "--help"):
            print(__doc__)
            return 0
        else:
            values.append(arg)
            i += 1

    if pairs_file:
        with open(pairs_file, "r", encoding="utf-8") as handle:
            values = [pair for group in json.load(handle) for pair in group]

    if len(values) < 2 or len(values) % 2 != 0:
        print("Give at least one foreground/background pair. See --help.")
        return 2

    failures = 0
    for index in range(0, len(values), 2):
        fg = parse_color(values[index])
        bg = parse_color(values[index + 1])
        ratio = contrast_ratio(fg, bg)
        verdict = grade(ratio, minimum)
        line = "{} on {}: {:.2f}:1  {}".format(
            values[index], values[index + 1], ratio, verdict
        )
        print(line)
        if ratio < minimum:
            failures += 1
            if suggest:
                candidate = suggest_passing(fg, bg, minimum)
                if candidate:
                    print("    suggested: {} (darkened to pass {:.1f}:1)".format(candidate, minimum))
                else:
                    print("    no nearby shade passes; choose a different hue or a darker background")

    total = len(values) // 2
    if failures:
        print("\n{} of {} pair(s) below {:.1f}:1. Fix before delivery.".format(failures, total, minimum))
        return 1
    print("\nAll {} pair(s) pass.".format(total))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
