#!/usr/bin/env zsh
# Oh My Zsh plugin setup tool that downloads plugins from GitHub or custom Git
# repositories and automatically enables them in .zshrc configuration.
#
# Usage:
#   ./run.zsh [--no-enable] [--from-string <plugin-list>] [<repo/plugin> ...]
#   ./run.zsh zsh-users/zsh-autosuggestions \
#             zsh-users/zsh-syntax-highlighting
#   ./run.zsh --from-string "zsh-users/zsh-autosuggestions zsh-users/zsh-syntax-highlighting"
#   ./run.zsh --from-string "${PLUGINS_LIST}"
#   ./run.zsh --no-enable https://gitlab.com/user/custom-plugin.git
#
# Options:
#   --no-enable
#       Skip enabling plugins in .zshrc after installation (download only)
#   --from-string <plugin-list>
#       Accept plugins from a space-separated string (useful for automation)
#
# Notes:
#   - Supports GitHub shorthand format (org/repo) or full Git URIs
#   - Downloads plugins as Git submodules to avoid conflicts
#   - Automatically appends plugins to existing plugins=() line in .zshrc
#   - Creates .zshrc.bak backup before making changes
#   - Continues processing remaining plugins if one fails

set -euo pipefail

# Global variables
PLUGIN_DIRS="${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/plugins"
readonly PLUGIN_DIRS

ZSHRC="${ZDOTDIR:-$HOME}/.zshrc"
readonly ZSHRC


{ # Colors
  BOLD_RED=$'\033[1;31m'
  BOLD_GREEN=$'\033[1;32m'
  BOLD_YELLOW=$'\033[1;33m'
  BOLD_BLUE=$'\033[1;34m'
  NC=$'\033[0m'
}

{ # Logging functions
  log::info() {
    echo -e "${BOLD_BLUE}[INFO]${NC} $*" >&2
  }

  log::success() {
    echo -e "${BOLD_GREEN}[SUCCESS]${NC} $*" >&2
  }

  log::warning() {
    echo -e "${BOLD_YELLOW}[WARNING]${NC} $*" >&2
  }

  log::error() {
    echo -e "${BOLD_RED}[ERROR]${NC} $*" >&2
  }
}

# @param $@   string[] $args
show_environment() {
  log::info "About to setup zsh plugins on ${PLUGIN_DIRS} with args:\n" \
    "$*"
}

# @param $@   string[] $args
# @return     string[] $plugins (remaining arguments after flags)
parse_arguments() {
  local plugins=()
  local enable_plugins="true"
  local from_string=""

  while [[ $# -gt 0 ]]; do
    case "$1" in
      --no-enable)
        enable_plugins="false"
        shift 1
        ;;
      --from-string)
        from_string="$2"
        shift 2
        ;;
      -* )
        log::error "Unknown option: $1"
        exit 1
        ;;
      *)
        plugins+=("$1")
        shift 1
        ;;
    esac
  done

  if [[ -n "$from_string" ]]; then
    local from_string_plugins=( ${(z)from_string} )
    plugins+=("${from_string_plugins[@]}")
  fi

  # Print enable_plugins and plugins as a single line, plugins space-separated
  printf '%s ' "$enable_plugins"
  printf '%s ' "${plugins[@]}"
  printf '\n'
}

check_dependencies() {
  if ! command -v git > /dev/null 2>&1; then
    log::error "git is required to setup omz plugins."
    exit 1
  fi

  if ! command -v zsh > /dev/null 2>&1; then
    log::error "zsh is required to setup omz plugins."
    exit 1
  fi
}

check_environment() {
    if [[ ! -d "${PLUGIN_DIRS}" ]]; then
    log::error "PLUGIN_DIRS directory does not exist: ${PLUGIN_DIRS}"
    exit 1
  fi

  if [[ ! -f "${ZSHRC}" ]]; then
    log::error "ZSHRC file does not exist: ${ZSHRC}"
    exit 1
  fi
}

# @param $1   string $serialized_list, e.g. "plugins=(plugin1 plugin2)"
# @param $2   string $item, e.g. "new_plugin"
# @return     string serialized list with item appended,
#                    e.g. "plugins=(plugin1 plugin2 new_plugin)"
array::append_item_to_serialized_list() {
  local item="$1"
  local serialized_list="$2"

  local list_name
  local new_list
  local new_serialized

  # Extract the list name (everything before the '=')
  list_name="${serialized_list%%=*}"

  # Unserialize by removing the list name and parenthesis
  new_list=("${(s: :)${serialized_list#*=\(}}")  # Split by spaces, removing the 'var=(' part
  new_list=("${new_list[@]%)}")                  # Remove trailing parenthesis

  # Append new item
  new_list=("${new_list[@]}" "$item")

  # Serialize back to line using the extracted list name
  new_serialized="${list_name}=(${(j: :)new_list})"

  echo "$new_serialized"
}

