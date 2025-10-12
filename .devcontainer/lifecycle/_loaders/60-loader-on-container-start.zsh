#!/usr/bin/env zsh
# vim: set ft=zsh:
#
# Executes scripts from "60-on-container-start" directory
#
# This script loads and executes all shell scripts (.sh, .zsh, .bash)
# from the 60-on-container-start directory when the container starts.
#

# Libraries
source "${WORKSPACE_DIR}/.devcontainer/lifecycle/_lib/loaders.zsh"

# Globals
DIR_PATH="${WORKSPACE_DIR}/.devcontainer/lifecycle/60-on-container-start"

# Main logic
execute_dir "${DIR_PATH}"

exit 0