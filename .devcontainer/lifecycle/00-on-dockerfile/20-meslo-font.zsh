#!/usr/bin/env zsh
#
# Download and install Meslo fonts
#
# Note: Font is already set up in `.vscode/settings.json`
#

# Download Meslo fonts
wget https://github.com/romkatv/powerlevel10k-media/raw/master/MesloLGS%20NF%20Regular.ttf -P "${HOME}/.local/share/fonts"
wget https://github.com/romkatv/powerlevel10k-media/raw/master/MesloLGS%20NF%20Bold.ttf -P "${HOME}/.local/share/fonts"
wget https://github.com/romkatv/powerlevel10k-media/raw/master/MesloLGS%20NF%20Italic.ttf -P "${HOME}/.local/share/fonts"
wget https://github.com/romkatv/powerlevel10k-media/raw/master/MesloLGS%20NF%20Bold%20Italic.ttf -P "${HOME}/.local/share/fonts"

# Update font cache
sudo apt install -y fontconfig

fc-cache -fv "${HOME}/.local/share/fonts"
