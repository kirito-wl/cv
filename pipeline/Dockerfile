# Start with the official Jenkins Docker image version 2.375.2 as the base - latest LTS release
FROM jenkins/jenkins:2.375.2

# Change the user to root to perform administrative tasks
USER root

# Update the package list and install lsb-release, which is used to determine the Debian version number
RUN apt-get update && apt-get install -y lsb-release

# Download the Docker GPG key, which will be used to verify the authenticity of the Docker package
RUN curl -fsSLo /usr/share/keyrings/docker-archive-keyring.asc https://download.docker.com/linux/debian/gpg

# Add the Docker repository to the list of sources used by apt-get
RUN echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.asc] https://download.docker.com/linux/debian $(lsb_release -cs) stable" > /etc/apt/sources.list.d/docker.list

# Update the package list and install the Docker CLI
RUN apt-get update && apt-get install -y docker-ce-cli

# Change the user back to jenkins to run Jenkins as the primary user
USER jenkins

# Install the Blue Ocean and Docker Workflow plugins via the Jenkins CLI
RUN jenkins-plugin-cli --plugins "blueocean docker-workflow"
