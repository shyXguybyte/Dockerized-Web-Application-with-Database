# Final Project: Dockerized Web Application with Database

## Objective
The goal of this project is to design and implement a web application using Docker, featuring a web server and a database, with the capability to display team data on the website. This project will provide hands-on experience in containerization, communication between containers using Docker Compose, and web development.

## Project Description


### 1. Web Application
- **Description**: Create a simple website to display team data.
- **Pages**:
  - Homepage
  - Team data display page
  - Additional pages as desired
- **Technologies**: HTML, CSS, JavaScript
- **Requirements**:
  - User-friendly and visually appealing interface

### 2. Docker Containers
- **Web Server Container**:
  - Containerize the web application using Docker.
  - Create a `Dockerfile` to define the specifications and dependencies of the web server container.
  - Ensure that the web server container runs the website successfully.

### 3. Database
- **Description**: Design and implement a database to store student data.
- **Schema**:
  - Fields: `name`, `id`, `age`, `CGPA`
- **Database Technology**: MySQL, PostgreSQL, or SQLite
- **Tasks**:
  - Create the necessary tables
  - Define appropriate data types for each field

### 4. Docker Compose
- **Description**: Use Docker Compose to orchestrate the communication between the web server container and the database container.
- **Tasks**:
  - Create a `docker-compose.yml` file with specifications for both containers
  - Configure environment variables, ports, and volumes

### 5. Team Data
- **Requirements**: Display team member data including `name`, `id`, `age`, and `CGPA` on the website. Ensure that this data is stored in the database.


## Getting Started
1. Clone this repository.
2. Build and run the Docker containers using Docker Compose:
   ```bash
   docker-compose up --build
