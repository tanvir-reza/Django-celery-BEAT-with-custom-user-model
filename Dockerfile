# write Docker file to build the image

# Use the official image as a parent image

FROM python:3.10

# Set the working directory

ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Copy the current directory contents into the container at /app

COPY . /app

# update pip

RUN pip install --upgrade pip

# Install any needed packages specified in requirements.txt

RUN pip install -r requirements.txt

# Run the server

CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]



EXPOSE 8080
