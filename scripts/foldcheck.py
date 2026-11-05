#!/usr/bin/env python3
"""foldcheck.py: static review cues for recurring interface patterns.

Zero dependencies. Python 3.8+. Scans source files for the patterns listed in
references/anti-slop.md: blinking and looping decoration, default gradient
heroes, glow and cyberpunk styling, emoji as icons, icon and button spam,
placeholder content, hotlinked stock images, em dashes, and more.

Usage:
    python3 foldcheck.py src/ components/ index.html
    python3 foldcheck.py --rules          list every rule
    python3 foldcheck.py --strict src/    warnings also fail
    python3 foldcheck.py --format json src/
    python3 foldcheck.py --allow-infinite src/   do not flag infinite animations

Patterns are contextual cues, not style bans or authorship signals. Exit code 1
is reserved for likely implementation/content defects, not visual preferences.
"""

import argparse
import colorsys
import json
import os
import re
import sys

SKIP_DIRS = {
    "node_modules", ".git", "dist", "build", "coverage", ".next", ".nuxt",
    ".cache", "venv", ".venv", "__pycache__", ".svelte-kit", "vendor",
}

CODE_EXT = {".html", ".htm", ".css", ".scss", ".sass", ".less", ".js", ".jsx",
            ".ts", ".tsx", ".mjs", ".cjs", ".vue", ".svelte", ".astro",
            ".md", ".mdx", ".txt"}
CSS_EXT = {".css", ".scss", ".sass", ".less", ".vue", ".svelte", ".astro"}
JS_EXT = {".js", ".jsx", ".ts", ".tsx", ".mjs", ".cjs"}
MARKUP_EXT = {".html", ".htm", ".vue", ".svelte", ".astro"}
IMG_EXT = JS_EXT | MARKUP_EXT

MAX_BYTES = 1_500_000

JARGON = (
    "seamless|effortless|revolutionary|game-changing|cutting-edge|"
    "next-generation|best-in-class|world-class|state-of-the-art|"
    "unleash|supercharge|delve|tapestry|elevate|synergy"
)

RULES = {
    "EM-DASH": ("info", "Punctuation cue only. Keep it when it fits the product voice; review generic or repetitive copy in context."),
    "EN-DASH": ("info", "Punctuation cue only. Preserve intentional typography and the user's style."),
    "LOOP-INFINITE": ("warn", "Review whether the loop communicates real state or supports this product. Decorative motion is not automatically wrong."),
    "KEYFRAME-DECOR": ("info", "Review this motion in context. Keep it when it communicates state, interaction, or an intentional brand moment."),
    "GRADIENT-HERO": ("info", "A familiar gradient was found. Check whether it fits the brief; the pattern alone is not a defect."),
    "RAINBOW-GRADIENT": ("info", "A multi-hue gradient was found. Check its role, contrast, and fit with the product."),
    "TINY-TEXT": ("warn", "Check legibility, zoom, and the relevant text-size requirements; no universal 12px floor is assumed."),
    "GRADIENT-TEXT": ("info", "Check legibility and contrast in the rendered state; gradient text is not inherently a defect."),
    "TEXT-GLOW": ("info", "Check whether the effect supports identity or hierarchy and preserves legibility."),
    "BIG-GLOW": ("info", "Check whether this shadow communicates elevation or is decorative noise."),
    "CYBERPUNK": ("info", "Style cue only. Keep the direction when it matches the user's brief and the product."),
    "NEON-COLOR": ("info", "Color cue only. Check contrast, meaning, and product fit in context."),
    "EMOJI-ICON": ("info", "Check cross-platform rendering and accessible meaning; emoji may be appropriate as product content."),
    "ICON-SPAM": ("info", "Review whether each icon improves recognition or scanning; file count alone is not a defect."),
    "BUTTON-SPAM": ("info", "Review action hierarchy and semantics; button count alone is not a defect."),
    "LOREM": ("error", "Placeholder copy is present. Replace it or label the screen as a content prototype."),
    "COMING-SOON": ("warn", "Check whether this is an intentional product message or an unfinished placeholder."),
    "TODO-MARKER": ("warn", "Check whether this marker or unfinished work belongs in the shipped interface."),
    "HOTLINK": ("warn", "Check asset rights, reliability, and whether this is a placeholder URL."),
    "ALERT-DIALOG": ("error", "alert()/confirm()/prompt(). Use inline messages, dialogs, or toasts with role=status."),
    "IMG-NO-ALT": ("error", "<img> without alt text."),
    "OUTLINE-KILL": ("warn", "outline: none/0 with no :focus-visible replacement in this file."),
    "INTER-IDENTITY": ("info", "Check whether this typeface is a deliberate brand or product choice; do not reject it by default."),
    "JARGON": ("info", "Check whether this claim is concrete and truthful in context; vocabulary alone is not a defect."),
    "PILL-DEFAULT": ("info", "Check whether the shape communicates a chip, state, or brand choice."),
    "UPPERCASE-SPAM": ("info", "Check readability and whether casing carries useful hierarchy or category meaning."),
    "IMPORTANT-SPAM": ("info", "Frequent !important. Fix specificity instead."),
    "TERMINAL-CHROME": ("info", "Monospace terminal decoration (e.g. '01 //', '// OS', 'SYS SPEC'). Review whether this is a genuine CLI tool or decorative AI slop."),
    "FAKE-TELEMETRY": ("info", "Simulated device telemetry or fake metric gauge (e.g. 'Drain / Hr', 'Calories Burned Today' in fake mockup frame). Replace with authentic artifacts or clean architecture."),
}

