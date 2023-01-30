# Use the Alpine Linux image as the base image
FROM alpine:latest

# Install pandoc and all its dependencies
RUN apk add --no-cache pandoc
RUN apk add --no-cache texlive-xetex
RUN apk add --no-cache texlive-fonts
RUN apk add --no-cache texlive-latex

# Copy the Python script to the container
COPY converter.py /app/

# Set the working directory to where the script is located
WORKDIR /app/

# Run the script and pass in the necessary arguments
CMD ["python3", "converter.py", "input_file.md", "output_file.pdf"]

# When the script is done running, shutdown the container
CMD ["shutdown", "-h", "now"]