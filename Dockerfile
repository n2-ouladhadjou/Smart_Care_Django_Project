# Dockerfile :
# ----------
# Python Image
FROM python:3.10-slim

# Install the files/compilers/lib to run mysql
RUN apt-get update && apt-get install -y \
    gcc \
    musl-dev \
    libmariadb-dev \
    pkg-config

# Create project Folder (Volume)
WORKDIR /smartCareApp

# Install the reiquirements
COPY  requirements.txt ./
RUN pip install -r requirements.txt

COPY . .

# Expose Port
EXPOSE 8000
