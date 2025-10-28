"""
TODO: Complete this FastAPI network automation service
Hint: Create endpoints for network utilities and dad jokes!
"""

from fastapi import FastAPI, HTTPException
import requests
import json
import random
from datetime import datetime

# TODO: Create FastAPI app instance
app = FastAPI()

# Sample network data for demos
SAMPLE_DEVICES = [
    {"hostname": "router-01", "ip": "192.168.1.1", "type": "router", "status": "up"},
    {"hostname": "switch-01", "ip": "192.168.1.10", "type": "switch", "status": "up"},
    {"hostname": "switch-02", "ip": "192.168.1.11", "type": "switch", "status": "down"},
    {"hostname": "firewall-01", "ip": "192.168.1.100", "type": "firewall", "status": "up"},
]

@app.get("/")
def read_root():
    """
    TODO: Create welcome endpoint
    Hint: Return a welcome message with API information
    """
    # TODO: Return welcome message and available endpoints
    pass

@app.get("/health")
def health_check():
    """
    TODO: Create health check endpoint
    Hint: Return service status and current time
    """
    # TODO: Return health status with timestamp
    pass

@app.get("/devices")
def get_devices():
    """
    TODO: Return list of network devices
    Hint: Return the SAMPLE_DEVICES list
    """
    # TODO: Return all devices
    pass

@app.get("/devices/{device_type}")
def get_devices_by_type(device_type: str):
    """
    TODO: Filter devices by type (router, switch, firewall)
    Hint: Filter SAMPLE_DEVICES by the device_type parameter
    """
    # TODO: Filter and return devices of specified type
    pass

@app.get("/joke")
def get_network_joke():
    """
    TODO: Return a networking-themed joke
    Hint: Either fetch from API or return from local list
    """
    local_jokes = [
        {"setup": "Why do routers never get lost?", "punchline": "Because they always know the route!"},
        {"setup": "What's a network engineer's favorite type of music?", "punchline": "Heavy bandwidth!"},
        {"setup": "Why don't firewalls ever feel lonely?", "punchline": "Because they're always blocking connections!"},
    ]
    # TODO: Return a random joke or fetch from API
    pass

@app.get("/ping/{host}")
def simulate_ping(host: str):
    """
    TODO: Simulate a ping command (for demo purposes)
    Hint: Return fake ping statistics for the given host
    """
    # TODO: Generate fake but realistic ping results
    pass

@app.get("/port-scan/{host}")
def simulate_port_scan(host: str, ports: str = "22,80,443,8080"):
    """
    TODO: Simulate a port scan (for educational purposes)
    Hint: Parse the ports parameter and return fake scan results
    """
    # TODO: Parse ports and return mock scan results
    pass

if __name__ == "__main__":
    import uvicorn
    # TODO: Run the server
    # Hint: uvicorn.run(app, host="0.0.0.0", port=8000)
    pass