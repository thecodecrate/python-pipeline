#!/usr/bin/env zsh
# Functions for loading scripts

##
# Get list of executable script files from directory
#
# @param {string} dir_path - Directory to search for scripts
# @return {array} List of script files, or empty array if dir_path is invalid
#
# NOTES:
# - Only searches for files with .sh, .zsh, or .bash extensions
##
get_script_files() {
  setopt local_options null_glob
  local dir_path="$1"

  # Check if "dir_path" is not empty and the directory exists
  if [[ -z ${dir_path} ]] || [[ ! -d ${dir_path} ]]; then
    return
  fi

  # Find all scripts with .sh, .zsh, or .bash extensions in the directory
  local files=("${dir_path}/"*.{sh,zsh,bash})

  # If no files found, return
  if [[ ! -e ${files[1]} ]]; then
    return
  fi

  # Return the files array
  echo "${files[@]}"
}

##
# Execute scripts from the specified directory
#
# @param {string} dir_path - Directory containing scripts to execute
##
execute_dir() {
  local dir_path="$1"

  # Get list of script files from directory
  local files=($(get_script_files "${dir_path}"))

  # If no files found, return
  if [[ ${#files[@]} -eq 0 ]]; then
    return
  fi

  # Loop through each file and execute it if it exists and is readable
  for file in "${files[@]}"; do
    if [[ -e ${file} ]] && [[ -r ${file} ]]; then
      # shellcheck source=/dev/null
      zsh "${file}"
    fi
  done
}

##
# Source scripts from the specified directory
#
# @param {string} dir_path - Directory to source scripts from
##
source_dir() {
  local dir_path="$1"

  # Get list of script files from directory
  local files=($(get_script_files "${dir_path}"))

  # If no files found, return
  if [[ ${#files[@]} -eq 0 ]]; then
    return
  fi

  for file in "${files[@]}"; do
    if [[ -e ${file} ]] && [[ -r ${file} ]]; then
      # shellcheck source=/dev/null
      source "${file}"
    fi
  done
}
