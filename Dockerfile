# Use Python 3.12 slim-buster as the base image
FROM python:3.12-slim-buster

# Set the working directory to /app
WORKDIR /app

# Copy the entire current directory contents to the container
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 8080 available to the world outside this container
EXPOSE 8080

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["python", "app.py"]
