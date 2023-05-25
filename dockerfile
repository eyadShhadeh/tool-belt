# Use the official Python image as the base image
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.11 as base

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code to the container
# COPY . .

# Expose the port on which the application will run
EXPOSE 80

# Start the app using the Uvicorn server with Gunicorn workers
# CMD [ "gunicorn", "-c", "gunicorn_conf.py", "-b", "0.0.0.0:80", "src.main:app"]
