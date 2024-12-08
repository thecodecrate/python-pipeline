#!/usr/bin/zsh

# Set WORKSPACE_DIR
echo "export WORKSPACE_DIR='$PWD'" >> $HOME/.zshrc

# Install virtual environment
export UV_CACHE_DIR="$PWD/.uv_cache"
uv sync
