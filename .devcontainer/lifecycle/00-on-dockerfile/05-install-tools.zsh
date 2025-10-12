#!/usr/bin/env zsh

# Globals
SRC_TOOLS_DIR="${WORKSPACE_DIR}/.devcontainer/tools"
DST_TOOLS_DIR="/usr/local/bin/devcontainer-tools"
SHARED_BIN_DIR="/usr/local/bin"

# Copy tools to the destination directory
sudo mkdir -p "${DST_TOOLS_DIR}"
sudo cp -r "${SRC_TOOLS_DIR}/." "${DST_TOOLS_DIR}/"
sudo chmod -R +x "${DST_TOOLS_DIR}/**/install.zsh"

# Install tools for dev container setup
sudo "${DST_TOOLS_DIR}/enable-config-dir/install.zsh" --prefix "${SHARED_BIN_DIR}" --create-dirs
sudo "${DST_TOOLS_DIR}/setup-omz-plugins/install.zsh" --prefix "${SHARED_BIN_DIR}" --create-dirs
sudo "${DST_TOOLS_DIR}/switch-apt-mirror/install.zsh" --prefix "${SHARED_BIN_DIR}" --create-dirs

# vim: set ft=sh:
