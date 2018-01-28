#!/usr/bin/env bats

SCRIPT_PATH="$BATS_TEST_DIRNAME"
export ROOT="$SCRIPT_PATH/../.."
export PYTHONPATH="$ROOT"

cd "$ROOT"

@test "Method too long rule" {
    pylint --rcfile="$ROOT/pylintrc" \
        "$ROOT/examples/complexity.py" | grep method-too-long
}