# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the service account key into the container
COPY llm-hackathon-pr-agent-plus-f9022659b239.json /app/service-account-key.json

# Set the environment variable for the service account
ENV GOOGLE_APPLICATION_CREDENTIALS /app/service-account-key.json

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV NAME World

# Run start.sh when the container launches
CMD ["sh", "start.sh"]