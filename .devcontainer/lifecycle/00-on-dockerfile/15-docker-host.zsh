#!/usr/bin/env zsh
#
# This script configures Docker contexts for dev container environments
# supporting both Docker-in-Docker (DinD) and Docker-outside-Docker patterns.
#
# NOTES:
# - Part 1/2 of the Docker host setup. Part 2 is in `30-on-container-create/15-docker-host.zsh`.
#

# Create docker-host group with matching host GID for Docker socket access
HOST_DOCKER_GID=$(stat -c '%g' /var/run/docker-host.sock 2>/dev/null || echo "997")
sudo groupadd -g "$HOST_DOCKER_GID" docker-host

# Add vscode user to docker-host group
[ -z "$USER" ] && USER=$(whoami 2>/dev/null || echo "vscode")
sudo usermod -aG docker-host "$USER"
