#!/usr/bin/env zsh
# Download and install latest asdf release from GitHub
# This script uses a hybrid approach: GitHub API first, Git tags as fallback

set -euo pipefail

# Configuration
ASDF_DIR="${ASDF_DIR:-$HOME/.asdf}"
ASDF_REPO="https://github.com/asdf-vm/asdf"
API_URL="https://api.github.com/repos/asdf-vm/asdf/releases/latest"
TIMEOUT_SECONDS=10
MAX_RETRIES=3

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Logging functions
log_info() {
    echo -e "${BLUE}[INFO]${NC} $1" >&2
}

log_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1" >&2
}

log_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1" >&2
}

log_error() {
    echo -e "${RED}[ERROR]${NC} $1" >&2
}

# Check prerequisites
check_prerequisites() {
    local missing_tools=()

    for tool in curl git jq; do
        if ! command -v "$tool" >/dev/null 2>&1; then
            missing_tools+=("$tool")
        fi
    done

    if [[ ${#missing_tools[@]} -gt 0 ]]; then
        log_error "Missing required tools: ${missing_tools[*]}"
        log_info "Installing missing tools..."

        # Install missing tools using apt (since we're in Ubuntu dev container)
        sudo apt-get update -qq
        for tool in "${missing_tools[@]}"; do
            sudo apt-get install -y "$tool"
        done

        log_success "Required tools installed"
    fi
}

# Get latest release using GitHub API with retry logic
get_latest_version_api() {
    local retry_count=0
    local retry_delay=2

    while [[ $retry_count -lt $MAX_RETRIES ]]; do
        local response
        if response=$(curl -sfS --connect-timeout "$TIMEOUT_SECONDS" "$API_URL" 2>/dev/null); then
            local tag_name
            if tag_name=$(echo "$response" | jq -r '.tag_name' 2>/dev/null) && [[ "$tag_name" != "null" ]] && [[ -n "$tag_name" ]]; then
                echo "$tag_name"
                return 0
            fi
        fi

        retry_count=$((retry_count + 1))
        if [[ $retry_count -lt $MAX_RETRIES ]]; then
            sleep "$retry_delay"
            retry_delay=$((retry_delay * 2))
        fi
    done

    return 1
}

# Fallback: Get latest release using Git tags
get_latest_version_git() {
    local latest_tag
    if latest_tag=$(git ls-remote --tags --sort=-v:refname "$ASDF_REPO" 2>/dev/null |
        grep -oP 'refs/tags/\Kv.*' |
        grep -v '\^' |
        head -1); then
        echo "$latest_tag"
        return 0
    fi

    return 1
}

# Get the latest version using hybrid approach
get_latest_version() {
    local version

    log_info "Attempting to fetch latest version from GitHub API..."
    # Try API first
    if version=$(get_latest_version_api); then
        log_success "Retrieved latest version from GitHub API: $version"
        echo "$version"
        return 0
    fi

    log_warning "GitHub API failed, falling back to Git tags method..."
    # Fallback to Git tags
    if version=$(get_latest_version_git); then
        log_success "Retrieved latest version from Git tags: $version"
        echo "$version"
        return 0
    fi

    log_error "Failed to retrieve latest version using both methods"
    return 1
}

# Check if asdf is already installed and up to date
check_existing_installation() {
    if [[ -d "$ASDF_DIR" ]] && [[ -f "$ASDF_DIR/bin/asdf" ]]; then
        local current_version
        if current_version=$("$ASDF_DIR/bin/asdf" version 2>/dev/null | cut -d' ' -f1); then
            log_info "Found existing asdf installation: $current_version"

            local latest_version
            if latest_version=$(get_latest_version); then
                # Remove 'v' prefix for comparison
                local current_clean="${current_version#v}"
                local latest_clean="${latest_version#v}"

                if [[ "$current_clean" == "$latest_clean" ]]; then
                    log_success "asdf is already up to date ($current_version)"
                    return 0
                else
                    log_info "Update available: $current_version -> $latest_version"
                    return 1
                fi
            fi
        fi
    fi

    return 1
}

# Download and install asdf
install_asdf() {
    local version="$1"

    log_info "Installing asdf $version"

    # Remove existing installation if present
    if [[ -d "$ASDF_DIR" ]]; then
        log_info "Removing existing asdf installation at $ASDF_DIR"
        rm -rf "$ASDF_DIR"
    fi

    # Check if this is a newer version (0.16+) that uses Go binary
    local version_number="${version#v}"
    local major_version="${version_number%%.*}"
    local minor_version="${version_number#*.}"
    minor_version="${minor_version%%.*}"

    if [[ "$major_version" -gt 0 ]] || [[ "$major_version" -eq 0 && "$minor_version" -ge 16 ]]; then
        log_info "Version $version is 0.16+ (Go-based), attempting binary download..."

        # Try to download pre-built binary for newer versions
        local arch=$(uname -m)
        local os=$(uname -s | tr '[:upper:]' '[:lower:]')

        # Map common architecture names
        case "$arch" in
            x86_64) arch="amd64" ;;
            aarch64 | arm64) arch="arm64" ;;
            *) log_warning "Unsupported architecture: $arch, falling back to source install" ;;
        esac

        local binary_url="https://github.com/asdf-vm/asdf/releases/download/${version}/asdf-${version}-${os}-${arch}.tar.gz" # Try to download binary
        log_info "Attempting to download binary from: $binary_url"
        local temp_dir=$(mktemp -d)
        if curl -sfL "$binary_url" -o "$temp_dir/asdf.tar.gz" 2>/dev/null; then
            mkdir -p "$ASDF_DIR/bin"
            # Extract the binary directly to the bin directory
            if tar -xzf "$temp_dir/asdf.tar.gz" -C "$ASDF_DIR/bin" 2>/dev/null; then
                rm -rf "$temp_dir"

                # Make sure the binary is executable
                chmod +x "$ASDF_DIR/bin/asdf"

                # Verify installation
                if [[ -f "$ASDF_DIR/bin/asdf" ]]; then
                    local installed_version
                    if installed_version=$("$ASDF_DIR/bin/asdf" version 2>/dev/null | head -1); then
                        log_success "Successfully installed asdf binary $version"
                        log_success "Binary installation verified: $installed_version"
                        return 0
                    fi
                fi
            fi
        fi

        rm -rf "$temp_dir"
        log_warning "Binary download failed, falling back to Git clone method"
    fi

    # Clone the repository (fallback or for older versions)
    log_info "Cloning asdf repository..."
    if ! git clone "$ASDF_REPO" "$ASDF_DIR" --quiet; then
        log_error "Failed to clone asdf repository"
        return 1
    fi

    # Checkout the specific version
    log_info "Checking out version $version..."
    if ! (cd "$ASDF_DIR" && git checkout "$version" --quiet); then
        log_error "Failed to checkout version $version"
        return 1
    fi

    # Verify installation
    if [[ -f "$ASDF_DIR/bin/asdf" ]]; then
        local installed_version
        if installed_version=$("$ASDF_DIR/bin/asdf" version 2>/dev/null | head -1); then
            log_success "Successfully installed asdf $installed_version"
            return 0
        fi
    fi

    log_error "Installation verification failed"
    return 1
}

