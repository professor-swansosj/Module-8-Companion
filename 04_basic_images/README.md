# 04: Basic Images - Create Your First Custom Container

## 🎯 Mission

Build your first custom Docker image! Create a Dockerfile and use the build command to package your own ASCII art application into a portable container.

## 🎖 Goals

- [ ] Understand what a Dockerfile is and how to write one
- [ ] Use the build command to create custom images  
- [ ] Learn Dockerfile instructions through guided discovery
- [ ] Run containers from your custom-built images
- [ ] Practice image management with command-line tools

## 💡 Key Concepts

**Dockerfile**: Text file with instructions to build an image  
**Base Image**: Starting point for your custom image (like `python:3.11`)  
**Build Context**: Directory containing files Docker can access during build  
**Image Tags**: Names and versions for your images (like `my-app:v1.0`)

## 🔍 Dockerfile Command Discovery

### Task 1: Explore the Build Command

Before creating images, let's understand the build process:

```bash
# Explore the build command options
docker build --help
```

**🎯 Find these in the help output:**

- What does the `-t` or `--tag` flag do?
- What does the `.` (dot) represent at the end of build commands?
- What does `-f` allow you to specify?

## 🎨 Your First Custom Image

### Step 1: Learn ASCII Art Generation

Before coding, let's explore how to create ASCII art! You have several options:

#### Option A: Use Command-Line Tools (Linux/WSL)

**Install ASCII art generators:**

```bash
# On Ubuntu/Debian (if using WSL)
sudo apt update
sudo apt install toilet figlet

# Generate ASCII art with toilet
toilet "Docker"
toilet -f mono12 "Network"

# Generate ASCII art with figlet  
figlet "Containers"
figlet -f big "FSCJ"
```

#### Option B: Use Online Generators

**Web-based ASCII generators (copy and paste results):**

- **Text to ASCII**: <https://patorjk.com/software/taag/>
- **ASCII Art Generator**: <https://www.asciiart.eu/text-to-ascii-art>
- **FIGlet Fonts**: <http://www.figlet.org/examples.html>

**🎯 Try These Examples:**

1. Go to <https://patorjk.com/software/taag/>
2. Type "Docker" or your name
3. Try different fonts like "Big", "Block", "Slant"
4. Copy the result for use in your Python code

#### Option C: PowerShell ASCII Art

**Create simple ASCII art in PowerShell:**

```powershell
# Generate simple text art
Write-Host @"
 ____             _              
|  _ \  ___   ___| | _____ _ __ 
| | | |/ _ \ / __| |/ / _ \ '__|
| |_| | (_) | (__|   <  __/ |   
|____/ \___/ \___|_|\_\___|_|   
"@
```

### Step 2: Test Your ASCII Art First

**🎯 Pro Tip**: Test your ASCII art before containerizing:

```bash
# Test your Python script directly first
python ascii_art.py

# This helps you debug ASCII formatting before building containers
```

**Common ASCII Art Tips:**

- Escape backslashes: `\` becomes `\\` in Python strings
- Test triple-quoted strings for proper formatting
- Keep ASCII art under 80 characters wide for better display

### Step 3: Create the Application

Now create your Python script using the ASCII art you generated:

**File:** `ascii_art.py`

```python
"""
Network Automation ASCII Art Display
Complete the TODO items to create awesome ASCII art!
"""

def display_welcome_art():
    """
    TODO: Create an awesome welcome ASCII art
    Hint: Use triple quotes for multi-line strings
    Example themes: network devices, containers, your name
    """
    # TODO: Replace 'pass' with your ASCII art
    # Example:
    # print("""
    #  ____             _              
    # |  _ \  ___   ___| | _____ _ __ 
    # | | | |/ _ \ / __| |/ / _ \ '__|
    # | |_| | (_) | (__|   <  __/ |   
    # |____/ \___/ \___|_|\_\___|_|   
    # """)
    pass

def display_container_art():
    """
    TODO: Create Docker/container themed ASCII art
    Hint: Try drawing a simple whale (Docker's mascot) or container
    """
    # TODO: Add container-themed ASCII art
    pass

def display_network_art():
    """
    TODO: Create network equipment ASCII art  
    Hint: Draw routers, switches, or network connections
    """
    # TODO: Add network-themed ASCII art
    pass

def main():
    """Main function - calls all your art functions"""
    print("🎨 Welcome to Network Automation Containers!")
    print("=" * 50)
    
    # TODO: Call your art functions here
    display_welcome_art()
    display_container_art() 
    display_network_art()
    
    print("\n🐳 Container successfully executed!")

if __name__ == "__main__":
    main()
