## Smart Care Django Project

Welcome to the Smart Care Django Project! This project aims to create a django project for a GP business recruiting 1 full-time and 1-part-time doctors and 1 part-time nurse.

## Table of Contents
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
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

5. Access the application at ````http://localhost:8000````

### other usefull commands:
#### Remove the containers and images
````docker-compose down````\
````docker system prune -a````

#### to run to container 
````docker-compose run SmartCare````

#### to enter to container 
````docker-compose exec SmartCare /bin/bash````\
````ls```` to see the container folders.
#### to get out of the container
````exit````

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

# License
This project is licensed under the GLOBAL LICENSE - see the [LICENSE](https://www.gov.uk/guidance/global-project-licence) file for details.
