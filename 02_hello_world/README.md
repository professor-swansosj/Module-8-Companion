# 02: Hello World - Your First Container

## 🎯 Mission

Experience the magic of containers by running Docker's famous "hello-world" container. This simple container will prove your Docker setup works and show you the basic container lifecycle.

## 🎖 Goals

- [ ] Successfully run your first container using the run command
- [ ] Understand the container lifecycle through observation
- [ ] Practice container management commands you discovered in Module 01
- [ ] Learn to give containers custom names and manage them

## 💡 Key Concepts

**Container Lifecycle**: Pull → Create → Start → Run → Stop → Remove  
**Automatic Pulling**: Docker downloads images you don't have locally  
**Container Names**: You can assign custom names for easier management  
**Container States**: Containers can be running, stopped, or removed

## 🚀 The Classic Hello World

### Step 1: Run Your First Container

Use the Docker run command to execute the hello-world container:

```bash
docker run hello-world
```

**What just happened?**

1. Docker looked for "hello-world" image locally
2. Didn't find it, so downloaded from Docker Hub  
3. Created a container from the image
4. Ran the container (which prints a message)
5. Container exited automatically

> **Success!** You just ran your first containerized application!

### Step 2: Investigate the Results

Use the commands you learned in Module 01 to see what happened:

**🎯 Challenge**: Use `--help` to find the right commands and flags:

1. **Check if the hello-world image was downloaded**
   - Hint: Use the command that lists images on your system

2. **See the container that just ran (even though it stopped)**  
   - Hint: Use the command that shows containers, with the flag for ALL containers

```bash
# Fill in these commands using what you learned:
docker [command to list images]
docker [command to show all containers with the right flag]
```

### Step 3: Practice Container Management

**Run hello-world with a custom name:**

```bash
# Use the run command with the name option to create a named container
docker run --name my-first-container hello-world
```

> **Discover**: Use `docker run --help` to see what the `--name` option does!

**Check your named container:**

```bash
# Use the container listing command to see your named container
docker [fill in the command and flag]
```

## 🎯 Command Discovery Challenges

**Use only Docker's help system to complete these:**

### Challenge 1: Container Investigation

**Goal**: Learn about the containers on your system

1. **Find the command to list containers**

   - Use `docker --help` to find it
   - Run `docker [command] --help` to see the options
   - What flag shows ALL containers (not just running ones)?

2. **Run the command and observe the output**
   - What columns do you see?
   - What's the STATUS of your hello-world containers?

### Challenge 2: Image Management

**Goal**: Understand images vs containers

1. **Find the command to list images**
   - Look in `docker --help` for image-related commands
   - Run the command - is hello-world there now?

2. **Explore the pull command**  
   - Use `docker pull --help` to understand this command
   - Try: `docker pull hello-world` (even though you already have it)

### Challenge 3: Container Cleanup

**Goal**: Learn to remove containers

1. **Find the command to remove containers**
   - Hint: Look for "remove" or "rm" in `docker --help`
   - Check `docker [command] --help` to see the syntax

2. **Remove your named container**
   - Use: `docker [remove command] my-first-container`
   - Verify it's gone with the list command

## 🎯 Practice Scenarios

**Complete these using command discovery:**

### Scenario 1: Multiple Runs

```bash
# Run hello-world 3 times with different names
docker run --name hello-1 hello-world  
docker run --name hello-2 hello-world
docker run --name hello-3 hello-world

# Use the list command to see all three
docker [fill in command and flag]
```

### Scenario 2: Cleanup Operations

```bash
# Remove specific containers (find the remove command first!)
docker [remove command] hello-1
docker [remove command] hello-2  
docker [remove command] hello-3

# Verify they're gone
docker [list command with flag]
```

## 🎉 Success Criteria

You've mastered hello-world when you can:

- Run the hello-world container successfully
- Use the correct commands to list images and containers
- Create containers with custom names using the `--name` flag  
- Remove specific containers using the remove command
- Explain the difference between images and containers

## 🔧 Troubleshooting

### "docker: command not found"

- Docker might not be installed or not in your PATH
- Check with `docker --version`

### "Cannot connect to the Docker daemon"

- Docker service isn't running
- Start Docker Desktop or Docker service

### "docker: Error response from daemon"

- Usually a syntax error in your command
- Double-check the command format with `--help`

## 🔍 Check Yourself

1. **What's the difference between `docker images` and `docker ps -a`?**
2. **Why is running hello-world the second time faster?**  
3. **What happens to containers after they finish running?**
4. **How do you remove a container with a specific name?**

## 💡 Command Pattern Recognition

Notice how Docker commands follow patterns:

```bash
# List things:
docker images        # Lists images  
docker ps           # Lists running containers
docker ps -a        # Lists all containers

# Remove things:
docker rm [container]    # Remove containers
docker rmi [image]      # Remove images  

# Run things:
docker run [image]              # Basic run
docker run --name [name] [image] # Run with custom name
```

## 🚀 Ready for More?

Perfect! You can now run containers and manage them with command-line tools. Next, let's explore what's inside containers with **[Section 03: Interactive Containers](../03_interactive_containers/README.md)**!

---

> **Celebrate!** 🎉 You just mastered Docker's most fundamental operation! Every containerized application starts with a `docker run` command, and you now understand the entire lifecycle!
