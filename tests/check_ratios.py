#!/usr/bin/env python3
"""check_ratios.py: re-compute every contrast ratio documented in
references/color.md from the palette tables, and compare with the numbers
claimed in the text. A doc number that drifts from reality fails the suite.

Zero dependencies. Python 3.8+. Run from the repository root:
    python3 tests/check_ratios.py
"""

import os
import re
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))
from contrast import contrast_ratio, parse_color  # noqa: E402

DOCS = os.path.join(os.path.dirname(__file__), "..", "references", "color.md")
TOLERANCE = 0.06  # the docs round to one decimal

SECTION = re.compile(r"^### (\d+)\. (.+)$", re.MULTILINE)
ROLE_ROW = re.compile(r"^\| (Background|Surface|Ink|Muted ink|Accent ink|Accent) \| `#([0-9A-Fa-f]{6})` \|", re.MULTILINE)
CLAIMED = re.compile(
    r"Ink on background:\s*([\d.]+):1\.\s*Muted on background:\s*([\d.]+):1\.\s*"
    r"Accent on background:\s*([\d.]+):1\.\s*Accent ink on accent:\s*([\d.]+):1"
)


def main():
    with open(os.path.abspath(DOCS), "r", encoding="utf-8") as handle:
        text = handle.read()

    sections = []
    matches = list(SECTION.finditer(text))
    for i, match in enumerate(matches):
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        sections.append((match.group(1), match.group(2), text[match.start():end]))

    if not sections:
        print("No palette sections found in color.md. Check the parser.")
        return 2

    failures = 0
    checked = 0
    for number, name, body in sections:
        roles = {}
        for role, hex_value in ROLE_ROW.findall(body):
            roles[role] = "#" + hex_value
        claimed = CLAIMED.search(body)
        missing = [r for r in ("Background", "Surface", "Ink", "Muted ink", "Accent", "Accent ink") if r not in roles]
        if missing or not claimed:
            print("{:>2}. {:<11} SKIP (missing {} in section)".format(
                number, name, "roles: " + ", ".join(missing) if missing else "ratios line"))
            continue

        pairs = [
            ("Ink on background", roles["Ink"], roles["Background"], claimed.group(1)),
            ("Muted on background", roles["Muted ink"], roles["Background"], claimed.group(2)),
            ("Accent on background", roles["Accent"], roles["Background"], claimed.group(3)),
            ("Accent ink on accent", roles["Accent ink"], roles["Accent"], claimed.group(4)),
        ]
        bad = []
        for label, fg, bg, claimed_text in pairs:
            actual = contrast_ratio(parse_color(fg), parse_color(bg))
            checked += 1
            if abs(actual - float(claimed_text)) > TOLERANCE:
                bad.append("{}: doc says {}:1, script computes {:.2f}:1".format(label, claimed_text, actual))
        if bad:
            failures += 1
            print("{:>2}. {:<11} FAIL".format(number, name))
            for line in bad:
                print("        " + line)
        else:
            print("{:>2}. {:<11} ok".format(number, name))

    print()
    if failures:
        print("{} palette section(s) disagree with the script. Fix the docs (never estimate).".format(failures))
        return 1
    print("All documented ratios match the script ({} pairs across {} palettes).".format(checked, len(sections)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
