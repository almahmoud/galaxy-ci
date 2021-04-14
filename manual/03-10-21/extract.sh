#!/bin/bash
set -e
PASSED=$(awk '/passed/{print}' "$1" | tr -d '\000');
FAILED=$(awk '/failed/{print}' "$1" | tr -d '\000');
ALL=$(cat "$1" | tr -d '\000');
[[ ! -z "$PASSED" ]] && echo "$PASSED" > passed;
[[ ! -z "$FAILED" ]] && echo "$FAILED" > failed;
[[ ! -z "$ALL" ]] && echo "$ALL" > all;

