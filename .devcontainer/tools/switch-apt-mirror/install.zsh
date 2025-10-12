#!/usr/bin/env zsh
#
# Installs the switch-apt-mirror tool by creating a symlink from run.zsh to
# a directory in the user's PATH. This makes the tool available system-wide
# without requiring manual alias configuration.
#
# Usage:
#   ./install.zsh [OPTIONS]
#   ./install.zsh --prefix ~/.local/bin
#   ./install.zsh --prefix /usr/local/bin --create-dirs
#
# Options:
#   --prefix <directory>
#       Install to specified directory (default: ~/.local/bin)
#   --create-dirs
#       Create installation directory if it doesn't exist
#
# Notes:
# - Overwrites existing installation if present
# - Requires installation directory to be in user's PATH for system-wide access
# - Creates symlink preserving original script location

set -euo pipefail

# Global variables
SELF_DIR="$(cd -- "$(dirname -- "$0")" && pwd)"

SRC_SCRIPT_NAME="run.zsh"
DEST_SCRIPT_NAME="switch-apt-mirror"
DEFAULT_DEST_DIR="${HOME}/.local/bin"
SRC_SCRIPT_PATH="${SELF_DIR}/${SRC_SCRIPT_NAME}"

parse_arguments() {
  local dest_dir
  local create_dirs

  # Default values
  dest_dir="${DEFAULT_DEST_DIR}"
  create_dirs="false"

  while [[ $# -gt 0 ]]; do
    case "$1" in
      --prefix)
        if [[ -n "${2:-}" ]]; then
          dest_dir="$2"
          shift 2
        else
          echo "Error: --prefix requires a path argument" >&2
          exit 2
        fi
        ;;
      --create-dirs)
        create_dirs="true"
        shift
        ;;
      -*)
        echo "Error: Unknown option: $1" >&2
        exit 1
        ;;
      *)
        break
        ;;
    esac
  done

  echo "${dest_dir} ${create_dirs}"
}

check_environment() {
  if [[ ! -f "${SRC_SCRIPT_PATH}" ]]; then
    echo "Error: ${SRC_SCRIPT_PATH} not found" >&2
    exit 1
  fi
}

# @param $1   string $dest_dir. The destination directory where the script will be installed
# @param $2   string $create_dirs. If "true", create the directory if it doesn't exist
# @return     void
# @exits      1 if the directory does not exist and create_dirs is false
#             2 if the directory is not writable
#             3 if the directory cannot be created
ensure_dest_dir() {
  local dest_dir="$1"
  local create_dirs="$2"

  if [[ ! -d "${dest_dir}" ]]; then
    if [[ "${create_dirs}" == "true" ]]; then
      echo "Creating destination directory: ${dest_dir}"
      if ! mkdir -p "${dest_dir}"; then
        echo "Error: Failed to create directory ${dest_dir}" >&2
        exit 3
      fi
    else
      echo "Error: Directory ${dest_dir} does not exist. Use --create-dirs to create it automatically." >&2
      exit 1
    fi
  fi

  if [[ ! -w "${dest_dir}" ]]; then
    echo "Error: Destination directory ${dest_dir} is not writable." >&2
    exit 2
  fi
}

# @param $1   string $src_path. The source script path to symlink
# @param $2   string $dest_path. The destination path where the symlink will be created
# @return     void
# @exits      1 if the symlink creation fails
tool::install() {
  local src_path="$1"
  local dest_path="$2"

  if [[ -e "${dest_path}" ]]; then
    echo "Warning: ${dest_path} already exists. Overwriting..."
  fi

  if ! ln -sf "${src_path}" "${dest_path}"; then
    echo "Error: Failed to create symlink from ${src_path} to ${dest_path}" >&2
    exit 1
  fi
}

main() {
  # Parse arguments and assign to variables
  local dest_dir
  local create_dirs
  read -r dest_dir create_dirs < <(parse_arguments "$@")

  local dest_script_path
  dest_script_path="${dest_dir}/${DEST_SCRIPT_NAME}"

  check_environment

  ensure_dest_dir "${dest_dir}" "${create_dirs}"

  tool::install "${SRC_SCRIPT_PATH}" "${dest_script_path}"

  echo "Installed ${DEST_SCRIPT_NAME} to ${dest_script_path}"
}

main "$@"
