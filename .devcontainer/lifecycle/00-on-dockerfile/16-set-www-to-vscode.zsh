#!/usr/bin/env zsh

# Set the user to 'vscode' if not already set
[ -z "$USER" ] && USER=$(whoami 2>/dev/null || echo "vscode")

# Add vscode user to www-data group
sudo usermod -aG www-data "$USER"
