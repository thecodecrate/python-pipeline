#!/usr/bin/env zsh

# Wait for Docker to be ready
while ! docker info >/dev/null 2>&1; do
  echo "Waiting for Docker to be ready..."
  sleep 1
done

# Set container hostnames in /etc/hosts
sudo $WORKSPACE_DIR/.devcontainer/tools/set-docker-subhosts/run.zsh

exit 0
