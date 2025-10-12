# OMZ Plugin Setup Tool Specification

## Overview

The OMZ Plugin Setup Tool is a general-purpose command-line tool that automates the installation and activation of Oh My Zsh plugins from GitHub repositories or custom Git URIs. The tool downloads plugins as Git submodules and automatically enables them in the user's `.zshrc` configuration.

## Purpose

- **Primary Function**: Install Oh My Zsh plugins from GitHub or custom Git repositories
- **Secondary Function**: Automatically enable installed plugins in the user's zsh configuration
- **Target Audience**: Developers using Oh My Zsh who want to streamline plugin installation

## Usage

### Installation

Run the installation script to create a symlink in your PATH:

```bash
./install.zsh
```

This creates a symlink from `run.zsh` to a directory in your `$PATH`, renaming it to `setup-omz-plugins` during the process. After installation, the tool will be available system-wide as `setup-omz-plugins`.

#### Installation Options

```bash
./install.zsh [OPTIONS]
```

**Options:**

- `--prefix <directory>`: Install to specified directory (default: `~/.local/bin`)
- `--create-dirs`: Create installation directory if it doesn't exist

**Examples:**

```bash
# Default installation to ~/.local/bin
./install.zsh

# Install to custom directory
./install.zsh --prefix /usr/local/bin

# Install to custom directory, creating it if needed
./install.zsh --prefix ~/mytools/bin --create-dirs
```

### Basic Syntax

```bash
setup-omz-plugins [--no-enable] [--from-string <plugin-list>] [<repo/plugin> ...]
```

### Arguments

- `--no-enable`: Skip enabling plugins in `.zshrc` after installation (download only)
- `--from-string <plugin-list>`: Accept plugins from a space-separated string (useful for automation and environment variables)

### Examples

```bash
# Install single plugin using GitHub shorthand
setup-omz-plugins zsh-users/zsh-autosuggestions

# Install multiple plugins
setup-omz-plugins zsh-users/zsh-autosuggestions \
                  zsh-users/zsh-syntax-highlighting

# Install from custom Git URI
setup-omz-plugins https://gitlab.com/user/custom-plugin.git

# Install plugins from string (useful for automation)
setup-omz-plugins --from-string "zsh-users/zsh-autosuggestions zsh-users/zsh-syntax-highlighting"

# Install from environment variable
setup-omz-plugins --from-string "${PLUGINS_LIST}"

# Download plugins without enabling them
setup-omz-plugins --no-enable zsh-users/zsh-autosuggestions \
                              zsh-users/zsh-syntax-highlighting

# Download from string without enabling
setup-omz-plugins --no-enable --from-string "${PLUGINS_LIST}"

# Development usage (before installation)
./run.zsh zsh-users/zsh-autosuggestions
```

## Plugin Format Support

### GitHub Shorthand Format

- **Pattern**: `<organization>/<repository>`
- **Example**: `zsh-users/zsh-autosuggestions`
- **Resolves to**: `https://github.com/zsh-users/zsh-autosuggestions`

### Full URI Format

- **HTTP/HTTPS**: `https://github.com/user/repo.git`
- **SSH**: `git@gitlab.com:user/repo.git`
- **Use Case**: Non-GitHub repositories (GitLab, Bitbucket, etc.)

## Technical Implementation

### Dependencies

- **Required**: `git`, `zsh`
- **Validation**: Tool exits with error code 1 if dependencies are missing
- **Environment Requirements**:
  - `$ZSH_CUSTOM/plugins` directory must exist
  - `.zshrc` file must exist and contain a `plugins=()` line

### Installation Process

1. **Download Phase**:
   - Changes directory to `$ZSH_CUSTOM/plugins`
   - Executes `git submodule add -f <repository_uri>`
   - Plugin name extracted from repository path (everything after last `/`)

2. **Activation Phase** (skipped if `--no-enable` flag is used):
   - Parses existing `plugins=()` line from `.zshrc`
   - Appends plugin name to plugins array
   - Updates `.zshrc` with modified plugins line
   - Creates backup file (`.zshrc.bak`) during modification

### Error Handling

- **Batch Processing**: If one plugin fails, continues with remaining plugins
- **Logging**: Colored output with different log levels (INFO, SUCCESS, WARNING, ERROR)
- **Graceful Degradation**: Shows specific error messages and continues processing