DECOR_KEYFRAMES = re.compile(
    r"@keyframes\s+[\w-]*(blink|pulse|bounce|float|glow|shimmer|flicker|neon|wiggle)[\w-]*",
    re.IGNORECASE,
)
GRADIENT = re.compile(r"(?:linear|radial|conic)-gradient\s*\(", re.IGNORECASE)
HEX = re.compile(r"#[0-9a-fA-F]{3,8}")
GRADIENT_CLIP = re.compile(r"background-clip:\s*text", re.IGNORECASE)
FONT_SIZE_PX = re.compile(r"font-size\s*:\s*(\d+(?:\.\d+)?)px", re.IGNORECASE)
TEXT_SHADOW = re.compile(r"text-shadow\s*:", re.IGNORECASE)
BIG_SHADOW = re.compile(r"box-shadow\s*:[^;]*?(?:[4-9]\d|[1-9]\d\d)px", re.IGNORECASE)
CYBER = re.compile(r"\b(cyberpunk|synthwave|vaporwave|holographic|glitch)\b", re.IGNORECASE)
NEON_WORD = re.compile(r"\bneon\b", re.IGNORECASE)
NEON_HEX = re.compile(r"#(?:00ff00|39ff14|00ff41|ff10f0)\b|#0f0\b", re.IGNORECASE)
EMOJI = re.compile(
    "[\U0001F000-\U0001FAFF\u2600-\u26FF\u2700-\u27BF\u2B00-\u2BFF\uFE0F\u2049\u203C]"
)
ICON_PACKAGES = r"(?:lucide-react|@heroicons/react(?:/[^\"']*)?|react-icons(?:/[^\"']*)?|@radix-ui/react-icons|@tabler/icons-react|@phosphor-icons/react|@iconify/react|@mui/icons-material|@ant-design/icons)"
ICON_IMPORT = re.compile(
    r"(?ms)^\s*import\b(?P<bindings>(?:(?!^\s*(?:import|export)\b).)*?)\bfrom\s*(['\"])(?:" + ICON_PACKAGES + r")\2"
)
ICON_MARKUP = re.compile(r"data-lucide=", re.IGNORECASE)
BUTTON = re.compile(r"<button\b", re.IGNORECASE)
LOREM = re.compile(r"lorem\s+ipsum", re.IGNORECASE)
COMING = re.compile(r"coming\s+soon", re.IGNORECASE)
TODO = re.compile(r"\b(TODO|FIXME)\b")
HOTLINK = re.compile(r"(?:placehold\.co|via\.placeholder\.com|picsum\.photos|placekitten\.com|images\.unsplash\.com)", re.IGNORECASE)
ALERT = re.compile(r"(?<![\w$.])(?:alert|confirm|prompt)\s*\(|\b(?:window|globalThis)\.(?:alert|confirm|prompt)\s*\(", re.IGNORECASE)
IMG_START = re.compile(r"<img\b", re.IGNORECASE)
IMG_ALT = re.compile(r"(?<![\w:-])alt\s*=|(?<![\w-])(?::alt|v-bind:alt)\s*=", re.IGNORECASE)
SCRIPT_TAG = re.compile(r"(<script\b([^>]*)>)(.*?)(</script\s*>|$)", re.IGNORECASE | re.DOTALL)
STYLE_TAG = re.compile(r"(<style\b[^>]*>)(.*?)(</style\s*>|$)", re.IGNORECASE | re.DOTALL)
ASTRO_FRONTMATTER = re.compile(r"\A(---[ \t]*\r?\n)(.*?)(\r?\n---[ \t]*(?:\r?\n|$))", re.DOTALL)
OUTLINE_NONE = re.compile(r"outline\s*:\s*(?:none|0)\b", re.IGNORECASE)
FOCUS_VISIBLE = re.compile(r":focus-visible", re.IGNORECASE)
INTER = re.compile(r"font-family\s*:\s*[\"']?Inter\b[\"']?", re.IGNORECASE)
JARGON_RE = re.compile(r"\b(" + JARGON + r")\b", re.IGNORECASE)
PILL = re.compile(r"border-radius\s*:\s*(?:9999px|9999rem|100vmax|999px)", re.IGNORECASE)
TAILWIND_PILL = re.compile(r"(?<![\w-])rounded-full(?![\w-])")
UPPERCASE = re.compile(r"text-transform\s*:\s*uppercase", re.IGNORECASE)
IMPORTANT = re.compile(r"!important")
EM_DASH = re.compile("[\u2014\u2015]")
EN_DASH = re.compile("[\u2013]")
TERMINAL_CHROME = re.compile(r"(?:\b0\d\s*//|(?<![:/])//\s*[A-Z_]{2,}|\bSYS\s*SPEC\s*INDEX\b)")
FAKE_TELEMETRY = re.compile(r"\b(drain\s*/\s*hr|calories\s*burned\s*today|sys\s*spec\s*index|telemetry\s*blueprint)\b", re.IGNORECASE)

