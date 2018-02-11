#!/usr/bin/env bats

export ROOT="$BATS_TEST_DIRNAME/../.."
export EXAMPLES_ROOT="$BATS_TEST_DIRNAME/examples"
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
    run_pylint "$EXAMPLES_ROOT/method_length.py" method-too-long
}

@test "Cyclomatic complexity too high" {
    run_pylint "$EXAMPLES_ROOT/cyclomatic_complexity.py" too-complex
}

@test "Too many methods rule" {
    run_pylint "$EXAMPLES_ROOT/method_count_in_class.py" too-many-methods
}