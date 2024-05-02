# Dockerfile :
# ----------
# Official Python image as the base image
FROM python:3.9

# Sent output to the terminal
ENV PYTHONUNBUFFERED = 1

# Set the working directory in docker 
WORKDIR /smartCareApp


# Install the reiquirements
COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . .

# Expose Port
EXPOSE 8000

ENTRYPOINT ["./smartcare-entrypoint.sh"]