## File System Behavior

### Plugin Storage Location

```bash
${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/plugins
```

- Uses `$ZSH_CUSTOM` if set, otherwise defaults to `$HOME/.oh-my-zsh/custom`
- Each plugin installed as a subdirectory named after the repository

### Configuration File Modification

```bash
${ZDOTDIR:-$HOME}/.zshrc
```

- Uses `$ZDOTDIR/.zshrc` if set, otherwise `$HOME/.zshrc`
- Modifies the `plugins=()` line using regex pattern matching
- Creates backup before modification

## Integration Points

### Oh My Zsh Ecosystem

- **Plugin Discovery**: Installed plugins appear in `omz plugin list`
- **Manual Management**: Plugins can be managed with `omz plugin enable/disable <name>`
- **Standard Location**: Uses Oh My Zsh's standard plugin directory structure

### Git Submodule Strategy

- **Rationale**: Avoids conflicts when `$ZSH_CUSTOM` is already a Git repository
- **Benefit**: Maintains proper Git history and enables easy updates
- **Command**: `git submodule add -f <uri>`

## Output and Logging

### Log Levels

- **INFO** (Blue): General operation information
- **SUCCESS** (Green): Successful plugin installation
- **WARNING** (Yellow): Non-critical issues (duplicate plugins, failures)
- **ERROR** (Red): Critical failures requiring user attention

### Color Codes

```bash
BOLD_RED=$'\033[1;31m'
BOLD_GREEN=$'\033[1;32m'
BOLD_YELLOW=$'\033[1;33m'
BOLD_BLUE=$'\033[1;34m'
NC=$'\033[0m'  # No Color
```

## Configuration Parsing

### Plugin Line Format

- **Expected Pattern**: `^plugins=\(.*\)$`
- **Example**: `plugins=(git docker zsh-autosuggestions)`
- **Modification Strategy**: String replacement using `sed`

### Array Manipulation

- **Serialization**: Converts zsh array to space-separated string in parentheses
- **Deserialization**: Parses parenthesized string back to array elements
- **Append Logic**: Adds new plugin name to existing array

## Error Conditions

### Pre-execution Validation

- Missing `git` command
- Missing `zsh` command
- Non-existent `$ZSH_CUSTOM/plugins` directory
- Non-existent `.zshrc` file

### Runtime Errors

- Invalid repository URI
- Network connectivity issues during `git submodule add`
- Missing `plugins=()` line in `.zshrc`
- File permission issues during `.zshrc` modification

## Shell Script Architecture

### Source Files

- **run.zsh**: Main script with argument parsing, validation, and plugin installation logic
- **install.zsh**: Installation script with `--prefix` and `--create-dirs` options for flexible installation to user-specified directories

### Function Organization

- **Logging**: `log::info`, `log::success`, `log::warning`, `log::error`
- **Validation**: `check_dependencies`, `show_environment`
- **Plugin Operations**: `plugins::*` namespace functions
- **Configuration**: `zshrc::*` namespace functions
- **Utilities**: `array::*` namespace functions

### Script Options

```bash
set -euo pipefail
```

- **`-e`**: Exit on any command failure
- **`-u`**: Exit on undefined variable usage
- **`-o pipefail`**: Exit on pipeline failures

## Use Cases for AI Assistants

### Implementation Assistance

- Understanding the modular function architecture
- Extending functionality (e.g., plugin removal, updates)
- Debugging installation failures
- Adding support for additional Git hosting services

### User Support

- Troubleshooting installation errors
- Explaining plugin activation process
- Guiding users through manual `.zshrc` fixes
- Recommending popular plugins for installation

### Automation Integration

- Incorporating into development environment setup scripts
- Batch installation for team standardization
- Integration with dotfiles management systems
- CI/CD pipeline usage for consistent environments

## Limitations and Considerations

- **Single Plugin Line**: Assumes `.zshrc` has exactly one `plugins=()` line
- **Bash Arrays**: Uses zsh-specific array syntax for plugin list manipulation
- **No Conflict Resolution**: Does not handle plugin name conflicts
- **No Version Management**: Always installs latest version from default branch
- **No Uninstall**: Tool only handles installation, not removal
