#!/usr/bin/env bash
# Test runner for the slopless-ui repository.
# Verifies the scripts behave as documented and that the repo stays clean.
# Run with: bash tests/run_tests.sh

set -u
cd "$(dirname "$0")/.."
PYTHON="${PYTHON:-python3}"

pass=0
fail=0

check() {
  local name="$1" expected="$2" actual="$3"
  if [ "$actual" = "$expected" ]; then
    echo "ok    $name"
    pass=$((pass + 1))
  else
    echo "FAIL  $name (expected $expected, got $actual)"
    fail=$((fail + 1))
  fi
}

echo "1. foldcheck rules listing"
"$PYTHON" scripts/foldcheck.py --rules > /dev/null 2>&1
check "foldcheck --rules exits 0" "0" "$?"

echo "2. foldcheck rule count"
check "foldcheck lists exactly 27 rules" "27" "$("$PYTHON" scripts/foldcheck.py --rules | wc -l | tr -d ' ')"

echo "3. foldcheck flags the sloppy fixture"
"$PYTHON" scripts/foldcheck.py tests/fixtures/sloppy.html > /dev/null 2>&1
check "sloppy fixture fails (exit 1)" "1" "$?"

echo "4. foldcheck passes the clean fixture"
"$PYTHON" scripts/foldcheck.py tests/fixtures/clean.html > /dev/null 2>&1
check "clean fixture passes (exit 0)" "0" "$?"

echo "5. foldcheck reports cues in the illustrative before pages without declaring a verdict"
for page in examples/oscilla/before.html examples/outerform/before.html examples/nocturne/before.html; do
  "$PYTHON" scripts/foldcheck.py --format json "$page" 2>/dev/null | "$PYTHON" -c "import json,sys; d=json.load(sys.stdin); assert d['summary']['info'] > 0 and d['summary']['error'] == 0" 2>/dev/null
  check "$page emits review cues without a style error" "0" "$?"
done

echo "6. foldcheck passes every finished page"
"$PYTHON" scripts/foldcheck.py examples/oscilla/index.html > /dev/null 2>&1
check "dev-tool after passes (exit 0)" "0" "$?"
"$PYTHON" scripts/foldcheck.py examples/outerform/index.html > /dev/null 2>&1
check "studio after passes (exit 0)" "0" "$?"
"$PYTHON" scripts/foldcheck.py examples/nocturne/index.html > /dev/null 2>&1
check "festival after passes (exit 0)" "0" "$?"

echo "7. foldcheck strict mode fails on warnings"
"$PYTHON" scripts/foldcheck.py --strict tests/fixtures/sloppy.html > /dev/null 2>&1
check "sloppy fixture fails strict (exit 1)" "1" "$?"

echo "8. foldcheck json output parses"
"$PYTHON" scripts/foldcheck.py --format json tests/fixtures/sloppy.html 2>/dev/null | "$PYTHON" -c "import json,sys; d=json.load(sys.stdin); assert d['summary']['error'] > 0" 2>/dev/null
check "json output has errors" "0" "$?"

echo "9. visual preferences are review cues, not build failures"
printf 'body { background: linear-gradient(135deg, #6366F1, #EC4899); font-family: Inter, sans-serif; }\n.pill { border-radius: 9999px; }\n' > /tmp/slopless-style-choice.css
"$PYTHON" scripts/foldcheck.py /tmp/slopless-style-choice.css > /dev/null 2>&1
check "purple gradient, familiar type, and pill pass the default audit" "0" "$?"
"$PYTHON" scripts/foldcheck.py --strict /tmp/slopless-style-choice.css > /dev/null 2>&1
check "visual preference cues do not fail strict mode" "0" "$?"
rm -f /tmp/slopless-style-choice.css

echo "10. the ticker exemption is deliberate"
printf 'a { animation: ticker-scroll 36s linear infinite; }\n' > /tmp/slopless-ticker.css
"$PYTHON" scripts/foldcheck.py /tmp/slopless-ticker.css > /dev/null 2>&1
check "named ticker loop passes (exit 0)" "0" "$?"
printf 'a { animation: drift 6s ease-in-out infinite; }\n' > /tmp/slopless-drift.css
"$PYTHON" scripts/foldcheck.py /tmp/slopless-drift.css > /dev/null 2>&1
check "unexplained loop is a review warning, not a default failure" "0" "$?"
"$PYTHON" scripts/foldcheck.py --strict /tmp/slopless-drift.css > /dev/null 2>&1
check "strict mode can promote review warnings" "1" "$?"
rm -f /tmp/slopless-ticker.css /tmp/slopless-drift.css

