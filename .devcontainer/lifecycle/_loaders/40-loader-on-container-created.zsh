#!/usr/bin/env zsh
# vim: set ft=zsh:
#
# Executes scripts from "40-on-container-created" directory
#
# This script loads and executes all shell scripts (.sh, .zsh, .bash)
# from the 40-on-container-created directory after container creation.
#

# Libraries
source "${WORKSPACE_DIR}/.devcontainer/lifecycle/_lib/loaders.zsh"

# Globals
DIR_PATH="${WORKSPACE_DIR}/.devcontainer/lifecycle/40-on-container-created"

# Main logic
execute_dir "${DIR_PATH}"

exit 0