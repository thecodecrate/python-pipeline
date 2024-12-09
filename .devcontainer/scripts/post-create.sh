#!/usr/bin/zsh

# Set WORKSPACE_DIR
export WORKSPACE_DIR="$PWD"
echo "export WORKSPACE_DIR='$WORKSPACE_DIR'" >> $HOME/.zshrc

# Install virtual environment
export UV_CACHE_DIR="$PWD/.uv_cache"
uv sync --frozen

# Show a "dirty" indicator in the prompt if the workspace is dirty
git config devcontainers-theme.show-dirty 1

# UV/UVX auto-completion
echo 'eval "$(uv generate-shell-completion bash)"' >> ~/.bashrc
echo 'eval "$(uv generate-shell-completion zsh)"' >> ~/.zshrc
echo 'eval "$(uvx --generate-shell-completion bash)"' >> ~/.bashrc
echo 'eval "$(uvx --generate-shell-completion zsh)"' >> ~/.zshrc
