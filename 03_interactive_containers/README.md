# 03: Interactive Containers - Peek Inside the Box

## 🎯 Mission

Step inside a running container and explore its environment! Learn to use interactive and detached modes while discovering how containers provide isolated, lightweight environments.

## 🎖 Goals

- [ ] Use the run command with interactive and terminal flags
- [ ] Explore a container's file system through hands-on commands  
- [ ] Practice the exec command to access running containers
- [ ] Understand container isolation by comparing to host system
- [ ] Learn the difference between interactive and detached modes

## 💡 Key Concepts

**Interactive Mode (`-i`)**: Keeps container's input stream open  
**Terminal Mode (`-t`)**: Allocates a pseudo-terminal (TTY)  
**Combined (`-it`)**: Interactive terminal for shell access  
**Detached Mode (`-d`)**: Runs container in background  
**Container Isolation**: Containers can't see your host system files

## 🔍 Command Discovery First

### Task 1: Discover Interactive Options

Before running containers, let's explore the options:

```bash
# Explore the run command options
docker run --help
```

**🎯 Find these flags in the help output:**
- What does `-i` or `--interactive` do?
- What does `-t` or `--tty` do? 
- What does `-d` or `--detach` do?
- What does `--name` allow you to do?

## 🚀 Interactive Container Exploration

### Task 2: Launch Interactive Ubuntu Container

Use the Docker run command to start an Ubuntu container in interactive terminal mode:

```bash
# Use run with interactive and terminal flags to start Ubuntu with bash shell
docker run -it ubuntu bash
```

> **You're in!** Notice your command prompt changed? You're now running commands inside the Ubuntu container, not your host system.

**Inside the container, explore with these commands:**

```bash
# See what Linux distribution you're running  
cat /etc/os-release

# Check what's in the root directory
ls /

# See what user you are
whoami

# Check available disk space  
df -h

# See running processes
ps aux

# Try to access what would be your host home directory
ls /home

# Exit the container when done exploring
exit
```

### Task 3: Learn Container States

**🎯 Discovery Challenge**: Find commands to investigate containers

1. **After exiting, check what happened to your container:**
   - Use the command that lists all containers (including stopped ones)
   - What's the STATUS of your Ubuntu container?

2. **Find the remove command:**
   - Use `docker --help` to find the command that removes containers
   - Remove your stopped Ubuntu container by ID or name

### Task 4: Practice Detached Mode 

**Launch a container that keeps running in the background:**

```bash
# Use run with detached, interactive, terminal flags and a custom name
docker run -dit --name ubuntu-explorer ubuntu bash
```

**🎯 Discovery Challenge**: 
1. **Find the command to list running containers** - Is your ubuntu-explorer running?
2. **Find the exec command** - Use `docker --help` to locate it
3. **Use exec to connect to the running container:**

```bash
# Use exec with interactive and terminal flags to access the running container  
docker exec -it ubuntu-explorer bash
```

### Task 5: Compare Container vs Host

**Inside your running container, try these explorations:**

```bash
# Install something temporarily
apt update
apt install -y curl tree

# Test the new tools
curl --version
tree --version

# Create a test file
echo "I was here!" > /tmp/container-file.txt
cat /tmp/container-file.txt

# Exit but don't stop the container
exit
```

**Back on your host system:**

```bash  
# Try to find the file you created (it won't be there!)
cat /tmp/container-file.txt  # This will fail

# Connect back to the same container
docker exec -it ubuntu-explorer bash

# Inside again - is your file still there?
cat /tmp/container-file.txt  # This should work!
exit
```

## 🎯 Command Practice Challenges

### Challenge 1: Multiple Container Management

**Use command discovery to complete these tasks:**

1. **Start 3 different containers with custom names:**

```bash
# Run these containers in detached mode with custom names
docker run -dit --name container1 ubuntu bash
docker run -dit --name container2 alpine sh  
docker run -dit --name container3 debian bash
```

2. **Use the appropriate commands to:**
   - List all running containers
   - Connect to each container and run `whoami`
   - Stop all three containers
   - Remove all three containers

### Challenge 2: Container Persistence Exploration

**Goal**: Understand what persists and what doesn't

1. **Create a container with modifications:**

```bash
# Start a named container
docker run -dit --name persistence-test ubuntu bash

# Connect and make changes
docker exec -it persistence-test bash

# Inside the container:
apt update && apt install -y nano
echo "persistent data" > /tmp/test.txt
exit
```

2. **Test persistence:**

```bash
# Stop the container
docker stop persistence-test

# Start it again  
docker start persistence-test

# Connect and check if changes survived
docker exec -it persistence-test bash
# Inside: Check if nano and test.txt are still there
nano --version
cat /tmp/test.txt
exit
```

## 🎉 Success Criteria

You've mastered interactive containers when you can:

- Use `docker run -it` to start interactive containers
- Use `docker run -dit` to start detached containers  
- Use `docker exec -it` to access running containers
- Understand that container changes persist while the container exists
- Stop, start, and remove containers using appropriate commands

## 🔧 Interactive Command Patterns

```bash
# Interactive patterns:
docker run -it [image] [command]           # Run and interact immediately
docker run -dit --name [name] [image] [cmd] # Run detached with name
docker exec -it [container] [command]      # Connect to running container

# Management patterns:
docker ps                    # See running containers
docker ps -a                # See all containers  
docker stop [container]     # Stop running container
docker start [container]    # Start stopped container
docker rm [container]       # Remove stopped container
```

## 🔍 Check Yourself

1. **What's the difference between `docker run -it` and `docker run -dit`?**
2. **When would you use `docker exec` instead of `docker run`?** 
3. **What happens to files you create inside a container when you remove it?**
4. **How can you tell if a container is running vs stopped?**

## 💡 Real-World Applications

**Why interactive containers matter:**
- **Debugging**: Jump into containers to troubleshoot issues
- **Development**: Test applications in clean, isolated environments  
- **Exploration**: Try different Linux distributions safely
- **Maintenance**: Access running services for configuration or updates

## 🚀 Ready for More?

Perfect! You can now work with containers interactively and understand their isolation. Time to create your own custom containers in **[04_basic_images](../04_basic_images/README.md)**!

---

> **Container mastery unlocked!** 🔓 You now understand the difference between your host system and container environments. This isolation is what makes containers so powerful for development and deployment!