# Use Ubuntu as base image
FROM ubuntu:22.04

# Update package list and install toilet
RUN apt-get update && apt-get install -y toilet

# Set working directory
WORKDIR /app

# Default command to run when container starts
CMD ["toilet", "Hello Network Engineers!"]