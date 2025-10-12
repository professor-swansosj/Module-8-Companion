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