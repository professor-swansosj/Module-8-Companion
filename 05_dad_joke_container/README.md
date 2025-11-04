# 🎭 Section 05: Dad Joke Container - Network Service CLI

## 🎯 Mission Brief

Time for network operations! Build a container that fetches dad jokes from the internet using command-line Docker tools. You'll master `docker build` with dependencies and `docker run` for networked services.

## 🧭 Learning Path

- **Docker Build**: Create images with Python dependencies
- **Container Networking**: Enable internet access in containers
- **Dependency Management**: Install packages using requirements.txt
- **Service Testing**: Run and verify networked containers

## 🚀 The Adventure Begins

### Step 1: Discover Docker Build Options

```bash
# Explore build command capabilities
docker build --help

# Focus on these key options:
# -t, --tag     Name and optionally a tag in the 'name:tag' format
# -f, --file    Name of the Dockerfile (Default is 'PATH/Dockerfile')
# --no-cache    Do not use cache when building the image

# Try building help exploration
docker build --help | findstr "tag\|file\|cache"
```

**🎯 Challenge**: What's the difference between `docker build .` and `docker build -t myimage .`?

### Step 2: Build Your Joke Service

The Python app is ready - now use Docker CLI to containerize it:

```bash
# Build the dad joke service image
docker build -t dad-joke-service .

# Verify your image was created
docker images

# Look for your dad-joke-service in the list
docker images dad-joke-service
```

**🎯 CLI Discovery**: Try `docker images --help` - what filtering options do you have?

### Step 3: Run Network-Enabled Containers

```bash
# Run the joke service (needs internet access)
docker run dad-joke-service

# Run it multiple times for different jokes
docker run dad-joke-service
docker run dad-joke-service
docker run dad-joke-service
```

**🎯 Challenge**: Each run creates a new container. Use `docker ps -a` to see them all!

### Step 4: Network Testing Adventures

```bash
# Test normal network access
docker run dad-joke-service

# Test WITHOUT network access (should show fallback joke)
docker run --network none dad-joke-service

# Compare the outputs - see the fallback system working!
```

**🎯 Discovery Mission**:

```bash
# Explore network options
docker run --help | findstr "network"

# What other network modes are available?
docker network --help
docker network ls
```

### Step 5: Container Management CLI

```bash
# See all containers (including stopped ones)
docker ps -a

# Clean up stopped containers
docker container prune

# Or remove specific containers
docker rm <container_id>

# Remove the image if you want to rebuild
docker rmi dad-joke-service
```

**🎯 CLI Explorer Challenge**: Use `docker container --help` to find ALL container management commands!

## 🔍 Dockerfile Detective Work

Open the `Dockerfile` and complete the TODOs. Key concepts:

```dockerfile
# Layer optimization - copy requirements first
COPY requirements.txt .
RUN pip install -r requirements.txt

# Then copy code (better caching)
COPY joke_fetcher.py .
```

**Why this order?** Dependencies change less often than code!

## 🧪 Testing Your Service

### Network Connectivity Test

```bash
# Normal run (with internet)
docker run dad-joke-service

# Offline test (no internet)
docker run --network none dad-joke-service
```

### Build Testing

```bash
# Clean build (no cache)
docker build --no-cache -t dad-joke-service .

# Quick rebuild (with cache)
docker build -t dad-joke-service .
```

**🎯 Speed Challenge**: Time both builds. See the caching difference!

## 🎮 Practice Challenges

### Challenge 1: Image Variations

```bash
# Build with different tags
docker build -t dad-joke-service:v1 .
docker build -t dad-joke-service:latest .
docker build -t dad-joke-service:network-enabled .

# See all your tagged versions
docker images dad-joke-service
```

### Challenge 2: Container Naming

```bash
# Run with custom names
docker run --name joke-container-1 dad-joke-service
docker run --name joke-container-2 dad-joke-service

# See your named containers
docker ps -a --filter name=joke-container
```

### Challenge 3: Log Investigation  

```bash
# Run a container
docker run --name my-joke-container dad-joke-service

# Check its logs
docker logs my-joke-container

# Follow logs in real-time (if it was long-running)
docker logs -f my-joke-container
```

## 📚 Command Reference

| Command | Purpose | Example |
|---------|---------|---------|
| `docker build -t name .` | Build tagged image | `docker build -t dad-joke-service .` |
| `docker run image` | Run container | `docker run dad-joke-service` |
| `docker run --network none` | Run without network | `docker run --network none dad-joke-service` |
| `docker images` | List images | `docker images dad-joke-service` |
| `docker ps -a` | List all containers | `docker ps -a` |
| `docker logs container` | View container logs | `docker logs my-joke-container` |
| `docker rm container` | Remove container | `docker rm my-joke-container` |
| `docker rmi image` | Remove image | `docker rmi dad-joke-service` |

## 🔧 Troubleshooting CLI

### Build Problems?

```bash
# Check if Dockerfile exists
dir Dockerfile

# Try building with verbose output
docker build -t dad-joke-service . --progress=plain
```

### Network Issues?

```bash
# Test container internet access
docker run dad-joke-service

# If network fails, check Docker daemon
docker version
```

### Container Not Starting?

```bash
# Check logs for errors
docker logs <container_name>

# Run interactively for debugging
docker run -it dad-joke-service /bin/bash
```

## 🎯 Success Checklist

- [ ] Built image using `docker build -t dad-joke-service .`
- [ ] Successfully ran container with `docker run dad-joke-service`
- [ ] Tested network connectivity with normal run
- [ ] Tested fallback with `--network none` flag
- [ ] Managed containers using `docker ps` and `docker rm`
- [ ] Explored build options with `docker build --help`
- [ ] Used container naming with `--name` flag

## 🚀 Next Adventure

Outstanding! You've mastered networked containers and CLI management. Ready for **[Section 06: FastAPI Service](../06_fastapi_service/README.md)** - build persistent web services that stay running!

---

> **Network Automation Ready!** 🌐 You can now build containers that interact with APIs and external services - the foundation of network automation tools!
