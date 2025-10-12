# enable-config-dir Tool

## Overview

The `enable-config-dir` tool transforms any user directory into a system-like configuration directory that automatically loads on new shell sessions. Instead of cramming everything into your `.zshrc` file, this tool lets you choose any directory (or multiple directories) to become modular configuration sources - just like having multiple `.zshrc` files organized in directories.

## Purpose

- **Primary Function**: Transform ordinary directories into configuration directories that auto-load on shell startup
- **Secondary Function**: Enable modular shell configuration using directories instead of monolithic files
- **User Benefit**: Choose your own directory structure for shell configuration - personal dotfiles, project configs, team shared settings
- **Target Audience**: Developers using Oh My Zsh who want to organize shell configuration in directories rather than single files

## Usage

### Installation

Run the installation script to create a symlink in your PATH:

```bash
./install.zsh
```

This creates a symlink from `run.zsh` to a directory in your `$PATH`, renaming it to `enable-config-dir` during the process. After installation, the tool will be available system-wide as `enable-config-dir`.

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
enable-config-dir <path>
```

### Arguments

- `<path>`: Required. Directory path containing custom shell scripts to be auto-loaded (positional argument)

### Examples

```bash
# Transform your personal dotfiles directory into a config directory
enable-config-dir ~/.config/shell

# Make your project workspace auto-configure shells
enable-config-dir /workspace/custom-scripts