```

### Step 4: Learn Dockerfile Instructions

Create a `Dockerfile` (no extension) in the same directory:

**File:** `Dockerfile`

```dockerfile
# TODO: Complete this Dockerfile using the instructions below
# Hint: Each instruction creates a new layer in your image

# TODO: Choose a base image with Python installed
# Hint: Use 'FROM python:3.11-slim' for a lightweight Python environment
FROM 

# TODO: Set the working directory inside the container  
# Hint: Use 'WORKDIR /app' to set where commands run
WORKDIR 

# TODO: Copy your Python script into the container
# Hint: Use 'COPY ascii_art.py .' to copy file to current workdir
COPY 

# TODO: Set the default command to run when container starts
# Hint: Use 'CMD ["python", "ascii_art.py"]' to run your script
CMD 
```

### Step 5: Build Your First Image

**🎯 Discovery Challenge**: Use the build command you explored

```bash
# Use the build command with a tag to create your image
docker build -t my-ascii-art .

# What happened? Docker should show each step of the build process
```

**Verify your image was created:**

```bash
# Use the command to list images and find yours
docker images
```

### Step 6: Run Your Custom Container

```bash
# Use the run command with your custom image
docker run my-ascii-art

# Run it with a custom container name
docker run --name my-art-container my-ascii-art
```

## 🎯 Build Command Practice

### Challenge 1: Image Variations

**Create multiple versions of your image:**

1. **Build with different tags:**

```bash
# Build the same image with different tags
docker build -t my-ascii-art:v1.0 .
docker build -t my-ascii-art:latest .
docker build -t network-art:student-version .
```

2. **List and compare your images:**

```bash
# Use the images command to see all your tagged versions
docker images | grep ascii
docker images | grep network-art
```

### Challenge 2: Build Process Understanding

**Modify and rebuild to see Docker's caching:**

1. **Make a small change to your Python script**
2. **Rebuild the image:**

```bash
# Rebuild with the same tag
docker build -t my-ascii-art .
```

3. **Observe**: Did Docker rebuild everything or use cached layers?

### Challenge 3: Image Management

**🎯 Discovery**: Use `--help` to find these commands:

1. **Find the command to remove images**
2. **Find the command to see detailed image information**
3. **Practice image cleanup:**

```bash
# Remove specific image tags
docker [remove-image-command] my-ascii-art:v1.0

# Remove images by ID
docker [remove-image-command] [image-id]
```

## 🎯 Advanced Dockerfile Practice

### Challenge 4: Improve Your Dockerfile

**Add these improvements one by one and rebuild:**

```dockerfile
# Better Dockerfile with best practices

FROM python:3.11-slim

# Set working directory  
WORKDIR /app

# Copy application file
COPY ascii_art.py .

# Add metadata labels
LABEL maintainer="your-name"
LABEL description="Network ASCII Art Container"

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Default command
CMD ["python", "ascii_art.py"]
```

**Build the improved version:**

```bash
# Build with a new tag for the improved version
docker build -t my-ascii-art:improved .
```

## 🎉 Success Criteria

You've mastered basic image building when you can:

- Write a Dockerfile with proper instructions
- Use `docker build -t` to create tagged images
- Build multiple versions and tags of the same image
- Run containers from your custom images
- Remove images when no longer needed

## 🔧 Common Build Patterns

```bash
# Basic build patterns:
docker build -t [name] .                    # Build with name
docker build -t [name]:[tag] .             # Build with name and tag
docker build -f [Dockerfile] -t [name] .   # Build with specific Dockerfile

# Image management patterns:  
docker images                              # List all images
docker images [name]                       # List specific images
docker rmi [image]                        # Remove image
docker rmi -f [image]                     # Force remove image
```

## 🔍 Check Yourself

1. **What does the `.` at the end of `docker build -t myapp .` represent?**
2. **What happens if you build an image with a tag that already exists?**  
3. **Why do we use a base image instead of starting from scratch?**
4. **How can you see the layers that make up an image?**

## 💡 Dockerfile Best Practices

**Tips for better Dockerfiles:**

- Use specific base image versions (`python:3.11-slim`, not just `python`)
- Set a WORKDIR to organize your container filesystem  
- Copy files in logical order for better caching
- Add labels for documentation and metadata
- Use multi-stage builds for production images (advanced topic)

## 🚀 Ready for More?

Excellent! You can now create custom Docker images from scratch. Time to build something that interacts with the internet in **[Section 05: Dad Joke Container](../05_dad_joke_container/README.md)**!

---

> **You're a Docker image builder!** 🏗️ Every application you create can now be packaged into a portable, consistent container that runs anywhere Docker is installed!
