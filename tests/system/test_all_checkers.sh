#!/usr/bin/env bats

SCRIPT_PATH="$BATS_TEST_DIRNAME"
export ROOT="$SCRIPT_PATH/../.."
export PYTHONPATH="$ROOT"

cd "$ROOT"

run_pylint() {
    local file_path="$1"; shift
    local expected_error_message="$1"; shift
    run pylint --rcfile="$ROOT/pylintrc" \
        "$file_path"
    echo $status
    echo "$output"
    echo "$output" | grep "$expected_error_message"

}

@test "Method too long rule" {
    run_pylint "$ROOT/examples/method_length.py" method-too-long
}

@test "Cyclomatic complexity too high" {
    run_pylint "$ROOT/examples/cyclomatic_complexity.py" too-complex
}

@test "Too many methods rule" {
    run_pylint "$ROOT/examples/method_count_in_class.py" too-many-methods
}