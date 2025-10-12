# Exercise 1: Docker Installation Guide

## Overview

Before we can work with Docker containers, we need to install and verify Docker on our system. This guide covers installation for Windows, macOS, and Linux systems.

## Installation Instructions

### Windows Installation

#### Docker Desktop for Windows

1. Visit the official Docker website: [https://docs.docker.com/docker-for-windows/install/](https://docs.docker.com/docker-for-windows/install/)
2. Download Docker Desktop for Windows
3. Run the installer as Administrator
4. Follow the installation wizard
5. Restart your computer when prompted

#### System Requirements

- Windows 10 64-bit: Pro, Enterprise, or Education
- Hyper-V and Containers Windows features must be enabled
- BIOS-level hardware virtualization support

### macOS Installation

#### Docker Desktop for Mac

1. Visit: [https://docs.docker.com/docker-for-mac/install/](https://docs.docker.com/docker-for-mac/install/)
2. Download Docker Desktop for Mac
3. Double-click the downloaded `.dmg` file
4. Drag Docker to Applications folder
5. Launch Docker from Applications

### Linux Installation (Ubuntu/Debian)

```bash
# Update package index
sudo apt-get update

# Install packages to allow apt to use repository over HTTPS
sudo apt-get install \
    ca-certificates \
    curl \
    gnupg \
    lsb-release

# Add Docker's official GPG key
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

# Set up stable repository
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# Install Docker Engine
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io

# Add user to docker group (optional - allows running without sudo)
sudo usermod -aG docker $USER
```

## Verification Steps

After installation, verify Docker is working correctly:

### 1. Check Docker Version

```bash
docker --version
```

Expected output should show Docker version information.

### 2. Check Docker Info

```bash
docker info
```

This displays system-wide information about Docker installation.

### 3. Test Docker Installation

```bash
docker run hello-world
```

This command downloads and runs a test container that verifies your installation.

## Troubleshooting Common Issues

### Windows Issues

- **Hyper-V not enabled**: Enable Hyper-V in Windows Features
- **Virtualization not enabled**: Enable in BIOS/UEFI settings
- **WSL 2 required**: Install Windows Subsystem for Linux 2

### macOS Issues

- **Permission denied**: Make sure Docker Desktop is running
- **Resource limits**: Adjust memory/CPU allocation in Docker Desktop preferences

### Linux Issues

- **Permission denied**: Add user to docker group or use sudo
- **Service not running**: Start Docker service with `sudo systemctl start docker`

## Exercise Checklist

Complete these verification steps:

- [ ] Docker is installed on your system
- [ ] `docker --version` returns version information
- [ ] `docker info` displays system information without errors
- [ ] `docker run hello-world` executes successfully
- [ ] Docker Desktop is running (Windows/macOS)
- [ ] You can run Docker commands without errors

## Next Steps

Once Docker is successfully installed and verified, proceed to [Exercise 2: Basic Docker Commands](02-basic-commands.md) to start learning fundamental Docker operations.

## Additional Resources

- [Official Docker Documentation](https://docs.docker.com/)
- [Docker Desktop User Manual](https://docs.docker.com/desktop/)
- [Docker Engine Installation](https://docs.docker.com/engine/install/)