ANIMATION_INFINITE = re.compile(r"\banimation(?:-[\w-]+)?\s*:[^;}]*\binfinite\b", re.IGNORECASE)
ANIMATION_EXEMPT = re.compile(
    r"spinner|loading|progress|skeleton|aria-busy|marquee|ticker", re.IGNORECASE
)


def count_icon_references(text):
    """Count supported named icon imports and explicit data-lucide attributes."""
    count = len(ICON_MARKUP.findall(text))
    for match in ICON_IMPORT.finditer(text):
        bindings = match.group("bindings").strip()
        brace_start = bindings.find("{")
        if brace_start >= 0:
            brace_end = bindings.find("}", brace_start + 1)
            if brace_end >= 0:
                names = [name for name in bindings[brace_start + 1 : brace_end].split(",") if name.strip()]
                count += len(names)
                default_binding = bindings[:brace_start].strip().rstrip(",").replace("type ", "", 1).strip()
                if default_binding:
                    count += 1
        elif re.match(r"(?:type\s+)?(?:\*\s+as\s+\w+|[\w$]+)", bindings):
            count += 1
    return count


def strip_comments(text, ext):
    """Blank comments while preserving line breaks, offsets, and quoted text."""
    if ext in MARKUP_EXT:
        def blank_match(match):
            return "".join(ch if ch in "\r\n" else " " for ch in match.group(0))

        cleaned = re.sub(r"<!--.*?(?:-->|$)", blank_match, text, flags=re.DOTALL)

        if ext == ".astro":
            frontmatter = ASTRO_FRONTMATTER.match(cleaned)
            if frontmatter:
                cleaned = (
                    frontmatter.group(1)
                    + strip_comments(frontmatter.group(2), ".js")
                    + frontmatter.group(3)
                    + cleaned[frontmatter.end() :]
                )

        def clean_script(match):
            attrs = match.group(2)
            if re.search(r"\btype\s*=\s*[\"']?application/(?:ld\+)?json\b", attrs, re.IGNORECASE):
                return match.group(0)
            return match.group(1) + strip_comments(match.group(3), ".js") + match.group(4)

        cleaned = SCRIPT_TAG.sub(clean_script, cleaned)
        cleaned = STYLE_TAG.sub(
            lambda match: match.group(1) + strip_comments(match.group(2), ".css") + match.group(3),
            cleaned,
        )
        return cleaned

    if ext in {".md", ".mdx", ".txt"}:
        text = re.sub(
            r"<!--.*?(?:-->|$)",
            lambda match: "".join(ch if ch in "\r\n" else " " for ch in match.group(0)),
            text,
            flags=re.DOTALL,
        )

    chars = list(text)
    n = len(chars)
    i = 0
    quote = None
    line_comments = ext in JS_EXT or ext in {".scss", ".sass", ".less"}

    def blank(start, end):
        for index in range(start, end):
            if chars[index] not in "\r\n":
                chars[index] = " "

    while i < n:
        ch = chars[i]
        if quote:
            if ch == "\\":
                i += 2
                continue
            if ch == quote:
                quote = None
            i += 1
            continue
        if ch in "'\"`":
            quote = ch
            i += 1
            continue
        if text.startswith("/*", i):
            end = text.find("*/", i + 2)
            end = n if end < 0 else end + 2
            blank(i, end)
            i = end
            continue
        if line_comments and text.startswith("//", i):
            url_context = ext in {".scss", ".sass", ".less"} and (
                (i > 0 and text[i - 1] == ":")
                or re.search(r"url\(\s*$", text[:i], re.IGNORECASE)
            )
            if url_context:
                i += 2  # preserve absolute and protocol-relative unquoted URLs
                continue
            end = text.find("\n", i + 2)
            end = n if end < 0 else end
            blank(i, end)
            i = end
            continue
        i += 1
    return "".join(chars)


