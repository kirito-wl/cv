# Digital CV

Local POC Program to take a CV in MD format, convert it to PDF and store it in a GCS Bucket.

Trigger the PDF file then being sent to Workable and selected contacts via email to update their records

Build a pipeline to auto trigger the convert and upload process on git commit

## To do:

Architecture Diagram

Terraform Modules to autobuild GCP Environment

Push the MD file to the GCS Bucket to trigger a container alpine creation for the python program to run, store the PDF in a bucket or Drive and then send via email.

Automate it all
