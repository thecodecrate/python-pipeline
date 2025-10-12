FROM mcr.microsoft.com/devcontainers/base:ubuntu

# Lifecycle scripts
USER vscode
ENV WORKSPACE_DIR=/tmp/workspace
COPY .devcontainer/tools ${WORKSPACE_DIR}/.devcontainer/tools
COPY .devcontainer/lifecycle ${WORKSPACE_DIR}/.devcontainer/lifecycle
RUN zsh ${WORKSPACE_DIR}/.devcontainer/lifecycle/_loaders/00-loader-on-dockerfile.zsh
