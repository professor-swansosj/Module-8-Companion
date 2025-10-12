# FastAPI Network Service Container

## Overview

This project demonstrates building a containerized web service using FastAPI, a modern Python web framework. You'll create a REST API for network device management, containerize it with Docker, and test it using cURL.

## Learning Objectives

- Build a Python web application with FastAPI
- Create production-ready Dockerfiles for web services
- Expose container ports for web services
- Test containerized APIs with cURL
- Understand container networking basics

## Project Structure

```yaml
fastapi-container/
├── app/
│   ├── __init__.py
│   └── main.py          # FastAPI application
├── requirements.txt     # Python dependencies
├── Dockerfile          # Container build instructions
├── docker-compose.yml  # Optional: multi-container setup
└── README.md          # This file
```

## Step 1: Create the FastAPI Application

### Create Application Directory Structure

First, create the `app` directory and files:

**app/**init**.py** (empty file):

```python
# This file makes the directory a Python package
```

**app/main.py**:

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import uvicorn

# Initialize FastAPI app
app = FastAPI(
    title="Network Device Management API",
    description="A simple API for managing network devices",
    version="1.0.0"
)

# Data models
class Device(BaseModel):
    id: int
    name: str
    ip_address: str
    device_type: str
    status: str = "unknown"

class DeviceUpdate(BaseModel):
    name: Optional[str] = None
    ip_address: Optional[str] = None
    device_type: Optional[str] = None
    status: Optional[str] = None

# In-memory database (for demo purposes)
devices_db = [
    Device(id=1, name="Router-01", ip_address="192.168.1.1", device_type="router", status="online"),
    Device(id=2, name="Switch-01", ip_address="192.168.1.10", device_type="switch", status="online"),
    Device(id=3, name="Firewall-01", ip_address="192.168.1.254", device_type="firewall", status="offline"),
]

@app.get("/")
async def root():
    """Welcome endpoint"""
    return {
        "message": "Welcome to Network Device Management API",
        "version": "1.0.0",
        "docs": "Visit /docs for interactive API documentation"
    }

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "service": "network-api"}

@app.get("/devices", response_model=List[Device])
async def get_devices():
    """Get all network devices"""
    return devices_db

@app.get("/devices/{device_id}", response_model=Device)
async def get_device(device_id: int):
    """Get a specific device by ID"""
    for device in devices_db:
        if device.id == device_id:
            return device
    raise HTTPException(status_code=404, detail="Device not found")

@app.post("/devices", response_model=Device)
async def create_device(device: Device):
    """Create a new device"""
    # Check if device ID already exists
    for existing_device in devices_db:
        if existing_device.id == device.id:
            raise HTTPException(status_code=400, detail="Device ID already exists")
    
    devices_db.append(device)
    return device

@app.put("/devices/{device_id}", response_model=Device)
async def update_device(device_id: int, device_update: DeviceUpdate):
    """Update a device"""
    for i, device in enumerate(devices_db):
        if device.id == device_id:
            # Update only provided fields
            if device_update.name is not None:
                device.name = device_update.name
            if device_update.ip_address is not None:
                device.ip_address = device_update.ip_address
            if device_update.device_type is not None:
                device.device_type = device_update.device_type
            if device_update.status is not None:
                device.status = device_update.status
            
            devices_db[i] = device
            return device
    
    raise HTTPException(status_code=404, detail="Device not found")

@app.delete("/devices/{device_id}")
async def delete_device(device_id: int):
    """Delete a device"""
    for i, device in enumerate(devices_db):
        if device.id == device_id:
            deleted_device = devices_db.pop(i)
            return {"message": f"Device {deleted_device.name} deleted successfully"}
    
    raise HTTPException(status_code=404, detail="Device not found")

# Device statistics endpoint
@app.get("/stats")
async def get_stats():
    """Get device statistics"""
    total_devices = len(devices_db)
    online_devices = len([d for d in devices_db if d.status == "online"])
    offline_devices = len([d for d in devices_db if d.status == "offline"])
    
    device_types = {}
    for device in devices_db:
        device_types[device.device_type] = device_types.get(device.device_type, 0) + 1
    
    return {
        "total_devices": total_devices,
        "online_devices": online_devices,
        "offline_devices": offline_devices,
        "device_types": device_types
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

### Create Requirements File

**requirements.txt**:

```python
fastapi==0.104.1
uvicorn[standard]==0.24.0
pydantic==2.5.0
```

## Step 2: Test Locally (Optional)

Before containerizing, you can test the application locally:

```bash
# Install dependencies
pip install -r requirements.txt

# Run the application
python app/main.py
```

Then visit `http://localhost:8000/docs` to see the interactive API documentation.

## Step 3: Create the Dockerfile

**Dockerfile**:

```dockerfile
# Use Python slim image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements first (for better caching)
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app/ ./app/

# Expose port 8000
EXPOSE 8000

# Create non-root user for security
RUN useradd -m -u 1000 appuser && chown -R appuser:appuser /app
USER appuser

# Health check
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:8000/health || exit 1

# Run the application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

## Step 4: Build and Run the Container

### Build the Docker Image

```bash
docker build -t network-api:v1 .
```

### Run the Container

```bash
docker run -d -p 8000:8000 --name network-api network-api:v1
```

**Command Breakdown:**

- `-d`: Run in detached mode (background)
- `-p 8000:8000`: Map host port 8000 to container port 8000
- `--name network-api`: Assign a name to the container

### Verify the Container is Running

```bash
docker ps
```

## Step 5: Test with cURL

Now test your API using cURL commands:

### Basic Health Check

```bash
curl http://localhost:8000/health
```

### Get Welcome Message

```bash
curl http://localhost:8000/
```

### Get All Devices

```bash
curl http://localhost:8000/devices
```

### Get Specific Device

```bash
curl http://localhost:8000/devices/1
```

### Create a New Device

```bash
curl -X POST "http://localhost:8000/devices" \
     -H "Content-Type: application/json" \
     -d '{
       "id": 4,
       "name": "Access-Point-01",
       "ip_address": "192.168.1.100",
       "device_type": "access_point",
       "status": "online"
     }'
```

### Update a Device

```bash
curl -X PUT "http://localhost:8000/devices/4" \
     -H "Content-Type: application/json" \
     -d '{
       "status": "offline"
     }'
```

### Get Statistics

```bash
curl http://localhost:8000/stats
```

### Delete a Device

```bash
curl -X DELETE "http://localhost:8000/devices/4"
```

## Step 6: Advanced Testing

### Test with Pretty JSON Output

```bash
# Install jq for pretty JSON (optional)
# On Windows: choco install jq
# On macOS: brew install jq
# On Linux: apt-get install jq

curl http://localhost:8000/devices | jq '.'
```

### Load Testing (Simple)

```bash
# Test multiple requests
for i in {1..10}; do
  curl -s http://localhost:8000/health
  echo "Request $i completed"
done
```

### View Container Logs

```bash
docker logs network-api
```

### Execute Commands in Running Container

```bash
docker exec -it network-api /bin/bash
```

## Step 7: Docker Compose (Optional)

Create **docker-compose.yml** for easier management:

```yaml
version: '3.8'

services:
  api:
    build: .
    ports:
      - "8000:8000"
    environment:
      - ENV=development
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8000/health"]
      interval: 30s
      timeout: 10s
      retries: 3
    restart: unless-stopped

  nginx:
    image: nginx:alpine
    ports:
      - "80:80"
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf:ro
    depends_on:
      - api
```

### Run with Docker Compose

```bash
# Start services
docker-compose up -d

# View logs
docker-compose logs -f

# Stop services
docker-compose down
```

## Exercise Tasks

Complete these tasks to master FastAPI containerization:

### Basic Tasks

- [ ] Create the FastAPI application files
- [ ] Build the Docker image
- [ ] Run the container with port mapping
- [ ] Test the health check endpoint with cURL

### API Testing Tasks

- [ ] Get all devices using cURL
- [ ] Create a new device via API
- [ ] Update an existing device
- [ ] Delete a device
- [ ] Check device statistics

### Container Management

- [ ] View container logs
- [ ] Stop and restart the container
- [ ] Execute commands inside the running container
- [ ] Monitor container resource usage

### Advanced Tasks (Optional)

- [ ] Create the Docker Compose configuration
- [ ] Add environment variable configuration
- [ ] Implement container health checks
- [ ] Test load balancing with multiple containers

## Key Learning Points

### FastAPI Benefits

- **Automatic API documentation** (Swagger UI at /docs)
- **Type validation** with Pydantic models
- **High performance** (comparable to Node.js and Go)
- **Modern Python** features (async/await, type hints)

### Container Best Practices

- **Multi-stage builds** for smaller images
- **Non-root users** for security
- **Health checks** for monitoring
- **Proper port exposure** for web services

### API Development Patterns

- **RESTful design** with proper HTTP methods
- **Request/response models** for validation
- **Error handling** with appropriate HTTP status codes
- **Documentation** generation from code

## Troubleshooting

### Common Issues

- **Port already in use**: Stop conflicting services or use different ports
- **Connection refused**: Check if container is running and ports are mapped
- **Import errors**: Verify requirements.txt includes all dependencies
- **Permission denied**: Ensure proper file permissions and user configuration

### Debugging Commands

```bash
# Check container status
docker ps -a

# View detailed container info
docker inspect network-api

# Check port mappings
docker port network-api

# Monitor container stats
docker stats network-api

# View container filesystem
docker exec -it network-api ls -la /app
```

### Testing Tips

- Use `curl -v` for verbose output to debug HTTP issues
- Test endpoints individually before running complex scenarios
- Check container logs if API returns unexpected results
- Use browser dev tools to inspect API responses

## Production Considerations

### Security Enhancements

- Use secrets management for sensitive data
- Implement authentication and authorization
- Add rate limiting and input validation
- Use HTTPS with proper certificates

### Performance Optimization

- Enable caching for frequently accessed data
- Use connection pooling for databases
- Implement proper logging and monitoring
- Consider using a reverse proxy (nginx)

### Deployment Strategies

- Use container orchestration (Kubernetes, Docker Swarm)
- Implement CI/CD pipelines
- Set up monitoring and alerting
- Plan for horizontal scaling

## Next Steps

After completing this FastAPI container project:

1. Explore the interactive API documentation at `/docs`
2. Add database integration (PostgreSQL, MongoDB)
3. Implement authentication with JWT tokens
4. Add comprehensive testing with pytest
5. Deploy to cloud platforms (AWS, GCP, Azure)

This project provides a solid foundation for building and containerizing modern web APIs for network automation and management tasks.
