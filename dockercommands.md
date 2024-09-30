# Flask & Redis Multi-Container Application

This project sets up a multi-container application using Docker Compose. It consists of a Flask web application and a Redis database. The Flask app interacts with Redis to store and retrieve the visit count.

## Prerequisites

- [Docker](https://docs.docker.com/get-docker/) installed
- [Docker Compose](https://docs.docker.com/compose/install/) installed

## Project Structure

```
.
├── app.py               # Flask web application
├── Dockerfile           # Dockerfile to build the Flask app image
├── requirements.txt     # Python dependencies
├── docker-compose.yml   # Docker Compose configuration file
└── README.md            # This README file
```

## Setup Instructions

### 1. Clone the Repository

```bash
git clone <repository-url>
cd <repository-directory>
```

### 2. Build and Run the Application

To build the Docker images and start the containers:

```bash
docker-compose up --build
```

- This command builds the Flask app image and starts both the Flask app and Redis containers.

### 3. Access the Application

Once the containers are up and running, you can access the application by navigating to the following URLs in your web browser:

- Flask welcome page: [http://localhost:5002](http://localhost:5002)
- Visit count page: [http://localhost:5002/count](http://localhost:5002/count)

### 4. Stopping the Application

To stop and remove the containers without removing the built images:

```bash
docker-compose down
```

### 5. Useful Docker Commands

Here are some common Docker and Docker Compose commands that are useful for managing the application:

#### Build the Docker Containers
```bash
docker-compose build
```

#### Start the Containers in the Background (Detached Mode)
```bash
docker-compose up -d
```

#### View Logs for All Services
```bash
docker-compose logs
```

#### View Logs for a Specific Service (e.g., web)
```bash
docker-compose logs web
```

#### Stop the Running Containers
```bash
docker-compose down
```

#### Stop Containers and Remove Volumes
```bash
docker-compose down --volumes
```

#### Rebuild Containers Without Using Cache
```bash
docker-compose build --no-cache
```

#### List Running Containers
```bash
docker ps
```

#### Check Container Resource Usage
```bash
docker stats
```

#### Clean Up Docker Resources (Unused Images, Containers, Volumes)
```bash
docker system prune -a --volumes
```

### 6. Removing All Containers and Images

To remove all containers, networks, and images associated with the application:

```bash
docker-compose down --rmi all --volumes
```

This command removes all images and volumes created by the Compose file, freeing up space on your system.

## Troubleshooting

- **Port Conflict**: If port `5002` or `6379` is already in use, modify the `docker-compose.yml` file to use a different port.
- **Docker Issues**: If you're facing slow builds or container startup, try cleaning up unused resources with `docker system prune -a --volumes`.