def iter_gradients(text):
    """Yield balanced gradient argument strings, including nested color functions."""
    for match in GRADIENT.finditer(text):
        start = match.end()
        depth = 1
        quote = None
        i = start
        while i < len(text) and depth:
            ch = text[i]
            if quote:
                if ch == "\\":
                    i += 2
                    continue
                if ch == quote:
                    quote = None
            elif ch in "'\"`":
                quote = ch
            elif ch == "(":
                depth += 1
            elif ch == ")":
                depth -= 1
            i += 1
        if depth == 0:
            yield match.start(), text[start : i - 1]


def iter_img_tags(text):
    """Yield complete img tags while respecting quoted `>` characters."""
    for match in IMG_START.finditer(text):
        quote = None
        i = match.end()
        while i < len(text):
            char = text[i]
            if quote:
                if char == quote:
                    quote = None
            elif char in "'\"":
                quote = char
            elif char == ">":
                yield match.start(), text[match.start() : i + 1]
                break
            i += 1


def resolve_custom_properties(text, source_text):
    """Expand same-file CSS custom properties in a gradient for color review."""
    properties = {
        match.group(1): match.group(2).strip()
        for match in re.finditer(r"(--[\w-]+)\s*:\s*([^;{}]+)", source_text)
    }
    variable = re.compile(r"var\(\s*(--[\w-]+)(?:\s*,\s*([^)]*))?\s*\)", re.IGNORECASE)
    expanded = text
    for _ in range(8):
        changed = False

        def replace(match):
            nonlocal changed
            value = properties.get(match.group(1))
            if value is None:
                value = match.group(2) or match.group(0)
            else:
                changed = True
            return value

        expanded = variable.sub(replace, expanded)
        if not changed:
            break
    return expanded