# @param $1   string $zshrc_path, e.g. "$HOME/.zshrc"
# @return     string The plugins line/block, e.g. "plugins=(plugin1 plugin2)"
# @exits      1 if no plugins line found
zshrc::extract_plugins_line() {
  local zshrc_path="$1"

  local plugins_line
  plugins_line=$(grep -E '^plugins=\(' "$zshrc_path" || true)

  if [[ -z "$plugins_line" ]]; then
    return 1
  fi

  echo "$plugins_line"
}

# @param $1   string $plugins_line, e.g. "plugins=(plugin1 plugin2)"
# @param $2   string $zshrc_path, e.g. "$HOME/.zshrc"
# @exits      1 if plugins line format is invalid
#             2 if update failed
zshrc::update_plugins_line() {
  local plugins_line="$1"
  local zshrc_path="$2"

  # Ensure the plugins line is properly formatted
  if [[ ! "$plugins_line" =~ ^plugins=\(.*\)$ ]]; then
    log::error "Invalid plugins line format: $plugins_line"
    return 1
  fi

  # Replace the existing plugins line in .zshrc
  if ! sed -i.bak "s/^plugins=.*/$plugins_line/" "$zshrc_path"; then
    return 2
  fi
}

# @param $1   string $plugin
# @param $2   string $zshrc_path, e.g. "$HOME/.zshrc"
# @exits      1 if no plugins line found
#             2 if update failed
zshrc::enable_plugin() {
  local plugin="$1"
  local zshrc_path="$2"

  local plugin_name
  plugin_name="${plugin##*/}"

  log::info "Enabling plugin '$plugin_name' in .zshrc"

  local plugins_line
  if ! plugins_line=$(zshrc::extract_plugins_line "$zshrc_path"); then
    log::error "No plugins line found in .zshrc. Please add 'plugins=(...)' to your .zshrc file."
    return 1
  fi

  if [[ "$plugins_line" =~ $plugin_name ]]; then
    log::warning "Plugin '$plugin_name' is already enabled in .zshrc."
    return 0
  fi

  plugins_line=$(array::append_item_to_serialized_list "$plugin_name" "$plugins_line")

  if ! $(zshrc::update_plugins_line "$plugins_line" "$zshrc_path"); then
    log::error "Failed to update .zshrc with plugin '$plugin_name'."
    return 2
  fi
}

# @param $1   string $plugin
# @exit       0 if plugin is a URI, 1 otherwise
plugins::is_uri() {
  local plugin="$1"
  [[ "$plugin" =~ ^https?:// ]] || [[ "$plugin" =~ ^git@ ]]
}

# @param $1   string $plugin
# @return     string repository URL
plugins::get_repo_uri() {
  local plugin="$1"

  if plugins::is_uri "$plugin"; then
    echo "$plugin"
  else
    echo "https://github.com/$plugin"
  fi
}

# @param $1   string $plugin
# @exits      1 if plugin couldn't be downloaded
plugins::download() {
  local plugin="$1"

  local plugin_name
  plugin_name="${plugin##*/}"

  local repo_uri
  repo_uri=$(plugins::get_repo_uri "${plugin}")

  log::info "Downloading plugin: ${repo_uri}"

  cd "$PLUGIN_DIRS"

  if ! git submodule add -f "${repo_uri}"; then
    log::error "Failed to download plugin: $plugin"
  fi
}

# @param $1   string enable_plugins. If "true", enable the plugin in .zshrc
# @param $2   string plugin. The plugin name or repository URL
# @exits      1 if plugin couldn't be downloaded
plugins::install_single() {
  local enable_plugins="$1"
  local plugin="$2"

  if ! plugins::download "${plugin}"; then
    return 1
  fi

  if [[ "$enable_plugins" == "true" ]]; then
    zshrc::enable_plugin "${plugin}" "${ZSHRC}"
  fi
}

# @param $1   string enable_plugins
# @param $@   string[] plugins
plugins::install_list() {
  local enable_plugins="$1"
  shift 1
  local plugins=("$@")

  if [[ ${#plugins[@]} -eq 0 ]]; then
    log::warning "No plugins specified for installation."
    return 0
  fi

  for plugin in "${plugins[@]}"; do
    log::info "Setting up plugin: ${plugin}"

    if plugins::install_single "$enable_plugins" "${plugin}"; then
      log::success "Installed: ${plugin}"
    else
      log::warning "Failed to install: ${plugin}"
    fi
  done
}

# @param $@   string[] $args
main() {
  # Parse command line arguments
  local enable_plugins
  local plugins_str
  local plugins

  read -r enable_plugins plugins_str < <(parse_arguments "$@")
  plugins=(${(z)plugins_str})

  show_environment "$@"

  check_dependencies

  check_environment

  plugins::install_list "${enable_plugins}" "${plugins[@]}"

  log::success "All specified plugins have been processed."
}

main $@
