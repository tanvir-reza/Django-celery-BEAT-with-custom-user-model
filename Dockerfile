# write Docker file to build the image

# Use the official image as a parent image

FROM python:3.7-slim

# Set the working directory

ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Copy the current directory contents into the container at /app

COPY . /app

# Install any needed packages specified in requirements.txt

RUN pip install -r requirements.txt

# Make port 80 available to the world outside this container

EXPOSE 80
