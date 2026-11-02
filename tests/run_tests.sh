#!/usr/bin/env bash
# Test runner for the slopless-ui repository.
# Verifies the scripts behave as documented and that the repo stays clean.
# Run with: bash tests/run_tests.sh

set -u
cd "$(dirname "$0")/.."

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
python3 scripts/foldcheck.py --rules > /dev/null 2>&1
check "foldcheck --rules exits 0" "0" "$?"

echo "2. foldcheck rule count"
check "foldcheck lists exactly 27 rules" "27" "$(python3 scripts/foldcheck.py --rules | wc -l | tr -d ' ')"

echo "3. foldcheck flags the sloppy fixture"
python3 scripts/foldcheck.py tests/fixtures/sloppy.html > /dev/null 2>&1
check "sloppy fixture fails (exit 1)" "1" "$?"

echo "4. foldcheck passes the clean fixture"
python3 scripts/foldcheck.py tests/fixtures/clean.html > /dev/null 2>&1
check "clean fixture passes (exit 0)" "0" "$?"

echo "5. foldcheck rejects the unguided builds"
python3 scripts/foldcheck.py examples/oscilla/before.html > /dev/null 2>&1
check "dev-tool before fails on real patterns (exit 1)" "1" "$?"
python3 scripts/foldcheck.py examples/outerform/before.html > /dev/null 2>&1
check "studio before fails on real patterns (exit 1)" "1" "$?"
python3 scripts/foldcheck.py examples/nocturne/before.html > /dev/null 2>&1
check "festival before fails on real patterns (exit 1)" "1" "$?"

echo "6. foldcheck passes every finished page"
python3 scripts/foldcheck.py examples/oscilla/index.html > /dev/null 2>&1
check "dev-tool after passes (exit 0)" "0" "$?"
python3 scripts/foldcheck.py examples/outerform/index.html > /dev/null 2>&1
check "studio after passes (exit 0)" "0" "$?"
python3 scripts/foldcheck.py examples/nocturne/index.html > /dev/null 2>&1
check "festival after passes (exit 0)" "0" "$?"

echo "7. foldcheck strict mode fails on warnings"
python3 scripts/foldcheck.py --strict tests/fixtures/sloppy.html > /dev/null 2>&1
check "sloppy fixture fails strict (exit 1)" "1" "$?"

echo "8. foldcheck json output parses"
python3 scripts/foldcheck.py --format json tests/fixtures/sloppy.html 2>/dev/null | python3 -c "import json,sys; d=json.load(sys.stdin); assert d['summary']['error'] > 0" 2>/dev/null
check "json output has errors" "0" "$?"

echo "9. the ticker exemption is deliberate"
printf 'a { animation: ticker-scroll 36s linear infinite; }\n' > /tmp/slopless-ticker.css
python3 scripts/foldcheck.py /tmp/slopless-ticker.css > /dev/null 2>&1
check "named ticker loop passes (exit 0)" "0" "$?"
printf 'a { animation: drift 6s ease-in-out infinite; }\n' > /tmp/slopless-drift.css
python3 scripts/foldcheck.py /tmp/slopless-drift.css > /dev/null 2>&1
check "unnamed infinite loop still fails (exit 1)" "1" "$?"
rm -f /tmp/slopless-ticker.css /tmp/slopless-drift.css

echo "10. contrast grades a passing pair"
python3 scripts/contrast.py "#201B12" "#F6F1E5" > /dev/null 2>&1
check "AAA pair passes (exit 0)" "0" "$?"

echo "11. contrast grades a failing pair"
python3 scripts/contrast.py "#999999" "#FFFFFF" > /dev/null 2>&1
check "gray on white fails (exit 1)" "1" "$?"

echo "12. contrast suggests a passing shade"
python3 scripts/contrast.py "#999999" "#FFFFFF" --suggest 2>/dev/null | grep -q "suggested:"
check "suggestion printed" "0" "$?"

echo "13. contrast large-text threshold"
python3 scripts/contrast.py "#A8431F" "#E7ECE9" --min 3.0 > /dev/null 2>&1
check "5.04:1 passes --min 3.0 (exit 0)" "0" "$?"

echo "14. scripts compile"
python3 -m py_compile scripts/foldcheck.py scripts/contrast.py tests/check_ratios.py 2>/dev/null
check "python scripts compile" "0" "$?"
node --check scripts/finish.mjs 2>/dev/null
check "finish.mjs parses" "0" "$?"

echo "15. no em dashes anywhere in the repo's own text"
if python3 - <<'PYEOF'
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

echo "16. every contrast number in color.md matches the script"
python3 tests/check_ratios.py > /dev/null 2>&1
check "palette ratios verified" "0" "$?"

echo "17. SKILL.md frontmatter matches the folder name"
python3 - <<'PYEOF'
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

echo "18. finished pages carry the accessibility floor"
for page in examples/oscilla/index.html examples/outerform/index.html examples/nocturne/index.html; do
  if grep -q "prefers-reduced-motion" "$page" && grep -q ":focus-visible" "$page"; then
    check "$page ships reduced motion and focus styles" "0" "0"
  else
    check "$page ships reduced motion and focus styles" "0" "1"
  fi
done

echo "19. finished pages choreograph motion"
for page in examples/oscilla/index.html examples/outerform/index.html examples/nocturne/index.html; do
  if grep -q "IntersectionObserver" "$page" && grep -q "data-reveal" "$page"; then
    check "$page reveals on scroll" "0" "0"
  else
    check "$page reveals on scroll" "0" "1"
  fi
done

echo
echo "$pass passed, $fail failed"
[ "$fail" -eq 0 ]
