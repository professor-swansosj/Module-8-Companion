# Docker Commands Reference

## Essential Docker Commands

This reference sheet contains the most commonly used Docker commands for Module 8 exercises.

### Docker Information Commands

```bash
# Check Docker version
docker --version
docker version

# Display system information
docker info
docker system info

# Show Docker disk usage
docker system df

# Show real-time Docker events
docker system events

# Get help for any command
docker --help
docker <command> --help
```

### Image Management

```bash
# List all local images
docker images
docker image ls

# Search Docker Hub for images
docker search <image_name>

# Pull an image from registry
docker pull <image_name>
docker pull <image_name>:<tag>

# Remove an image
docker rmi <image_id>
docker rmi <image_name>:<tag>

# Remove all unused images
docker image prune
docker image prune -a  # Remove all unused images, not just dangling

# Build image from Dockerfile
docker build -t <image_name>:<tag> .
docker build -t <image_name>:<tag> <path>

# Tag an image
docker tag <source_image> <target_image>:<tag>

# Show image history/layers
docker history <image_name>

# Inspect image details
docker inspect <image_name>
```

### Container Lifecycle

```bash
# Run a container
docker run <image_name>
docker run -d <image_name>                    # Detached mode
docker run -it <image_name>                   # Interactive mode
docker run --name <container_name> <image>   # With custom name
docker run -p <host_port>:<container_port>    # Port mapping

# List containers
docker ps              # Running containers only
docker ps -a           # All containers (running and stopped)
docker ps -q           # Only container IDs

# Start/stop containers
docker start <container_id>
docker stop <container_id>
docker restart <container_id>

# Remove containers
docker rm <container_id>
docker rm -f <container_id>     # Force remove running container

# Execute commands in running container
docker exec -it <container_id> /bin/bash
docker exec <container_id> <command>
```

### Container Monitoring

```bash
# View container logs
docker logs <container_id>
docker logs -f <container_id>              # Follow logs (real-time)
docker logs --tail 50 <container_id>      # Last 50 lines

# Show container resource usage
docker stats
docker stats <container_id>

# Inspect container details
docker inspect <container_id>

# Show container processes
docker top <container_id>

# Show port mappings
docker port <container_id>
```

### Data Management

```bash
# List volumes
docker volume ls

# Create volume
docker volume create <volume_name>

# Remove volume
docker volume rm <volume_name>

# Mount volume to container
docker run -v <volume_name>:<container_path> <image>

# Bind mount (host directory to container)
docker run -v <host_path>:<container_path> <image>

# Copy files between host and container
docker cp <container_id>:<container_path> <host_path>
docker cp <host_path> <container_id>:<container_path>
```

### Network Management

```bash
# List networks
docker network ls

# Create network
docker network create <network_name>

# Connect container to network
docker network connect <network_name> <container_id>

# Disconnect container from network
docker network disconnect <network_name> <container_id>

# Inspect network
docker network inspect <network_name>

# Remove network
docker network rm <network_name>
```

### Cleanup Commands

```bash
# Remove stopped containers
docker container prune

# Remove unused images
docker image prune
docker image prune -a

# Remove unused volumes
docker volume prune

# Remove unused networks
docker network prune

# Complete cleanup (use with caution!)
docker system prune
docker system prune -a    # More aggressive cleanup

# Remove everything (DANGEROUS!)
docker system prune -a --volumes
```

## Dockerfile Commands

### Common Dockerfile Instructions

```dockerfile
# Base image
FROM <image_name>:<tag>

# Set working directory
WORKDIR <path>

# Copy files
COPY <source> <destination>
ADD <source> <destination>     # Can handle URLs and archives

# Run commands during build
RUN <command>

# Set environment variables
ENV <key>=<value>

# Expose ports
EXPOSE <port>

# Set default command
CMD ["executable", "param1", "param2"]

# Set entrypoint
ENTRYPOINT ["executable", "param1"]

# Create user
USER <username>

# Set labels
LABEL <key>=<value>

# Health check
HEALTHCHECK --interval=30s --timeout=3s CMD <command>
```

## Docker Compose Commands

### Basic Compose Operations

```bash
# Start services
docker-compose up
docker-compose up -d              # Detached mode
docker-compose up --build         # Force rebuild

# Stop services
docker-compose down
docker-compose down -v            # Remove volumes too

# View logs
docker-compose logs
docker-compose logs <service_name>

# Scale services
docker-compose up --scale <service>=<count>

# Execute commands in service
docker-compose exec <service> <command>
```

## Common Use Cases

### Development Workflow

```bash
# Build and run application
docker build -t myapp:dev .
docker run -d -p 8000:8000 --name myapp-container myapp:dev

# Make changes and rebuild
docker stop myapp-container
docker rm myapp-container
docker build -t myapp:dev .
docker run -d -p 8000:8000 --name myapp-container myapp:dev

# Quick cleanup and restart
docker stop myapp-container && docker rm myapp-container
docker run -d -p 8000:8000 --name myapp-container myapp:dev
```

### Debugging Containers

```bash
# Run container in interactive mode
docker run -it <image> /bin/bash

# Debug running container
docker exec -it <container_id> /bin/bash

# Check container logs
docker logs --tail 50 -f <container_id>

# Inspect container configuration
docker inspect <container_id> | grep -i <search_term>
```

### Network Testing

```bash
# Test connectivity between containers
docker exec <container1> ping <container2>

# Check open ports in container
docker exec <container_id> netstat -tlnp

# Test HTTP endpoints
docker exec <container_id> curl http://localhost:8000/health
```

## Troubleshooting Tips

### Common Issues and Solutions

1. **Port Already in Use**

   ```bash
   # Find process using port
   netstat -tlnp | grep :8000
   # Kill the process or use different port
   docker run -p 8001:8000 <image>
   ```

2. **Container Exits Immediately**

   ```bash
   # Check container logs
   docker logs <container_id>
   # Run interactively to debug
   docker run -it <image> /bin/bash
   ```

3. **Image Build Fails**

   ```bash
   # Build with verbose output
   docker build --progress=plain -t <image> .
   # Check Dockerfile syntax
   ```

4. **Cannot Connect to Container**

   ```bash
   # Verify port mapping
   docker port <container_id>
   # Check if service is running in container
   docker exec <container_id> ps aux
   ```

### Performance Tips

- Use `.dockerignore` to exclude unnecessary files from build context
- Leverage Docker layer caching by ordering Dockerfile commands properly
- Use multi-stage builds to reduce final image size
- Clean up unused resources regularly with `docker system prune`

### Security Best Practices

- Don't run containers as root user when possible
- Use specific image tags instead of `latest`
- Scan images for vulnerabilities: `docker scan <image>`
- Limit container resources: `docker run --memory=512m --cpus=1.0 <image>`

## Module 8 Specific Commands

### ASCII Art Container Commands

```bash
# Build the image
docker build -t my-ascii-art:v1 .

# Run with default message
docker run my-ascii-art:v1

# Run with custom message
docker run my-ascii-art:v2 "Custom Message"
```

### FastAPI Container Commands

```bash
# Build the API image
docker build -t network-api:v1 .

# Run the API container
docker run -d -p 8000:8000 --name network-api network-api:v1

# Test the API
curl http://localhost:8000/health
curl http://localhost:8000/devices
```

This reference guide should help you throughout Module 8 and beyond!
