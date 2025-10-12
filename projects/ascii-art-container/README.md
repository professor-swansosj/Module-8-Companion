# ASCII Art Container Project

## Overview

This project teaches you to create a custom Docker image that displays ASCII art using the `toilet` command. You'll learn how to write a Dockerfile, build an image, and run it as a container.

## Learning Objectives

- Write a basic Dockerfile
- Build a custom Docker image
- Run containers from your custom image
- Update and rebuild Docker images
- Understand image layers and caching

## Project Structure

```yaml
ascii-art-container/
├── Dockerfile           # Instructions to build the image
├── README.md           # This file
└── art-messages.txt    # Sample messages for ASCII art
```

## Step 1: Create the Initial Dockerfile

Create a file named `Dockerfile` (no extension) with the following content:

```dockerfile
# Use Ubuntu as base image
FROM ubuntu:22.04

# Update package list and install toilet
RUN apt-get update && apt-get install -y toilet

# Set working directory
WORKDIR /app

# Default command to run when container starts
CMD ["toilet", "Hello Network Engineers!"]
```

## Step 2: Build Your First Image

### Build the Docker Image

```bash
docker build -t my-ascii-art:v1 .
```

**Command Breakdown:**

- `docker build`: Command to build an image
- `-t my-ascii-art:v1`: Tag the image with name and version
- `.`: Use current directory as build context

### Expected Output

You'll see Docker executing each step:

```bash
Sending build context to Docker daemon...
Step 1/4 : FROM ubuntu:22.04
Step 2/4 : RUN apt-get update && apt-get install -y toilet
Step 3/4 : WORKDIR /app
Step 4/4 : CMD ["toilet", "Hello Network Engineers!"]
Successfully built <image_id>
Successfully tagged my-ascii-art:v1
```

### Verify the Image

```bash
docker images
```

You should see your new image listed.

## Step 3: Run Your Custom Container

### Run the Container

```bash
docker run my-ascii-art:v1
```

You should see ASCII art output similar to:

```bash
 _   _      _ _         _   _      _                      _    
| | | | ___| | | ___   | \ | | ___| |___      _____  _ __| | __
| |_| |/ _ \ | |/ _ \  |  \| |/ _ \ __\ \ /\ / / _ \| '__| |/ /
|  _  |  __/ | | (_) | | |\  |  __/ |_ \ V  V / (_) | |  |   < 
|_| |_|\___|_|_|\___/  |_| \_|\___|\__| \_/\_/ \___/|_|  |_|\_\
                                                              
 _____             _                          _ 
| ____|_ __   __ _(_)_ __   ___  ___ _ __ ___| |
|  _| | '_ \ / _` | | '_ \ / _ \/ _ \ '__/ __| |
| |___| | | | (_| | | | | |  __/  __/ |  \__ \_
|_____|_| |_|\__, |_|_| |_|\___|\___|_|  |___(_)
             |___/                             
```

## Step 4: Create Sample Messages File

Create `art-messages.txt` with various messages to display:

```text
Docker Rocks!
Network Automation
SDN Rules
Container Magic
Hello World
DevOps Ninja
Cloud Native
Microservices
```

## Step 5: Update Your Dockerfile

Update your Dockerfile to be more flexible:

```dockerfile
# Use Ubuntu as base image
FROM ubuntu:22.04

# Avoid prompts from apt
ENV DEBIAN_FRONTEND=noninteractive

# Update package list and install toilet and figlet
RUN apt-get update && \
    apt-get install -y toilet figlet && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy sample messages file
COPY art-messages.txt /app/

# Create a simple script to show random message
RUN echo '#!/bin/bash\nif [ $# -eq 0 ]; then\n  MESSAGE=$(shuf -n 1 /app/art-messages.txt)\nelse\n  MESSAGE="$*"\nfi\ntoilet "$MESSAGE"' > /app/show-art.sh && \
    chmod +x /app/show-art.sh

# Default command
CMD ["/app/show-art.sh"]
```

## Step 6: Rebuild with Updates

### Build Version 2

```bash
docker build -t my-ascii-art:v2 .
```

### Test the Updated Image

```bash
# Run with random message
docker run my-ascii-art:v2

# Run with custom message
docker run my-ascii-art:v2 "Custom Message!"

# Run multiple times to see random messages
docker run my-ascii-art:v2
docker run my-ascii-art:v2
docker run my-ascii-art:v2
```

## Step 7: Interactive Mode

### Run Container Interactively

```bash
docker run -it my-ascii-art:v2 /bin/bash
```

Inside the container, try:

```bash
# Use toilet directly
toilet "Interactive Mode"

# Use figlet (another ASCII art tool)
figlet "Figlet Style"

# View the messages file
cat /app/art-messages.txt

# Run the script manually
/app/show-art.sh "Manual Script Run"

# Exit container
exit
```

## Step 8: Advanced Dockerfile (Optional)

Create an even more advanced version:

```dockerfile
FROM ubuntu:22.04

# Install packages and create non-root user
RUN apt-get update && \
    apt-get install -y toilet figlet cowsay fortune && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    useradd -m -s /bin/bash artuser

# Switch to non-root user
USER artuser
WORKDIR /home/artuser

# Copy files as the user
COPY --chown=artuser:artuser art-messages.txt ./

# Create advanced script
RUN echo '#!/bin/bash\n\
if [ "$1" = "--fortune" ]; then\n\
    fortune | cowsay\n\
elif [ "$1" = "--figlet" ]; then\n\
    figlet "${2:-Hello Docker}"\n\
elif [ $# -eq 0 ]; then\n\
    MESSAGE=$(shuf -n 1 ./art-messages.txt)\n\
    toilet "$MESSAGE"\n\
else\n\
    toilet "$*"\n\
fi' > show-art.sh && \
    chmod +x show-art.sh

CMD ["./show-art.sh"]
```

### Build and Test Advanced Version

```bash
docker build -t my-ascii-art:v3 .

# Test different modes
docker run my-ascii-art:v3
docker run my-ascii-art:v3 "Network Engineer"
docker run my-ascii-art:v3 --figlet "Docker Pro"
docker run my-ascii-art:v3 --fortune
```

## Exercise Tasks

Complete these tasks to master custom image creation:

### Basic Tasks

- [ ] Create the initial Dockerfile
- [ ] Build your first image (v1)
- [ ] Run the container and see ASCII art output
- [ ] Create the art-messages.txt file

### Intermediate Tasks

- [ ] Update Dockerfile to version 2
- [ ] Rebuild the image with new features
- [ ] Test random message functionality
- [ ] Run container with custom messages
- [ ] Explore the container in interactive mode

### Advanced Tasks (Optional)

- [ ] Create the advanced Dockerfile (v3)
- [ ] Test all different modes (toilet, figlet, fortune)
- [ ] Understand user permissions in containers
- [ ] Compare image sizes between versions

### Analysis Tasks

- [ ] Compare the three image versions with `docker images`
- [ ] Use `docker history` to see image layers
- [ ] Time how long each version takes to build
- [ ] Understand Docker's layer caching

## Key Learning Points

### Dockerfile Best Practices

1. **Use specific base image tags** (ubuntu:22.04 vs ubuntu:latest)
2. **Combine RUN commands** to reduce layers
3. **Clean up package caches** to reduce image size
4. **Use non-root users** for security
5. **Set appropriate working directories**

### Docker Build Process

- Each Dockerfile instruction creates a new layer
- Docker caches layers to speed up builds
- Only changed layers and subsequent layers are rebuilt
- Build context includes all files in the build directory

### Container vs Image Versioning

- Tag images with meaningful versions
- Keep multiple versions for rollback capability
- Use semantic versioning (v1, v2, v3 or 1.0, 1.1, 2.0)

## Troubleshooting

### Common Issues

- **Build fails**: Check Dockerfile syntax and indentation
- **Package install fails**: Update package lists first
- **Permission denied**: Check file permissions and user context
- **Command not found**: Ensure packages are installed correctly

### Debugging Tips

```bash
# Build with verbose output
docker build -t my-ascii-art:debug . --progress=plain

# Run container with shell override
docker run -it my-ascii-art:v2 /bin/bash

# Check container logs
docker logs <container_id>

# Inspect image details
docker inspect my-ascii-art:v2
```

## Next Steps

Once you've mastered creating custom images with ASCII art, proceed to the [FastAPI Container Project](../fastapi-container/README.md) to learn about building web service containers.