def gradient_hues(args_text):
    """Extract recognizable (hue, saturation) pairs from common CSS colors."""
    colors = []
    for match in HEX.finditer(args_text):
        color = hue_family(match.group(0))
        if color:
            colors.append(color)
    number = r"([+-]?(?:\d+(?:\.\d*)?|\.\d+))"
    angle_unit = r"(deg|rad|turn)?"
    hsl = re.compile(r"hsla?\(\s*" + number + angle_unit + r"(?:\s*,\s*|\s+)" + number + r"%", re.IGNORECASE)
    for match in hsl.finditer(args_text):
        value = float(match.group(1))
        unit = (match.group(2) or "deg").lower()
        hue = value * (360 if unit == "turn" else 180 / 3.141592653589793 if unit == "rad" else 1)
        colors.append((hue % 360, min(1.0, abs(float(match.group(3))) / 100)))
    oklch = re.compile(r"oklch\(\s*[^\s,)]+\s+" + number + r"(%?)\s+" + number + angle_unit, re.IGNORECASE)
    for match in oklch.finditer(args_text):
        chroma = abs(float(match.group(1)))
        if match.group(2):
            chroma /= 100
        value = float(match.group(3))
        unit = (match.group(4) or "deg").lower()
        hue = value * (360 if unit == "turn" else 180 / 3.141592653589793 if unit == "rad" else 1)
        colors.append((hue % 360, min(1.0, chroma * 3)))
    for name, hue in (("red", 0), ("orange", 30), ("yellow", 60), ("green", 120), ("cyan", 180), ("blue", 220), ("indigo", 245), ("purple", 275), ("violet", 285), ("fuchsia", 310), ("magenta", 315)):
        if re.search(r"--[\w-]*" + name + r"[\w-]*|\b" + name + r"\b", args_text, re.IGNORECASE):
            colors.append((float(hue), 1.0))
    return colors


def hue_family(hex_text):
    """Return the HSV hue (degrees) and saturation for a hex color, else None."""
    text = hex_text[1:]
    if len(text) == 3:
        text = "".join(c * 2 for c in text)
    if len(text) not in (6, 8):
        return None
    try:
        r, g, b = (int(text[i : i + 2], 16) / 255.0 for i in (0, 2, 4))
    except ValueError:
        return None
    h, s, _v = colorsys.rgb_to_hsv(r, g, b)
    return h * 360.0, s


def is_default_gradient(args_text):
    """True when a gradient mixes two or more purple-family hues, or names them.

    The band starts at 235 degrees so the Tailwind indigos (indigo-500 sits
    near 239, indigo-600 near 243) count as the purple family; true blues sit
    below 225 degrees and stay out of it.
    """
    colors = gradient_hues(args_text)
    purples = [hue for hue, saturation in colors if saturation > 0.15 and 235 <= hue <= 340]
    return len(purples) >= 2


def is_rainbow_gradient(args_text):
    """True when a gradient spans two or more saturated hues far apart on the wheel."""
    colors = [hue for hue, saturation in gradient_hues(args_text) if saturation > 0.25]
    for i in range(len(colors)):
        for j in range(i + 1, len(colors)):
            distance = abs(colors[i] - colors[j])
            distance = min(distance, 360 - distance)
            if distance > 100:
                return True
    return False


