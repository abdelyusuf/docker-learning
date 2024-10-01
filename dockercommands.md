# Docker Commands Reference

This document provides a collection of commonly used Docker commands along with their descriptions. Use this guide to help you manage your Docker containers, images, and volumes effectively.

## Basic Commands

### 1. Docker Version
Check the installed version of Docker.

```bash
docker --version
```

### 2. List Docker Images
List all Docker images on your machine.

```bash
docker images
```

### 3. List Running Containers
Show all currently running Docker containers.

```bash
docker ps
```

### 4. List All Containers
Show all containers, including those that are stopped.

```bash
docker ps -a
```

### 5. Pull an Image
Download a Docker image from Docker Hub.

```bash
docker pull <image-name>
```

### 6. Run a Container
Create and start a new container from an image.

```bash
docker run <options> <image-name>
```

### 7. Stop a Running Container
Stop a running container.

```bash
docker stop <container-id>
```

### 8. Remove a Container
Remove a stopped container.

```bash
docker rm <container-id>
```

### 9. Remove an Image
Delete an image from your local machine.

```bash
docker rmi <image-name>
```

## Docker Compose Commands

### 10. Build Docker Containers
Build or rebuild services defined in the `docker-compose.yml` file.

```bash
docker-compose build
```

### 11. Start Services
Start all services defined in the `docker-compose.yml` file.

```bash
docker-compose up
```

### 12. Start Services in Detached Mode
Start services in the background (detached mode).

```bash
docker-compose up -d
```

### 13. Stop Services
Stop running services without removing containers.

```bash
docker-compose stop
```

### 14. Stop and Remove Services
Stop and remove all services and their containers.

```bash
docker-compose down
```

### 15. View Logs
View logs from all services or a specific service.

```bash
docker-compose logs              # All services
docker-compose logs <service>    # Specific service
```

## System Management Commands

### 16. Clean Up Docker Resources
Remove unused data, including stopped containers and unused images.

```bash
docker system prune
```

### 17. Remove All Unused Images and Volumes
Remove all unused images and volumes from your system.

```bash
docker system prune -a --volumes
```

## Troubleshooting Tips

- **Check Container Status**: If a container is not starting, use `docker logs <container-id>` to check its logs for errors.
- **Resource Usage**: Use `docker stats` to monitor the resource usage of running containers.
- **Inspect Container**: Get detailed information about a container with `docker inspect <container-id>`.


