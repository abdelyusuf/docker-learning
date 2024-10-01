# Use the smaller, official Python Alpine base image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file first (for dependency caching)
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir flask redis

# Copy the current directory contents into the container
COPY . .

# Expose the Flask app port
EXPOSE 5002

# Define environment variable for Flask
ENV FLASK_APP=app.py

# Run the Flask application
CMD ["flask", "run", "--host=0.0.0.0", "--port=5002"]
