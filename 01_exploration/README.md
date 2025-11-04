# 01: Docker Exploration - Your First Steps

## 🎯 Mission

Discover Docker's essential commands through guided exploration! You'll learn to use Docker's built-in help system to find what you need—just like you learned with Linux commands.

## 🎖 Goals

- [ ] Verify Docker is working on your system
- [ ] Master Docker's help system for self-discovery
- [ ] Learn the core Docker commands through exploration
- [ ] Understand Docker's command structure and subcommands

## 💡 Key Concepts

**Docker Image**: A blueprint or template for creating containers (like a recipe)  
**Docker Container**: A running instance of an image (like a meal made from the recipe)  
**Docker Hub**: Online repository where people share Docker images  
**Subcommands**: Docker uses subcommands like `docker run`, `docker build`, `docker ps`

## 🔍 Learning Docker's Help System

### Task 1: Docker Health Check

First, let's make sure Docker is ready for action:

```bash
# Check Docker version
docker --version

# Verify Docker is running
docker info
```

> **What do you see?** Docker should show version info and system details. If you get errors, Docker might not be running.

### Task 2: Discover Docker Commands

Docker has excellent built-in help. This is your most important skill:

```bash
# See all available Docker commands and subcommands
docker --help
```

> **Study the output!** You'll see sections like "Management Commands" and "Commands". Each one has a brief description.

**Now pick 3 commands that sound interesting and explore them:**

```bash
# Get detailed help for any command
docker run --help
docker images --help
docker ps --help
```

### Task 3: Practice Command Discovery

**🎯 Challenge**: Use only the `--help` flag to answer these questions:

1. **How do you list all Docker images on your system?**
   - Hint: Look for a command related to "images"
   - Run `docker [command] --help` to see the options

2. **How do you see running containers?**
   - Hint: Look for a command that "lists" or shows "processes"
   - Check what flags show ALL containers (not just running ones)

3. **How do you search for images on Docker Hub?**
   - Hint: Look for a "search" command
   - Try searching for "nginx" or "python"

## 🛠 Hands-On Exploration

### Task 4: System Investigation

Now use what you discovered to investigate your system:

**Check your current Docker state:**

```bash
# Use the command you found to list images
docker [fill in the command]

# Use the command to see all containers 
docker [fill in the command with the right flag]

# Search for popular images
docker [fill in the search command] ubuntu
docker [fill in the search command] python
```

### Task 5: Learn Docker Command Patterns

Docker follows consistent patterns. Explore these:

```bash
# Most Docker commands follow this pattern:
# docker [COMMAND] [OPTIONS] [ARGUMENTS]

# Try these and notice the patterns:
docker --help                    # Global help
docker images --help            # Specific command help
docker ps --help               # Another command help
```

## 🎯 Discovery Challenges

**Complete these using ONLY the `--help` system:**

### Challenge 1: Container Investigation

- Find the command to see ALL containers (running and stopped)
- Discover what the `-a` flag does by reading the help
- Learn what `-q` flag does (you'll use this later!)

### Challenge 2: Image Exploration  

- Find the command to list local images
- Discover how to see image sizes and creation dates
- Learn what the `-q` flag does for images

### Challenge 3: Search and Discovery

- Find how to search Docker Hub for images
- Try searching for "nginx", "python", and "hello-world"
- Notice how results are formatted and sorted

## 🎉 Success Criteria

You've mastered Docker exploration when you can:

- Use `docker --help` to find any command you need
- Understand the difference between management commands and regular commands  
- Navigate Docker's help system confidently
- Find specific flags and options for any Docker command

## 🔍 Check Yourself

1. **What command shows running containers?** Use `--help` to find it!
2. **How do you see ALL containers, not just running ones?** What flag do you add?
3. **What's the difference between `docker images` and `docker search`?**
4. **How can you get help for any Docker subcommand?**

## 💡 Pro Tips

**Remember from your Linux training:**

- Use `--help` when you're not sure about a command
- Read the SYNOPSIS section to understand command structure
- Pay attention to [OPTIONAL] vs required parameters
- Many commands have short flags (`-a`) and long flags (`--all`)

## 🚀 Ready for More?

Perfect! You now know how to discover Docker commands on your own. Time to go to **[Section 02: Hello World](../02_hello_world/README.md)** and run your first container using what you've learned!

---

> **You're building independence!** 🎓 Just like with Linux commands, Docker's help system is your best friend. When in doubt, add `--help`!
