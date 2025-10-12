#!/usr/bin/env zsh
#
# Switch APT repository mirrors in Debian-based systems.
#
# Usage:
#   sudo ./run.zsh [OPTIONS] <new_mirror>
#   sudo ./run.zsh --type deb mirrors.kernel.org
#   sudo ./run.zsh --suite security security.ubuntu.com
#   sudo ./run.zsh --no-backup test-mirror.example.com
#
# Options:
#   --type [deb|deb-src|all]
#       Filter by repository type (default: all)
#   --suite [updates|backports|security|main|all]
#       Filter by distribution suite (default: all)
#   --no-backup
#       Skip backup creation
#   --no-update
#       Skip running 'apt update' after switching mirrors
#
# Notes:
#   - Replaces mirror URLs while preserving all other repository metadata.
#   - Processes /etc/apt/sources.list only (not sources.list.d files).
#   - Creates timestamped backups by default unless --no-backup is specified.
#   - Script must be run with sudo privileges.
#

set -euo pipefail

# Global variables
SELF_PATH="$(readlink -f -- "${(%):-%N}")"
readonly SELF_PATH

SELF_DIR="$(cd -- "$(dirname -- "${SELF_PATH}")" && pwd)"
readonly SELF_DIR


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

show_environment() {
  log::info "About to switch APT repository mirrors with args:\n" \
    "$*"
}

check_dependencies() {
  if ! command -v awk > /dev/null 2>&1; then
    log::error "awk is required to process sources.list."
    exit 1
  fi
}

check_environment() {
  if [[ "$EUID" -ne 0 ]]; then
    log::error "Please run the script with sudo."
    exit 1
  fi
}

parse_arguments() {
  local type="all"
  local suite="all"
  local no_backup=0
  local no_update=0

  while [[ $# -gt 0 ]]; do
    case "$1" in
      --type)
        type="$2"
        shift 2
        ;;
      --suite)
        suite="$2"
        shift 2
        ;;
      --no-backup)
        no_backup=1
        shift
        ;;
      --no-update)
        no_update=1
        shift
        ;;
      -*)
        log::error "Unknown option: $1"
        exit 1
        ;;
      *)
        new_provider="$1"
        shift
        ;;
    esac
  done

  if [[ -z "${new_provider:-}" ]]; then
    log::error "<new_provider> is required."
    exit 1
  fi

  echo "$type" "$suite" "$no_backup" "$no_update" "$new_provider"
}

sources_file::backup() {
  local src="/etc/apt/sources.list"
  local symlink="/etc/apt/sources.list.backup"

  local backup_file
  backup_file="/etc/apt/sources.list.backup.$(date +%Y%m%d_%H%M%S)"

  if ! cp --preserve=all "${src}" "${backup_file}"; then
    log::error "Failed to create backup at ${backup_file}"
    exit 1
  fi

  ln -sf "${backup_file}" "${symlink}"
}

sources_file::replace_entry_uri() {
  local type="$1"
  local suite="$2"
  local new_uri="$3"

  awk -v type_match="$type" -v suite_match="$suite" -v new_uri="$new_uri" \
    -f "${SELF_DIR}/replace_entry_uri.awk"
}

sources_file::process() {
  local type="$1"
  local suite="$2"
  local new_provider="$3"
  local src="/etc/apt/sources.list"

  local tmp
  tmp="$(mktemp "${src}.XXXXXX")"

  if ! sources_file::replace_entry_uri "${type}" "${suite}" "${new_provider}" < "${src}" > "${tmp}"; then
    log::error "Failed to process ${src}."
    rm -f "${tmp}"
    exit 1
  fi

  if ! mv "${tmp}" "${src}"; then
    log::error "Failed to update ${src}."
    rm -f "${tmp}"
    exit 1
  fi
}

apt::update() {
  if ! apt-get update; then
    log::error "Failed to run 'apt update'. Please check your sources.list."
    exit 1
  fi
}

main() {
  show_environment "$@"

  check_dependencies

  check_environment

  # Parse arguments and assign to variables
  read -r type suite no_backup no_update new_provider < <(parse_arguments "$@")

  if [[ "${no_backup}" -eq 0 ]]; then
    sources_file::backup
  fi

  sources_file::process "${type}" "${suite}" "${new_provider}"

  if [[ "${no_update}" -eq 0 ]]; then
    apt::update
  fi

  log::success "Successfully switched APT repository mirrors to ${new_provider}."
}

main "$@"
