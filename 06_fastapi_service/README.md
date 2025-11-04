# 🚀 Section 06: FastAPI Service - Persistent Web Container CLI

## 🎯 Mission Brief

The final frontier! Build a persistent web service using `docker run -d` with port mapping. Master long-running containers that provide network automation APIs accessible from your host system.

## 🧭 Learning Path

- **Detached Mode**: Run containers in background with `-d` flag
- **Port Mapping**: Connect container ports to host with `-p` option  
- **Persistent Services**: Keep containers running continuously
- **Web Service Testing**: Access APIs from outside containers

## 🌟 The Grand Finale

### Step 1: Discover Docker Run Detached Mode

```bash
# Explore detached mode options
docker run --help | findstr "detach\|port"

# Key options to master:
# -d, --detach      Run container in background and print container ID
# -p, --publish     Publish a container's port(s) to the host

# Try detached mode exploration
docker run --help | findstr "\-d\|\-p"
```

**🎯 Challenge**: What's the difference between `docker run` and `docker run -d`?

### Step 2: Build Your FastAPI Service

Complete the Python web service, then build it:

```bash
# Build your network automation API
docker build -t network-api .

# Verify the build
docker images network-api
```

**🎯 CLI Discovery**: Try `docker build --help` - what's the `--target` option for?

### Step 3: Deploy Persistent Service

```bash
# Run in detached mode with port mapping
docker run -d -p 8080:8000 --name network-service network-api

# Verify it's running in background
docker ps

# Should show your container running, not exited!
```

**🎯 Port Mapping Challenge**: What does `-p 8080:8000` mean? Try `-p 9000:8000` instead!

### Step 4: Test Your Live API

```bash
# Test your API endpoints (if curl is available)
curl http://localhost:8080

# Or use PowerShell's Invoke-WebRequest
Invoke-WebRequest http://localhost:8080

# Test multiple endpoints
Invoke-WebRequest http://localhost:8080/health
Invoke-WebRequest http://localhost:8080/devices
```

**🎯 Discovery Mission**: Open <http://localhost:8080> in your browser! See your API docs!

### Step 5: Service Management CLI

```bash
# Check container status
docker ps

# View real-time logs from running container
docker logs network-service

# Follow logs live (Ctrl+C to exit)
docker logs -f network-service

# Stop the service
docker stop network-service

# Remove the stopped container
docker rm network-service
```

**🎯 CLI Explorer Challenge**: Use `docker logs --help` to find ALL logging options!

## 🔄 Service Lifecycle Management

### Start Your Service

```bash
# Deploy the service
docker run -d -p 8080:8000 --name api-service network-api

# Verify deployment
docker ps
```

### Monitor Your Service

```bash
# Check if it's responsive
Invoke-WebRequest http://localhost:8080/health

# Monitor resource usage
docker stats api-service

# View detailed container info
docker inspect api-service
```

### Manage Your Service

```bash
# Restart if needed
docker restart api-service

# Stop gracefully
docker stop api-service

# Force stop if unresponsive
docker kill api-service
```

**🎯 Resource Challenge**: Try `docker stats --help` - monitor multiple containers at once!

## 🎮 Advanced Challenges

### Challenge 1: Multiple Service Instances

```bash
# Run multiple instances on different ports
docker run -d -p 8080:8000 --name api-v1 network-api
docker run -d -p 8081:8000 --name api-v2 network-api
docker run -d -p 8082:8000 --name api-v3 network-api

# Test all instances
Invoke-WebRequest http://localhost:8080/health
Invoke-WebRequest http://localhost:8081/health
Invoke-WebRequest http://localhost:8082/health

# See all running services
docker ps --filter name=api-
```

### Challenge 2: Service Health Monitoring

```bash
# Run with automatic restart policy
docker run -d -p 8080:8000 --name persistent-api --restart always network-api

# Test restart behavior
docker stop persistent-api
# Wait a moment, then check:
docker ps

# The container should restart automatically!
```

### Challenge 3: Container Networking

```bash
# Explore container networking
docker network ls

# Run container on custom network
docker network create api-network
docker run -d --network api-network --name networked-api network-api

# Test network connectivity between containers
docker run --network api-network --rm alpine/curl curl http://networked-api:8000
```

## 📚 CLI Command Reference

| Command | Purpose | Example |
|---------|---------|---------|
| `docker run -d` | Run in background | `docker run -d network-api` |
| `docker run -p host:container` | Map ports | `docker run -p 8080:8000 network-api` |
| `docker ps` | List running containers | `docker ps` |
| `docker logs -f container` | Follow logs live | `docker logs -f api-service` |
| `docker stop container` | Stop container gracefully | `docker stop api-service` |
| `docker restart container` | Restart container | `docker restart api-service` |
| `docker stats container` | Monitor resources | `docker stats api-service` |

## 🔧 Troubleshooting Web Services

### Port Already in Use?

```bash
# Find what's using the port
netstat -an | findstr :8080

# Use a different port
docker run -d -p 8090:8000 --name api-service network-api
```

### Service Not Responding?

```bash
# Check container logs
docker logs api-service

# Check if container is still running
docker ps -a

# Test container networking
docker exec -it api-service curl http://localhost:8000
```

### Container Keeps Exiting?

```bash
# Check exit status and logs
docker ps -a
docker logs api-service

# Run interactively for debugging
docker run -it network-api /bin/bash
```

## 🎯 Success Checklist

- [ ] Built FastAPI service with `docker build -t network-api .`
- [ ] Deployed in detached mode with `docker run -d -p 8080:8000 network-api`
- [ ] Verified service running with `docker ps`
- [ ] Tested API endpoints via browser or CLI tools
- [ ] Monitored logs with `docker logs -f`
- [ ] Managed service lifecycle (start/stop/restart)
- [ ] Explored port mapping with different port numbers

## 🎊 Mission Complete

**Congratulations!** You've conquered Docker containers and built a complete network automation API service. You now have the skills to:

### ✅ What You've Mastered

- **Docker CLI Mastery**: All essential docker commands and options
- **Container Lifecycle**: Build, run, manage, and troubleshoot containers
- **Service Deployment**: Long-running web services with port mapping
- **Network Automation**: Containerized APIs for network operations

### 🚀 Your Next Adventures

- **Container Orchestration**: Learn Kubernetes for scaling
- **CI/CD Pipelines**: Automate container deployment
- **Microservices**: Build distributed network automation systems
- **Production Deployment**: Deploy containers to cloud platforms

---

> **You're now a Container-Powered Network Engineer!** 🐳⚡ Every Python script you create can become a portable, scalable service. The future of network automation is containerized!
