## Smart Care Django Project

Welcome to the Smart Care Django Project! This project aims to...

## Table of Contents
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Docker Setup](#Docker-Setup)
- [MySQL Configuration](#MySQL-Configuration)
  
## Getting Started

### Prerequisites

Before you begin, ensure you have met the following requirements:

- [Docker](https://www.docker.com/)
- [vscode](https://code.visualstudio.com/Download)
- pienv: pip install pipenv
  
### Installation

1. Clone the repository:\
   ````git clone https://github.com/your-username/Smart_Care_Django_Project.git````
   
2. Navigate to the project directory:\
````cd Smart_Care_Django_Project````

3. Build and run the Docker containers:\
````docker-compose up --build````
This will set up the Django application and MySQL database.

4. Access the application at ````http://localhost:8000````

## Docker Setup
This project utilizes Docker for containerization. The Dockerfile is included for building the Django application, and Docker Compose is used to manage multi-container Docker applications.

## MySQL Configuration
The project is configured to use MySQL as the database. Update the DATABASES section in the settings.py file:

# settings.py
````
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'smartcare',
        'USER': 'root',
        'PASSWORD': 'smartcare',
        'HOST': 'db',
        'PORT': '3306',
    }
}
````
