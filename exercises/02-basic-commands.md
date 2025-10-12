# Exercise 2: Basic Docker Commands

## Overview

This exercise introduces you to fundamental Docker commands for managing images and containers. You'll learn to inspect your Docker environment and work with basic container operations.

## Learning Objectives

- Execute basic Docker information commands
- List Docker images and containers
- Understand the difference between images and containers
- Clean up Docker resources

## Step 1: Explore Your Docker Environment

### Check Docker System Information

```bash
docker system info
```

This command provides detailed information about your Docker installation including:

- Docker version
- Storage driver
- Available plugins
- System resources

### View Docker System Statistics

```bash
docker system df
```

Shows disk usage by Docker resources (images, containers, volumes, build cache).

## Step 2: Working with Docker Images

### List All Images

```bash
docker images
```

Alternative command:

```bash
docker image ls
```

**Expected Output (initially empty):**

```bash
REPOSITORY   TAG       IMAGE ID   CREATED   SIZE
```

### Search for Images in Docker Hub

```bash
docker search ubuntu
```

This searches Docker Hub for Ubuntu-related images.

### Download an Image (without running)

```bash
docker pull ubuntu:latest
```

Downloads the latest Ubuntu image to your local system.

### List Images Again

```bash
docker images
```

Now you should see the Ubuntu image listed.

## Step 3: Working with Docker Containers

### List Running Containers

```bash
docker ps
```

### List All Containers (running and stopped)

```bash
docker ps -a
```

Alternative command:

```bash
docker container ls -a
```

**Expected Output (initially empty):**

```bash
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
```

### Run a Simple Container

```bash
docker run ubuntu:latest echo "Hello from Ubuntu container!"
```

### List Containers Again

```bash
docker ps -a
```

You should now see the container you just ran in "Exited" status.

## Step 4: Container Management

### Run Container Interactively

```bash
docker run -it ubuntu:latest /bin/bash
```

- `-i`: Keep STDIN open (interactive)
- `-t`: Allocate a pseudo-TTY (terminal)

Inside the container, try:

```bash
ls
cat /etc/os-release
exit
```

### Run Container in Background (Detached Mode)

```bash
docker run -d ubuntu:latest sleep 60
```

The `-d` flag runs the container in detached mode (background).

### Check Running Containers

```bash
docker ps
```

You should see the sleeping container running.

### Stop a Running Container

First, get the container ID from `docker ps`, then:

```bash
docker stop <CONTAINER_ID>
```

## Step 5: Naming and Managing Containers

### Run Container with Custom Name

```bash
docker run --name my-ubuntu -d ubuntu:latest sleep 30
```

### View Container Logs

```bash
docker logs my-ubuntu
```

### Execute Commands in Running Container

```bash
docker exec -it my-ubuntu /bin/bash
```

## Step 6: Cleanup Operations

### Remove a Specific Container

```bash
docker rm <CONTAINER_ID_or_NAME>
```

### Remove All Stopped Containers

```bash
docker container prune
```

### Remove a Specific Image

```bash
docker rmi ubuntu:latest
```

### Remove All Unused Images

```bash
docker image prune
```

### Complete System Cleanup (Use Carefully!)

```bash
docker system prune -a
```

This removes all unused containers, networks, images, and build cache.

## Exercise Tasks

Complete the following tasks and note the outputs:

1. **Environment Check**
   - [ ] Run `docker system info` and note Docker version
   - [ ] Run `docker system df` and observe initial disk usage

2. **Image Operations**
   - [ ] List current images (should be empty initially)
   - [ ] Pull the `nginx:latest` image
   - [ ] Pull the `python:3.9-slim` image
   - [ ] List images again and note the sizes

3. **Container Operations**
   - [ ] Run a simple `echo` command in an nginx container
   - [ ] Run an interactive bash session in the python container
   - [ ] Start a detached nginx container on port 80
   - [ ] List all containers (running and stopped)

4. **Management Operations**
   - [ ] Name a container and view its logs
   - [ ] Stop running containers
   - [ ] Remove specific containers
   - [ ] Clean up unused resources

## Command Reference Sheet

### Information Commands

```bash
docker --version          # Docker version
docker info              # System information
docker system df         # Disk usage
```

### Image Commands

```bash
docker images            # List images
docker pull <image>      # Download image
docker rmi <image>       # Remove image
docker image prune       # Remove unused images
```

### Container Commands

```bash
docker ps               # List running containers
docker ps -a            # List all containers
docker run <image>      # Run container
docker run -it <image>  # Run interactive container
docker run -d <image>   # Run detached container
docker stop <id>        # Stop container
docker rm <id>          # Remove container
docker logs <id>        # View container logs
docker exec -it <id>    # Execute command in container
```

### Cleanup Commands

```bash
docker container prune   # Remove stopped containers
docker image prune      # Remove unused images
docker system prune     # Remove unused resources
docker system prune -a  # Remove all unused resources
```

## Troubleshooting Tips

### Common Issues

- **Permission denied**: Use `sudo` on Linux or ensure Docker Desktop is running
- **Port already in use**: Stop conflicting services or use different ports
- **Image not found**: Check image name spelling and tag
- **Container name conflict**: Use unique names or remove existing container

### Getting Help

```bash
docker --help           # General help
docker run --help       # Command-specific help
docker <command> --help # Help for any Docker command
```

## Next Steps

Once you're comfortable with these basic commands, proceed to [Exercise 3: Hello World Container](03-hello-world.md) for a deeper dive into container operations.
