#!/usr/bin/env bash
# Convenience wrapper. The Python runner is the canonical cross-platform suite.
set -eu
cd "$(dirname "$0")/.."
PYTHON="${PYTHON:-python3}"
exec "$PYTHON" tests/run_tests.py