def scan_file(path):
    """Return a list of findings for one file."""
    with open(path, "rb") as handle:
        raw = handle.read(MAX_BYTES + 1)
    if len(raw) > MAX_BYTES or b"\x00" in raw[:4096]:
        return []
    text = raw.decode("utf-8", errors="replace")
    ext = os.path.splitext(path)[1].lower()
    scan_text = strip_comments(text, ext)
    findings = []

    def add(rule, line_no, col, extra=""):
        severity, base_message = RULES[rule]
        message = base_message + (" " + extra if extra else "")
        findings.append((line_no, col, rule, severity, message))

    for line_no, line in enumerate(scan_text.splitlines(), 1):
        for match in EM_DASH.finditer(line):
            add("EM-DASH", line_no, match.start() + 1)
        if EN_DASH.search(line):
            add("EN-DASH", line_no, EN_DASH.search(line).start() + 1)
        if DECOR_KEYFRAMES.search(line):
            add("KEYFRAME-DECOR", line_no, 1)
        if ext not in {".md", ".mdx", ".txt"}:
            tiny = FONT_SIZE_PX.search(line)
            if tiny and float(tiny.group(1)) < 12:
                add("TINY-TEXT", line_no, tiny.start() + 1)
        if GRADIENT_CLIP.search(line):
            add("GRADIENT-TEXT", line_no, GRADIENT_CLIP.search(line).start() + 1)
        if TEXT_SHADOW.search(line):
            add("TEXT-GLOW", line_no, TEXT_SHADOW.search(line).start() + 1)
        if BIG_SHADOW.search(line):
            add("BIG-GLOW", line_no, 1)
        if CYBER.search(line):
            add("CYBERPUNK", line_no, CYBER.search(line).start() + 1)
        elif NEON_WORD.search(line):
            add("CYBERPUNK", line_no, NEON_WORD.search(line).start() + 1, '(the word "neon")')
        if NEON_HEX.search(line):
            add("NEON-COLOR", line_no, NEON_HEX.search(line).start() + 1)
        if ext not in {".md", ".mdx", ".txt"} and EMOJI.search(line):
            add("EMOJI-ICON", line_no, EMOJI.search(line).start() + 1)
        if LOREM.search(line):
            add("LOREM", line_no, LOREM.search(line).start() + 1)
        if COMING.search(line):
            add("COMING-SOON", line_no, COMING.search(line).start() + 1)
        if TODO.search(line):
            add("TODO-MARKER", line_no, TODO.search(line).start() + 1)
        if HOTLINK.search(line):
            add("HOTLINK", line_no, HOTLINK.search(line).start() + 1)
        if INTER.search(line):
            add("INTER-IDENTITY", line_no, INTER.search(line).start() + 1)
        for match in JARGON_RE.finditer(line):
            add("JARGON", line_no, match.start() + 1, '(the word "{}")'.format(match.group(1)))
        if PILL.search(line):
            add("PILL-DEFAULT", line_no, PILL.search(line).start() + 1)
        elif TAILWIND_PILL.search(line):
            add("PILL-DEFAULT", line_no, TAILWIND_PILL.search(line).start() + 1)
        if UPPERCASE.search(line):
            add("UPPERCASE-SPAM", line_no, UPPERCASE.search(line).start() + 1)
        if len(IMPORTANT.findall(line)) > 2:
            add("IMPORTANT-SPAM", line_no, 1)
        if TERMINAL_CHROME.search(line):
            add("TERMINAL-CHROME", line_no, TERMINAL_CHROME.search(line).start() + 1)
        if FAKE_TELEMETRY.search(line):
            add("FAKE-TELEMETRY", line_no, FAKE_TELEMETRY.search(line).start() + 1)

    alert_sources = []
    if ext in JS_EXT:
        alert_sources.append((scan_text, 0))
    elif ext in MARKUP_EXT:
        if ext == ".astro":
            frontmatter = ASTRO_FRONTMATTER.match(scan_text)
            if frontmatter:
                alert_sources.append((frontmatter.group(2), frontmatter.start(2)))
        for block in SCRIPT_TAG.finditer(scan_text):
            if not re.search(r"\btype\s*=\s*[\"']?application/(?:ld\+)?json\b", block.group(2), re.IGNORECASE):
                alert_sources.append((block.group(3), block.start(3)))
    for source, base_offset in alert_sources:
        for match in ALERT.finditer(source):
            offset = base_offset + match.start()
            line_no = scan_text.count("\n", 0, offset) + 1
            line_start = scan_text.rfind("\n", 0, offset) + 1
            add("ALERT-DIALOG", line_no, offset - line_start + 1)

    for offset, args_text in iter_gradients(scan_text):
        line_no = scan_text.count("\n", 0, offset) + 1
        line_start = scan_text.rfind("\n", 0, offset) + 1
        col = offset - line_start + 1
        args_text = resolve_custom_properties(args_text, scan_text)
        if is_default_gradient(args_text):
            add("GRADIENT-HERO", line_no, col)
        elif is_rainbow_gradient(args_text):
            add("RAINBOW-GRADIENT", line_no, col)

    if ext in CSS_EXT:
        for block in re.finditer(r"([^{}]+)\{([^{}]*)\}", scan_text, re.DOTALL):
            selector, body = block.group(1), block.group(2)
            infinite = ANIMATION_INFINITE.search(body)
            animation_values = re.findall(r"\banimation(?:-name)?\s*:\s*([^;}]+)", body, re.IGNORECASE)
            exempt = ANIMATION_EXEMPT.search(selector) or any(
                ANIMATION_EXEMPT.search(value) for value in animation_values
            )
            if infinite and not exempt:
                offset = block.start(2) + infinite.start()
                line_no = scan_text.count("\n", 0, offset) + 1
                line_start = scan_text.rfind("\n", 0, offset) + 1
                add("LOOP-INFINITE", line_no, offset - line_start + 1)

    if ext in IMG_EXT:
        for offset, tag in iter_img_tags(scan_text):
            if not IMG_ALT.search(tag):
                line_no = scan_text.count("\n", 0, offset) + 1
                line_start = scan_text.rfind("\n", 0, offset) + 1
                add("IMG-NO-ALT", line_no, offset - line_start + 1)

    counts = {
        "icons": count_icon_references(scan_text),
        "button": len(BUTTON.findall(scan_text)),
        "uppercase": len(UPPERCASE.findall(scan_text)),
        "important": len(IMPORTANT.findall(scan_text)),
    }
    if counts["icons"] > 8:
        findings.append((0, 0, "ICON-SPAM", "info",
                         "{} supported icon-library references in one file; review them in the rendered context.".format(counts["icons"])))
    if counts["button"] > 6:
        findings.append((0, 0, "BUTTON-SPAM", "info",
                         "{} <button> elements in one file; review semantics and hierarchy per view.".format(counts["button"])))
    if counts["uppercase"] > 3:
        findings.append((0, 0, "UPPERCASE-SPAM", "info",
                         "{} uppercase transforms in one file.".format(counts["uppercase"])))
    if counts["important"] > 3:
        findings.append((0, 0, "IMPORTANT-SPAM", "info",
                         "{} !important declarations in one file.".format(counts["important"])))
    if OUTLINE_NONE.search(scan_text) and not FOCUS_VISIBLE.search(scan_text):
        findings.append((0, 0, "OUTLINE-KILL", "warn",
                         "outline removed with no :focus-visible style in this file."))

    findings.sort(key=lambda f: (f[0], f[1]))
    return findings


