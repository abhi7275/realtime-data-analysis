# Dockerfile in simulator folder
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the requirements.txt and install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy all files from the simulator folder into the container's /app/ directory
COPY ./simulator /app/

# Start the simulator script
CMD ["python", "data_simulator.py"]
