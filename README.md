# RoboSim
This is Team 1's Assignment 6 for ECE 4574 at Virginia Tech

### What is this repository for? ###

* This project is to provide a Database and API for storage and retrieval of information needed in Robot Simulation.
* Version 1.0

## Prerequisites to Run ##
* Docker is installed
* Your device is connected to the internet (to clone the repository and download required libraries)

## How to Generate the Docker Image ##
1. Navigate to the Dockerfile in your terminal (Powershell on Windows, Terminal on Mac/Linux), located at the root folder of this repository.
2. Run the command `docker build -t [name_of_image] .`, where `[name_of_image]` is a name of your choice

## How to Run the Docker Container ##
Run the command `docker run -p 50:50 -d [name_of_image]`. where `[name_of_image]` is the image name chosen previously.

## How to Stop the Docker Container ##
Run the command `docker stop [id]`, where `[id]` is the generated id number of your container. If you do not know what your container id is, use the command `docker ps` to view all running containers.

### Author ###

* David Gwizdala