echo "11. contrast grades a passing pair"
"$PYTHON" scripts/contrast.py "#201B12" "#F6F1E5" > /dev/null 2>&1
check "AAA pair passes (exit 0)" "0" "$?"

echo "12. contrast grades a failing pair"
"$PYTHON" scripts/contrast.py "#999999" "#FFFFFF" > /dev/null 2>&1
check "gray on white fails (exit 1)" "1" "$?"

echo "13. contrast suggests a passing shade"
"$PYTHON" scripts/contrast.py "#999999" "#FFFFFF" --suggest 2>/dev/null | grep -q "suggested:"
check "suggestion printed" "0" "$?"

echo "14. contrast large-text threshold"
"$PYTHON" scripts/contrast.py "#A8431F" "#E7ECE9" --min 3.0 > /dev/null 2>&1
check "5.04:1 passes --min 3.0 (exit 0)" "0" "$?"

echo "15. scripts compile"
"$PYTHON" -m py_compile scripts/foldcheck.py scripts/contrast.py tests/check_ratios.py 2>/dev/null
check "python scripts compile" "0" "$?"
node --check scripts/finish.mjs 2>/dev/null
check "finish.mjs parses" "0" "$?"

echo "16. no em dashes anywhere in the repo's own text"
if "$PYTHON" - <<'PYEOF'
import pathlib, sys
bad = []
for path in pathlib.Path(".").rglob("*"):
    if "tests/fixtures" in path.as_posix() or path.name == "before.html":
        continue  # fixtures and the slop specimens intentionally contain banned patterns
    if path.suffix in {".md", ".html", ".py", ".mjs", ".yml", ".sh"} and path.is_file():
        try:
            text = path.read_text(encoding="utf-8")
        except Exception:
            continue
        if "\u2014" in text or "\u2015" in text:
            bad.append(str(path))
if bad:
    print("em dashes found in: " + ", ".join(bad), file=sys.stderr)
    sys.exit(1)
PYEOF
then
  check "no em dashes" "0" "$?"
else
  check "no em dashes" "0" "1"
fi

echo "17. every contrast number in color.md matches the script"
"$PYTHON" tests/check_ratios.py > /dev/null 2>&1
check "palette ratios verified" "0" "$?"

echo "18. SKILL.md frontmatter matches the folder name"
"$PYTHON" - <<'PYEOF'
import pathlib, re, sys
text = pathlib.Path("SKILL.md").read_text(encoding="utf-8")
match = re.search(r"^---\n(.*?)\n---", text, re.DOTALL)
assert match, "frontmatter block missing"
front = match.group(1)
name = re.search(r"^name:\s*(.+)$", front, re.MULTILINE)
assert name and name.group(1).strip() == "slopless-ui", "name must be slopless-ui"
desc = re.search(r"^description:\s*(.+)$", front, re.MULTILINE)
assert desc and len(desc.group(1)) <= 1024, "description must exist and stay under 1024 chars"
PYEOF
check "SKILL.md frontmatter valid" "0" "$?"

echo "19. skill references resolve"
"$PYTHON" - <<'PYEOF'
import pathlib, re, sys
root = pathlib.Path('.')
text = (root / 'SKILL.md').read_text(encoding='utf-8')
missing = []
for target in re.findall(r'\[[^\]]+\]\(([^)]+)\)', text):
    if target.startswith(('http://', 'https://', '#', 'mailto:')):
        continue
    path = (root / target.split('#', 1)[0]).resolve()
    if not path.is_file():
        missing.append(target)
if missing:
    print('missing references: ' + ', '.join(missing), file=sys.stderr)
    sys.exit(1)
PYEOF
check "all SKILL.md linked files exist" "0" "$?"

echo "20. finished pages carry the accessibility floor"
for page in examples/oscilla/index.html examples/outerform/index.html examples/nocturne/index.html; do
  if grep -q "prefers-reduced-motion" "$page" && grep -q ":focus-visible" "$page"; then
    check "$page ships reduced motion and focus styles" "0" "0"
  else
    check "$page ships reduced motion and focus styles" "0" "1"
  fi
done

echo "21. finished pages declare a device-width viewport"
for page in examples/oscilla/index.html examples/outerform/index.html examples/nocturne/index.html; do
  if grep -q 'name="viewport"' "$page"; then
    check "$page includes responsive viewport metadata" "0" "0"
  else
    check "$page includes responsive viewport metadata" "0" "1"
  fi
done

echo
echo "$pass passed, $fail failed"
[ "$fail" -eq 0 ]
