#!/usr/bin/env sh

docker compose \
  --project-name test_docker_alias \
  -f test_docker_alias.yml \
  up -d
