#!/usr/bin/env zsh
# vim: set ft=zsh:
#
# Executes scripts from "00-on-dockerfile" directory
#
# This script loads and executes all shell scripts (.sh, .zsh, .bash)
# from the 00-on-dockerfile directory during Dockerfile build process.
#

# Globals
DIR_PATH="${WORKSPACE_DIR}/.devcontainer/lifecycle/00-on-dockerfile"

# Libraries
source "${WORKSPACE_DIR}/.devcontainer/lifecycle/_lib/loaders.zsh"

# Main logic
execute_dir "${DIR_PATH}"

exit 0
