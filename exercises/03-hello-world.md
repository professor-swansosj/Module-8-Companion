# Exercise 3: Hello World Container

## Overview

The Docker "Hello World" container is a simple test container that verifies Docker is working correctly. This exercise walks you through running it and understanding what happens behind the scenes.

## Learning Objectives

- Run the official Docker Hello World container
- Understand the container lifecycle
- Analyze container output and behavior
- Practice container cleanup

## Step 1: Run Hello World Container

### Execute the Hello World Container

```bash
docker run hello-world
```

### Expected Output

You should see output similar to this:

```bash
Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker ID:
 https://hub.docker.com/

For more examples and ideas, visit:
 https://docs.docker.com/get-started/
```

## Step 2: Analyze What Happened

### Check Downloaded Images

```bash
docker images
```

You should now see the `hello-world` image in your local repository.

### Check Container Status

```bash
docker ps -a
```

You'll see the hello-world container in "Exited" status since it completed its task and stopped.

### Understanding the Process

When you ran `docker run hello-world`, Docker:

1. **Checked locally** for the hello-world image
2. **Downloaded the image** from Docker Hub (if not found locally)
3. **Created a container** from the image
4. **Executed** the container's default command
5. **Displayed the output** in your terminal
6. **Stopped the container** when the process completed

## Step 3: Multiple Runs

### Run Hello World Again

```bash
docker run hello-world
```

Notice that:

- The image is NOT downloaded again (it's cached locally)
- A NEW container is created each time
- Each container gets a unique ID

### Verify Multiple Containers

```bash
docker ps -a
```

You should see multiple hello-world containers, each with different container IDs.

## Step 4: Container Inspection

### Get Container Details

First, get a container ID from `docker ps -a`, then:

```bash
docker inspect <CONTAINER_ID>
```

This shows detailed information about the container configuration.

### View Container Logs

```bash
docker logs <CONTAINER_ID>
```

This displays the output from when the container ran.

## Step 5: Image Analysis

### Inspect the Hello World Image

```bash
docker inspect hello-world
```

Examine the image configuration and see how small it is.

### Check Image History

```bash
docker history hello-world
```

Shows the layers that make up the image.

## Step 6: Cleanup

### Remove All Hello World Containers

```bash
docker container prune
```

This removes all stopped containers (including hello-world containers).

### Alternative: Remove Specific Containers

```bash
docker rm <CONTAINER_ID1> <CONTAINER_ID2>
```

### Remove the Hello World Image

```bash
docker rmi hello-world
```

### Verify Cleanup

```bash
docker images
docker ps -a
```

The hello-world image and containers should be gone.

## Step 7: Run Hello World One More Time

### Final Test

```bash
docker run hello-world
```

Docker will download the image again and run it, proving the cleanup was successful.

## Exercise Tasks

Complete these tasks to reinforce your learning:

### Basic Operations

- [ ] Run the hello-world container
- [ ] Verify the image was downloaded
- [ ] Check that a container was created and exited
- [ ] Read and understand the hello-world output

### Analysis Tasks

- [ ] Run hello-world 3 times and count the containers created
- [ ] Inspect a hello-world container
- [ ] View the logs of a specific container
- [ ] Examine the hello-world image details

### Cleanup Practice

- [ ] Remove all stopped containers
- [ ] Remove the hello-world image
- [ ] Verify everything is cleaned up
- [ ] Run hello-world again to test re-download

## Understanding Container vs Image

### Key Concepts

**Image**:

- A read-only template used to create containers
- Contains the application code and dependencies
- Stored locally after first download
- Can be used to create multiple containers

**Container**:

- A running instance of an image
- Has its own file system, networking, and process space
- Created each time you run `docker run`
- Can be started, stopped, and removed independently

### Analogy

Think of an **image** like a recipe, and a **container** like a meal made from that recipe. You can make many meals (containers) from the same recipe (image).

## What Makes Hello World Special?

The hello-world image is designed to:

- Be extremely small (less than 2KB)
- Execute quickly and exit immediately
- Provide clear feedback about Docker's functionality
- Demonstrate the basic Docker workflow

## Common Questions

**Q: Why does hello-world exit immediately?**
A: The hello-world program prints its message and then terminates. Since the main process ends, the container stops.

**Q: Can I run hello-world interactively?**
A: No, hello-world doesn't have a shell or interactive components. It's designed to run once and exit.

**Q: Why create a new container each time?**
A: Each `docker run` command creates a new container instance. This is Docker's default behavior for isolation and consistency.

## Next Steps

Now that you understand basic container operations, move on to creating your own custom container in the [ASCII Art Container Project](../projects/ascii-art-container/README.md).