# Configure shell integration (for zsh)
configure_shell() {
    local shell_config="$HOME/.zshrc"

    # Check if asdf is already configured
    if grep -q "asdf.sh\|\.asdf/bin" "$shell_config" 2>/dev/null; then
        log_info "asdf shell integration already configured"
        return 0
    fi

    log_info "Configuring asdf shell integration for zsh"

    # Backup existing config
    if [[ -f "$shell_config" ]]; then
        cp "$shell_config" "${shell_config}.backup.$(date +%Y%m%d_%H%M%S)"
    fi

    # Determine which asdf files exist for shell integration
    local asdf_init_line=""
    local asdf_completion_line=""

    if [[ -f "$ASDF_DIR/asdf.sh" ]]; then
        asdf_init_line=". \"\$HOME/.asdf/asdf.sh\""
    elif [[ -f "$ASDF_DIR/bin/asdf" ]]; then
        # For newer versions, add to PATH
        asdf_init_line="export PATH=\"\$HOME/.asdf/bin:\$PATH\""
    fi

    if [[ -f "$ASDF_DIR/completions/asdf.bash" ]]; then
        asdf_completion_line=". \"\$HOME/.asdf/completions/asdf.bash\""
    fi

    # Add asdf configuration
    {
        echo ""
        echo "# asdf version manager"
        [[ -n "$asdf_init_line" ]] && echo "$asdf_init_line"
        [[ -n "$asdf_completion_line" ]] && echo "$asdf_completion_line"
    } >>"$shell_config"

    log_success "Shell integration configured. Please restart your shell or run: source $shell_config"
}

# Validate installation
validate_installation() {
    log_info "Validating asdf installation..."

    # Try to source asdf for current session
    if [[ -f "$ASDF_DIR/asdf.sh" ]]; then
        # shellcheck source=/dev/null
        source "$ASDF_DIR/asdf.sh"
    elif [[ -f "$ASDF_DIR/bin/asdf" ]]; then
        # For newer versions, add to PATH
        export PATH="$ASDF_DIR/bin:$PATH"
    fi

    # Test asdf command
    if command -v asdf >/dev/null 2>&1; then
        local version
        if version=$(asdf version 2>/dev/null); then
            log_success "asdf is working correctly: $(echo "$version" | head -1)"

            # Test plugin listing (this works for both old and new versions)
            if asdf plugin list >/dev/null 2>&1; then
                log_success "asdf plugin system is functional"
                return 0
            else
                log_info "Plugin system test completed (empty plugin list is normal)"
                return 0
            fi
        fi
    fi

    log_warning "asdf validation failed. You may need to restart your shell."
    return 1
}

# Main execution
main() {
    log_info "Starting asdf installation script"

    # Check prerequisites
    check_prerequisites

    # Get latest version
    local latest_version
    if ! latest_version=$(get_latest_version); then
        log_error "Could not determine latest asdf version"
        return 1
    fi

    # Install asdf
    if ! install_asdf "$latest_version"; then
        log_error "Installation failed"
        return 1
    fi

    # Configure shell integration
    configure_shell

    # Validate installation
    validate_installation

    log_success "asdf installation completed successfully!"
    log_info "To start using asdf, restart your shell or run: source ~/.zshrc"
}

# Run main function
main "$@"

# Add shims directory to path
cat >>"$HOME/.zshrc" <<'EOF'
export PATH="${ASDF_DATA_DIR:-$HOME/.asdf}/shims:$PATH"
EOF

# Set up shell completions
mkdir -p "${ASDF_DATA_DIR:-$HOME/.asdf}/completions"
asdf completion zsh >"${ASDF_DATA_DIR:-$HOME/.asdf}/completions/_asdf"

# Add asdf completion setup to .zshrc
cat >>"$HOME/.zshrc" <<'EOF'
# append completions to fpath
fpath=(${ASDF_DATA_DIR:-$HOME/.asdf}/completions $fpath)

# initialise completions with ZSH's compinit
autoload -Uz compinit && compinit
EOF

# vim: set ft=sh:
