#!/usr/bin/env zsh
# This script installs uv/uvx, required for `.vscode/mcp.json`

# Dowload and install uv
curl -LsSf https://astral.sh/uv/install.sh | sh

# Auto-completion
echo 'eval "$(uv generate-shell-completion zsh)"' >> ~/.zshrc
echo 'eval "$(uvx --generate-shell-completion zsh)"' >> ~/.zshrc
