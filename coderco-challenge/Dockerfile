# Use the smaller, official Python Alpine base image
FROM python:3.9-alpine

# Set the working directory in the container
WORKDIR /app

# Install dependencies required for building certain Python packages
RUN apk add --no-cache gcc musl-dev linux-headers

# Copy the requirements.txt file first (for dependency caching)
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container
COPY . .

# Expose the Flask app port
EXPOSE 5002

# Define environment variable for Flask
ENV FLASK_APP=app.py

# Run the Flask application
CMD ["flask", "run", "--host=0.0.0.0", "--port=5002"]
