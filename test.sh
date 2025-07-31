#!/usr/bin/env sh

set -e

docker run --rm --network test_docker_alias_default test_docker_alias:local python3 test.py
