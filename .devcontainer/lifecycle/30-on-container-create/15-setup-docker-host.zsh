#!/usr/bin/env zsh
#
# This script configures Docker contexts for dev container environments
# supporting both Docker-in-Docker (DinD) and Docker-outside-Docker patterns.
#
# NOTES:
# - Part 2/2 of the Docker host setup. Part 1 is in `00-on-dockerfile/15-docker-host.zsh`.
#

# Setup Docker context for docker-outside-docker
docker context create docker-host --docker "host=unix:///var/run/docker-host.sock"

# "default" context uses DinD
docker context use default
