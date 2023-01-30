#!/bin/bash

# Clone the GitHub repository containing the files to be used
git clone https://github.com/kirito-wl/cv.git

# Navigate to the local-wip directory within the cloned repository
cd cv/local-wip

# Build a Docker image using the Dockerfile in the local-wip directory
docker build -t converter-image .

# Run a container from the newly created Docker image
docker run -d --name converter-container -v "$PWD":/app converter-image

# Execute the converter.py file within the container
docker exec converter-container python /app/converter.py

# Stop and remove the container
docker stop converter-container && docker rm converter-container

# Copy the outputted PDF file back to the local-wip directory on the host machine
docker cp converter-container:/app/Will-CV.pdf /Users/will.louzado/repos/cv/local-wip/Will-CV.pdf

# Open the PDF file
open /Users/will.louzado/repos/cv/local-wip/Will-CV.pdf