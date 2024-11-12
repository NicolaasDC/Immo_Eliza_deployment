# Start with a base image with Python
FROM python:3.13

# Set a working directory
WORKDIR /main

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the port your API listens on (adjust if necessary)
EXPOSE 8000

# Define the command to run your API
CMD ["python", "main.py"]  