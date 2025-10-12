# switch-apt-mirror Tool Specification

## Overview

A bash utility for safely switching APT repository mirrors in Debian-based systems. The tool replaces repository URLs while preserving all other source configuration details, providing automatic backup functionality, and automatically updating package lists after switching mirrors.

## Purpose

- **Primary Function**: Replace the URI component of APT source entries while maintaining all other repository metadata (type, options, distribution, suite, components)
- **Secondary Function**: Automatically update package lists and create backups for safe mirror switching
- **Target Audience**: System administrators and developers working with Debian-based systems who need to change APT mirrors efficiently

## Usage

### Installation

Run the installation script to create a symlink in your PATH:

```bash
./install.bash
```

This creates a symlink from `run.bash` to `~/.local/bin/switch-apt-mirror`. After installation, the tool will be available system-wide as `switch-apt-mirror` (assuming `~/.local/bin` is in your PATH).

#### Installation Options

```bash
./install.bash [OPTIONS]
```

**Options:**

- `--prefix <directory>`: Install to specified directory (default: `~/.local/bin`)
- `--create-dirs`: Create installation directory if it doesn't exist

**Examples:**

```bash
# Default installation to ~/.local/bin
./install.bash

# Install to custom directory
./install.bash --prefix /usr/local/bin

# Install to custom directory, creating it if needed
./install.bash --prefix ~/mytools/bin --create-dirs
```

### Basic Syntax

```bash
switch-apt-mirror [OPTIONS] <new_mirror>
```

### Arguments

- `<new_mirror>`: Required. The new repository mirror URL (e.g., `mirrors.kernel.org`)

### Options

- `--type [deb|deb-src|all]`: Filter by repository type (default: `all`)
- `--suite [updates|backports|security|main|all]`: Filter by distribution suite (default: `all`)
- `--no-backup`: Skip backup creation
- `--no-update`: Skip running 'apt update' after switching mirrors

### Examples

```bash
# Basic mirror change
sudo switch-apt-mirror mirrors.kernel.org

# Target only binary packages
sudo switch-apt-mirror --type deb mirrors.kernel.org

# Update only security repositories
sudo switch-apt-mirror --suite security security.ubuntu.com

# Skip backup for testing
sudo switch-apt-mirror --no-backup test-mirror.example.com

# Skip automatic apt update
sudo switch-apt-mirror --no-update mirrors.kernel.org

# Development usage (before installation)
sudo ./run.bash mirrors.kernel.org
```

## Repository Entry Format Support

APT source entries follow this structure:

```text
<type> [<options>] <uri> <distribution>[-<suite>] <component1> [component2] ...
```

### Field Definitions

- `<type>`: `deb` (binary packages) or `deb-src` (source packages)
- `[<options>]`: Optional parameters in square brackets (e.g., `[arch=amd64 signed-by=/path/to/key]`)
- `<uri>`: Repository URL (the field this tool modifies)
- `<distribution>`: Distribution codename (e.g., `focal`, `jammy`)
- `<suite>`: Optional suite suffix (`-updates`, `-backports`, `-security`)
- `<component>`: Repository components (`main`, `universe`, `restricted`, `multiverse`)

### Filtering Logic

**Type Filtering**:

- `deb`: Match only binary package repositories
- `deb-src`: Match only source package repositories
- `all`: Match both types

**Suite Filtering**:

- `updates`: Match distributions ending with `-updates`
- `backports`: Match distributions ending with `-backports`
- `security`: Match distributions ending with `-security`
- `main`: Match distributions without suite suffix (base distribution)
- `all`: Match any distribution/suite combination

## Technical Implementation

### Dependencies

- **Required**: `awk`, `sudo` (root privileges)
- **Validation**: Tool exits with error code 1 if dependencies are missing
- **Environment Requirements**:
  - `/etc/apt/sources.list` file must exist and be readable
  - Root/sudo privileges required for modifying `/etc/apt/` files

### Processing Pipeline

1. **Validation Phase**:
   - Check for required dependencies (`awk`)
   - Verify root/sudo privileges
   - Validate command line arguments

2. **Backup Phase** (skipped if `--no-backup`):
   - Create timestamped backup: `/etc/apt/sources.list.backup.YYYYMMDD_HHMMSS`
   - Create convenience symlink: `/etc/apt/sources.list.backup` → most recent backup

3. **Processing Phase**:
   - Use AWK-based text processing for reliable field parsing
   - Apply type and suite filters to target specific repositories
   - Replace URI field while preserving all other metadata
   - Handle only active (uncommented) repository entries

4. **Update Phase** (skipped if `--no-update`):
   - Execute `apt-get update` to refresh package lists
   - Verify mirror connectivity automatically

### Error Handling

- **Batch Processing**: Process all matching entries, continue on individual failures
- **Logging**: Colored output with different log levels (INFO, SUCCESS, WARNING, ERROR)
- **Graceful Degradation**: Atomic operations with backup → modify → verify workflow

## Error Conditions

### Pre-execution Validation

- Missing `awk` command
- Missing root/sudo privileges
- Non-existent `/etc/apt/sources.list` file
- Invalid command line arguments

### Runtime Errors

- File permission issues during backup creation
- Backup creation failures (aborts operation unless `--no-backup`)
- Malformed source entries in `/etc/apt/sources.list`
- Network connectivity issues during `apt update`
- Processing failures during URI replacement

### Input Validation

- Accept any string values for `--type` and `--suite` options (no hardcoded validation)
- Allow flexibility for custom repository types and suites beyond standard values
- Only validate that required parameters are provided

## Shell Script Architecture

### Source Files

- **run.bash**: Main script with argument parsing, validation, and mirror switching logic
- **install.bash**: Installation script with `--prefix` and `--create-dirs` options for flexible installation to user-specified directories
- **replace_entry_uri.awk**: AWK script for URI replacement in source entries

### Function Organization

- **Logging**: `log::info`, `log::success`, `log::warning`, `log::error`
- **Validation**: `check_dependencies`, `show_environment`
- **File Operations**: `sources_file::*` namespace functions
- **Package Management**: `apt::update` function
- **Argument Processing**: `parse_args` function

### Script Options

```bash
set -euo pipefail
```

- **`-e`**: Exit on any command failure
- **`-u`**: Exit on undefined variable usage
- **`-o pipefail`**: Exit on pipeline failures

## Use Cases for AI Assistants

### Implementation Assistance

- Understanding the AWK-based text processing workflow
- Extending functionality for additional file types (e.g., sources.list.d support)
- Debugging mirror switching failures
- Adding support for additional repository validation

### User Support

- Troubleshooting mirror switching issues
- Explaining the backup and restore process
- Guiding users through manual recovery procedures
- Recommending appropriate mirror URLs for different regions

### Automation Integration

- Incorporating into system setup and provisioning scripts
- Setting up automated mirror switching for different environments
- Integration with configuration management systems
- CI/CD pipeline usage for consistent package sources

## Limitations and Considerations

- **Single File Target**: Processes `/etc/apt/sources.list` only, not files in `sources.list.d/`
- **Root Privileges**: Requires sudo/root access for system file modifications
- **No Rollback**: Tool only handles forward migration, manual backup restoration needed for rollback
- **No Mirror Validation**: Does not validate mirror URL accessibility before switching
- **Atomic Operations**: Ensures backup → modify → verify workflow but no transaction rollback on failure
