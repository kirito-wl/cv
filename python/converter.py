# Import the necessary libraries

# To do:
# Set up the Google Cloud Envionment and test below code
# Architecture Diagram

import pdfkit
from google.cloud import storage

# Function to convert MD file to PDF
def convert_md_to_pdf(md_file, pdf_file):
    pdfkit.from_file(md_file, pdf_file)

# Function to upload the PDF file to GCS bucket

def upload_to_gcs(pdf_file, bucket_name, destination_blob_name):
    """
    Uploads a file to the specified GCS bucket
    """
    # Create a storage client
    storage_client = storage.Client()

    # Get the specified bucket
    bucket = storage_client.bucket(bucket_name)

    # Create a blob from the PDF file
    blob = bucket.blob(destination_blob_name)

    # Upload the PDF file to GCS bucket
    blob.upload_from_filename(pdf_file)
    print(f'File {pdf_file} uploaded to {destination_blob_name}.')

if __name__ == "__main__":
    # Replace with actual paths of your MD file, desired PDF file, GCS bucket name and the path where you want to store the PDF file
    md_file = "path/to/your/file.md"
    pdf_file = "path/to/your/file.pdf"
    bucket_name = "your-gcs-bucket-name"
    destination_blob_name = "path/in/your/gcs/bucket/file.pdf"

    # Convert the MD file to PDF
    convert_md_to_pdf(md_file, pdf_file)

    # Upload the PDF file to GCS bucket
    upload_to_gcs(pdf_file, bucket_name, destination_blob_name)

    # Print a success message
    print("MD file converted to PDF and uploaded to GCS bucket successfully!")
    
