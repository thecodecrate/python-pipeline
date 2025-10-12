#!/usr/bin/env zsh
# vim: set ft=sh:

# Install HADOLINT
HADOLINT_URL=https://github.com/hadolint/hadolint/releases/download/v2.12.0/hadolint-Linux-x86_64

sudo wget -q -O /usr/local/bin/hadolint "$HADOLINT_URL"
sudo chmod +x /usr/local/bin/hadolint
