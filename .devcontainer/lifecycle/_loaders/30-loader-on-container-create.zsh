#!/usr/bin/env zsh
# vim: set ft=zsh:
#
# Executes scripts from "30-on-container-create" directory
#
# This script loads and executes all shell scripts (.sh, .zsh, .bash)
# from the 30-on-container-create directory during container creation.
#

# Libraries
source "${WORKSPACE_DIR}/.devcontainer/lifecycle/_lib/loaders.zsh"

# Globals
DIR_PATH="${WORKSPACE_DIR}/.devcontainer/lifecycle/30-on-container-create"

# Main logic
execute_dir "${DIR_PATH}"

exit 0
