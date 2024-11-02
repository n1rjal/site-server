# Use the RHEL 9 Python 3.12 image as the base image
FROM --platform=linux/amd64 registry.access.redhat.com/rhel9/python-312 as base

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Set the working directory
WORKDIR /app

# Install necessary packages using 'yum' for RHEL-based images
USER root
RUN yum update -y && \
    yum install -y \
        pkgconfig \
        gcc \
        gcc-c++ \
        make \
        libpq-devel \
        openssl \
        ca-certificates && \
    yum clean all

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir --no-compile -r requirements.txt

# Copy the application code
COPY . .

# Create a non-root user and adjust permissions
RUN groupadd -r gnome_group && \
    useradd -r -g gnome_group -d /app -s /sbin/nologin gnome_user && \
    chown -R og+rw gnome_user:gnome_group /app

# Switch to non-root user
USER gnome_user
EXPOSE 8000
CMD ["make", "prod"]

# # Define the worker stage
# FROM base AS worker
# # (Add any worker-specific configurations here)

# # Define the development stage
# FROM base AS development
# EXPOSE 8000
# CMD ["make", "dev"]

# Define the production stage
# FROM base AS production

