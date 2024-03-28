# Dockerfile :
# ----------
# Official Python image as the base image
FROM python:3.9

# Sent output to the terminal
ENV PYTHONUNBUFFERED = 1

# Set the working directory
WORKDIR /smartCareApp

# Copy the project in the container
COPY . .

# Install the Python requirements
RUN pip install -r requirements.txt