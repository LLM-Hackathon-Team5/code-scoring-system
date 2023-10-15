# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container to /app
WORKDIR /code-scoring-system

# Copy the current directory contents into the container at /app
COPY . /code-scoring-system

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the service account key into the container
COPY llm-hackathon-pr-agent-plus-f9022659b239.json /app/service-account-key.json

# Set the environment variable for the service account
ENV GOOGLE_APPLICATION_CREDENTIALS /app/service-account-key.json

# Make port 80 available to the world outside this container
EXPOSE 8080

# 環境変数の追加
ENV PALM2_BASE_URL=https://generativelanguage.googleapis.com
ENV PALM2_MODEL_PATH=/v1beta2/models/text-bison-001:generateText


# Run start.sh when the container launches
CMD ["sh", "start.sh"]