# Enable team shared configuration directory
enable-config-dir /shared/team-configs
```

**Result**: Any `.sh`, `.zsh`, or `.bash` files in these directories will automatically load in new shell sessions, just like they were part of your `.zshrc`.

## Script Format Support

### What Gets Auto-Loaded

Once you transform a directory into a configuration directory, any script files placed in it will automatically load on new shell sessions:

- **Shell Scripts**: `.sh` files
- **Zsh Scripts**: `.zsh` files
- **Bash Scripts**: `.bash` files
- **Discovery Pattern**: All files matching `"${custom_dir}/"*.{sh,zsh,bash}`

### User Workflow

1. **Install the tool**: Run `./install.zsh` (with optional `--prefix` and `--create-dirs` options) to create a system-wide symlink
2. **Choose any directory** for your shell configurations
3. **Run enable-config-dir** to transform it: `enable-config-dir /path/to/your/directory`
4. **Add shell scripts** to that directory (aliases, functions, exports, etc.)
5. **Open new shells** - your configurations automatically load

## Technical Implementation

### Dependencies

- **Required**: `envsubst`, `zsh`
- **Validation**: Tool exits with error if dependencies are missing or environment is invalid
- **Environment Requirements**:
  - `$ZSH_CUSTOM` environment variable must be set by Oh My Zsh
  - Oh My Zsh must be installed and configured

### Installation Process

1. **Validation Phase**:
   - Validates command line arguments (path argument required)
   - Checks for required dependencies (`envsubst`)
   - Verifies `$ZSH_CUSTOM` environment variable is set

2. **Template Processing Phase**:
   - Generates directory-specific hash using MD5 of absolute path
   - Sets `CUSTOM_DIR` template variable from user argument
   - Processes `loader.zsh.template` with `envsubst`
   - Creates final autoloader script with unique filename

3. **Installation Phase**:
   - Outputs processed template to `${ZSH_CUSTOM}/custom-config-loader_${hash}.zsh`
   - Enables automatic loading on next shell session

### Error Handling

- **Batch Processing**: Individual script failures don't prevent loading remaining scripts
- **Argument Validation**: Displays usage message for missing or incorrect arguments
- **Dependency Checks**: Validates `envsubst` availability and template file existence
- **Silent Failures**: Missing target directories don't generate errors during runtime
- **Graceful Degradation**: File permission issues and syntax errors handled gracefully

## File System Behavior

### Autoloader Storage Location

```bash
${ZSH_CUSTOM}/custom-config-loader_${hash}.zsh
```

- Uses Oh My Zsh's `$ZSH_CUSTOM` directory for autoloader placement
- Hash-based naming prevents conflicts between multiple custom directories
- Each unique directory gets its own dedicated autoloader file

### Configuration Directory Location

```bash
${CUSTOM_DIR}
```

- User-specified directory containing custom shell scripts
- Supports absolute and relative paths (resolved to absolute during processing)
- Multiple directories can be configured with separate autoloaders

### Custom Script Discovery

```bash
"${custom_dir}/"*.{sh,zsh,bash}
```

- Searches for shell scripts in user-specified directory
- Supports `.sh`, `.zsh`, and `.bash` file extensions
- Uses glob patterns with `null_glob` option for safe empty directory handling

## Integration Points

### Oh My Zsh Ecosystem

- **Directory Convention**: Implements system-like configuration directories (similar to `/etc/profile.d/`) within Oh My Zsh
- **Automatic Discovery**: Oh My Zsh automatically sources all `.zsh` files in `$ZSH_CUSTOM` directory
- **Multiple Config Dirs**: Transform multiple directories - each gets its own autoloader, no conflicts
- **Load Order**: Depends on Oh My Zsh's file discovery order (typically alphabetical)
- **User Choice**: You decide which directories become configuration sources

### Template Processing Strategy

- **Rationale**: External template file maintains separation of concerns and improves maintainability
- **Benefit**: Clean substitution of user-provided directory paths using `envsubst`
- **Variables**: `${CUSTOM_DIR}` substituted with absolute path from positional argument

### Filename Generation Algorithm

- **Method**: MD5 hash of absolute directory path (via `realpath`)
- **Truncation**: Last 9 characters of MD5 hash for filename suffix
- **Collision Resistance**: 36^9 possible combinations provide sufficient uniqueness
- **Deterministic**: Same directory always generates same loader filename, enabling safe re-installation

## Output and Logging

### File Generation

- **Template Source**: `loader.zsh.template`
- **Main Script**: `run.zsh` (symlinked as `enable-config-dir`)
- **Output Location**: `${ZSH_CUSTOM}/custom-config-loader_${hash}.zsh`
- **Processing**: `envsubst` variable substitution

### Runtime Behavior

- **Silent Operation**: No output during normal autoloader execution
- **Error Suppression**: Missing directories and unreadable files fail silently
- **Graceful Handling**: Individual script failures don't prevent loading remaining scripts

### Installation Feedback

- **Success Indication**: Successful autoloader creation and installation
- **Error Messages**: Clear indication of validation failures and missing dependencies
- **Path Information**: Display of target directory and generated autoloader location

## Configuration Processing

### Template Variables

- **CUSTOM_DIR**: User-provided directory path from positional argument
- **Substitution Method**: `envsubst` command processes template file
- **Output Generation**: Creates Oh My Zsh-compatible autoloader script

### File Discovery Logic

- **Core Function**: `load_custom_dir()` in generated autoloader
- **Safety Checks**: Directory existence and readability validation before processing
- **Glob Pattern**: `"${custom_dir}/"*.{sh,zsh,bash}` with `null_glob` option
- **Processing**: Source each readable file found in directory

## Error Conditions

### Pre-execution Validation

- Missing path argument
- Missing `envsubst` utility
- Undefined `$ZSH_CUSTOM` environment variable
- Missing `loader.zsh.template` file

### Runtime Errors

- Invalid directory path provided as argument
- File permission issues during autoloader creation
- Template processing failures
- Syntax errors in template file

## Shell Script Architecture

### Source Files

- **run.zsh**: Main installation script with argument parsing and template processing
- **install.zsh**: Installation script with `--prefix` and `--create-dirs` options for flexible installation to user-specified directories
- **loader.zsh.template**: Template for runtime autoloader with `${CUSTOM_DIR}` placeholder

### Generated Components

- **custom-config-loader_${hash}.zsh**: Final autoloader script in Oh My Zsh custom directory
- **load_custom_dir()**: Core function that handles directory scanning and script sourcing

### Function Organization

- **Template Processing**: Main setup script with argument parsing and validation
- **File Generation**: Template variable substitution and autoloader creation
- **Path Utilities**: Directory resolution and hash generation functions
- **Validation**: Dependency checks and environment validation
- **Installation Management**: Symlink creation and PATH integration via `install.zsh`

### Script Options

```bash
set -euo pipefail
```

- **`-e`**: Exit on any command failure
- **`-u`**: Exit on undefined variable usage
- **`-o pipefail`**: Exit on pipeline failures

## Use Cases for AI Assistants

### Implementation Assistance

- Understanding the template processing workflow
- Extending functionality for additional file types or processing rules
- Debugging installation or runtime failures
- Adding validation for custom directory contents

### User Support

- Troubleshooting autoloader installation issues
- Explaining the hash-based naming system
- Guiding users through custom script organization
- Helping with Oh My Zsh integration concepts

### Automation Integration

- Incorporating into dotfiles management systems
- Setting up team-wide custom configuration standards
- Integration with development environment automation
- CI/CD pipeline usage for consistent shell environments

## Limitations and Considerations

- **Oh My Zsh Dependency**: Requires Oh My Zsh installation and `$ZSH_CUSTOM` environment variable
- **Template Dependency**: Assumes `loader.zsh.template` file exists alongside setup script
- **No Validation**: Does not validate contents of custom directory or individual scripts
- **Silent Failures**: Missing directories and script errors fail silently during runtime
- **No Uninstall**: Tool only handles installation, not removal of autoloaders