def iter_files(paths):
    for root_path in paths:
        if os.path.isfile(root_path):
            yield root_path
            continue
        for current, dirs, names in os.walk(root_path):
            dirs[:] = [d for d in dirs if d not in SKIP_DIRS and not d.startswith(".")]
            for name in names:
                ext = os.path.splitext(name)[1].lower()
                if ext in CODE_EXT:
                    yield os.path.join(current, name)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("paths", nargs="*", help="files or folders to scan")
    parser.add_argument("--rules", action="store_true", help="list rules and exit")
    parser.add_argument("--strict", action="store_true", help="warnings also fail the run")
    parser.add_argument("--allow-infinite", action="store_true", help="do not flag infinite animations")
    parser.add_argument("--format", choices=["text", "json"], default="text")
    args = parser.parse_args(argv)

    if args.rules:
        for name, (severity, message) in RULES.items():
            print("{:16} [{:5}] {}".format(name, severity, message))
        return 0

    if not args.paths:
        parser.print_usage()
        print("Give at least one file or folder, or use --rules.")
        return 2

    report = {}
    for path in iter_files(args.paths):
        findings = scan_file(path)
        if args.allow_infinite:
            findings = [f for f in findings if f[2] != "LOOP-INFINITE"]
        if findings:
            report[path] = findings

    totals = {"error": 0, "warn": 0, "info": 0}
    for findings in report.values():
        for finding in findings:
            totals[finding[3]] += 1

    if args.format == "json":
        print(json.dumps({
            "files": {
                path: [
                    {"line": f[0], "col": f[1], "rule": f[2], "severity": f[3], "message": f[4]}
                    for f in findings
                ]
                for path, findings in report.items()
            },
            "summary": totals,
        }, indent=2))
    else:
        for path, findings in report.items():
            print(path)
            for line_no, col, rule, severity, message in findings:
                where = "{}:{}".format(line_no, col) if line_no else "file"
                print("  {:>8}  {:14} [{:5}] {}".format(where, rule, severity, message))
        file_count = len(report)
        print("\n{} file(s) with findings. {} error(s), {} warning(s), {} note(s).".format(
            file_count, totals["error"], totals["warn"], totals["info"]))

    failed = totals["error"] > 0 or (args.strict and totals["warn"] > 0)
    if args.format != "json":
        print("Fail. Review error findings as likely defects; see references/anti-slop.md." if failed
              else "No error-level findings. Review contextual cues and inspect the rendered result.")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
