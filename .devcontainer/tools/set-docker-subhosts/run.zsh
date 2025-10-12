#!/usr/bin/env zsh

# Script to update /etc/hosts with running Docker container IP addresses
# This script maintains a section in /etc/hosts between markers for Docker containers

set -e  # Exit on any error

# Marker lines for /etc/hosts section
BEGIN_MARKER="# BEGIN DOCKER HOSTS"
END_MARKER="# END DOCKER HOSTS"

# Function to log messages
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1"
}

# Function to check if Docker is running
check_docker() {
    if ! docker info >/dev/null 2>&1; then
        log "ERROR: Docker daemon is not running or not accessible"
        return 1
    fi
    return 0
}

# Function to get container mappings in /etc/hosts format
get_container_mappings() {
    local mappings=""

    # Get running containers and their IP addresses
    docker ps --format "table {{.Names}}" | tail -n +2 | while read container_name; do
        if [[ -n "$container_name" ]]; then
            # Get first IP address (primary network)
            ip_address=$(docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{break}}{{end}}' "$container_name" 2>/dev/null)
            if [[ -n "$ip_address" && "$ip_address" != "" ]]; then
                echo "$ip_address $container_name"
            fi
        fi
    done
}

# Function to update /etc/hosts file
update_hosts_file() {
    local container_mappings="$1"
    local hosts_file="/etc/hosts"
    local temp_file="/tmp/hosts.tmp.$$"
    local backup_file="/etc/hosts.backup.$(date +%s)"

    # Check if we have sudo access
    if [[ $EUID -ne 0 ]]; then
        log "ERROR: This script needs to be run with sudo privileges to modify /etc/hosts"
        return 1
    fi

    # Create backup
    cp "$hosts_file" "$backup_file"
    log "Created backup: $backup_file"

    # Check if markers exist in the file
    if ! grep -q "$BEGIN_MARKER" "$hosts_file" || ! grep -q "$END_MARKER" "$hosts_file"; then
        log "Markers not found in $hosts_file. Adding Docker hosts section..."
        # Add markers and content at the end of the file
        {
            cat "$hosts_file"
            echo ""
            echo "$BEGIN_MARKER"
            if [[ -n "$container_mappings" ]]; then
                echo "$container_mappings"
            fi
            echo "$END_MARKER"
        } > "$temp_file"
    else
        # Replace content between markers
        log "Updating existing Docker hosts section..."
        awk -v begin="$BEGIN_MARKER" -v end="$END_MARKER" -v mappings="$container_mappings" '
        BEGIN { in_section = 0 }
        $0 == begin {
            print $0
            if (mappings != "") print mappings
            in_section = 1
            next
        }
        $0 == end {
            print $0
            in_section = 0
            next
        }
        !in_section { print $0 }
        ' "$hosts_file" > "$temp_file"
    fi

    # Validate the temporary file
    if [[ ! -s "$temp_file" ]]; then
        log "ERROR: Generated hosts file is empty. Aborting update."
        rm -f "$temp_file"
        return 1
    fi    # Copy content to hosts file (safer for mounted files)
    cat "$temp_file" > "$hosts_file"

    # Clean up temporary file
    rm -f "$temp_file"

    # Preserve original permissions
    chmod 644 "$hosts_file"
    chown root:root "$hosts_file"

    log "Successfully updated $hosts_file"
    return 0
}

# Main execution
main() {
    log "Starting Docker hosts update..."

    # Check if Docker is available
    if ! check_docker; then
        log "Docker is not available. Skipping hosts update."
        return 0
    fi

    # Get container mappings
    log "Retrieving container IP mappings..."
    local container_mappings
    container_mappings=$(get_container_mappings)

    if [[ -z "$container_mappings" ]]; then
        log "No running containers with IP addresses found."
        container_mappings=""
    else
        log "Found container mappings:"
        echo "$container_mappings" | while read line; do
            log "  $line"
        done
    fi

    # Update /etc/hosts
    if update_hosts_file "$container_mappings"; then
        log "Docker hosts update completed successfully"
    else
        log "ERROR: Failed to update hosts file"
        return 1
    fi
}

# Run main function if script is executed directly
if [[ "${BASH_SOURCE[0]}" == "${0}" ]] || [[ "${(%):-%N}" == "${0}" ]]; then
    main "$@"
fi
