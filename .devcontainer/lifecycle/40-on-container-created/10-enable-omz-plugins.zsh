#!/usr/bin/env zsh
# vim: set ft=zsh:

#
# Setup Oh My Zsh plugins
# Enables commonly used Oh My Zsh plugins for development workflow.
#


# Source rc for `omz` command
# shellcheck source=/dev/null
source "${HOME}/.zshrc"

# Enable OMZ plugins
omz plugin enable asdf
omz plugin enable docker
omz plugin enable docker-compose

exit 0
