#!/usr/bin/env zsh
# This script installs Claude CLI

set -euo pipefail

# npx @anthropic-ai/claude-code install --force
curl -fsSL https://claude.ai/install.sh | bash

# Tool needed for some MCP servers
# npm install -g mcp-remote

exit 0
