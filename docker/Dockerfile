# Use the official Alpine Linux image as the base image
FROM alpine:latest

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install the necessary dependencies
RUN apk add --no-cache build-base python3-dev libffi-dev openssl-dev wkhtmltopdf

# Install the python packages
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy the script to the working directory
COPY convert_md_to_pdf.py .

# Run the script
CMD ["python3", "convert_md_to_pdf.py"]
