# The base image
FROM ubuntu:24.04

###
# If you need "docker-in-docker" feature, use this Debian base image:
# ```
# FROM debian:bookworm-slim
# ```
#
# Then, add to `devcontainer.json`:
# ```
# "features": {
#     "ghcr.io/devcontainers/features/docker-in-docker:2": {}
# }
# ```
###

# The name of the Conda environment to create
ARG CONDA_ENV_NAME=venv
ENV CONDA_ENV_NAME=${CONDA_ENV_NAME}

# The version of Node.js to install
ARG NODE_VERSION=20

# Set the PYTHONPATH
ENV PYTHONPATH=/app:/app/jupyter:/app/src:$PYTHONPATH

# Install git, wget, supervisor, etc.
RUN apt-get update \
    && mkdir -p /etc/apt/keyrings \
    && apt-get install -y gnupg wget curl zip unzip git supervisor sqlite3 fswatch

# Set the working directory to /app
WORKDIR /app

# Install Miniforge in /opt/conda
RUN wget https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Linux-x86_64.sh -O /tmp/miniforge.sh \
    && bash /tmp/miniforge.sh -b -p /opt/conda \
    && rm /tmp/miniforge.sh

# Update Mamba
RUN /opt/conda/bin/mamba update -y -n base -c defaults mamba

# Add Miniforge to PATH
ENV PATH="/opt/conda/bin:$PATH"

# Copy the environment.yml file from your host to the current location in the container (i.e., /app)
COPY ./environment.yml .

# Create Mamba environment
RUN mamba env create -f environment.yml

# Initialize Conda
RUN mamba init bash

# Activate environment when opening a terminal
RUN echo "mamba activate ${CONDA_ENV_NAME}" >> ~/.bashrc

# supervisord
COPY ./docker/local/etc/supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# Set the entrypoint to supervisord
ENTRYPOINT ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]
