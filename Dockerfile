# Use the official Python image as the base image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt to the working directory
COPY requirements.txt .

# Install dependencies
RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt && echo "Requirements installed successfully."

# Copy the rest of the application code into the container
COPY . .

# Expose the port FastAPI will run on
EXPOSE 8000

# Command to run the FastAPI app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001"]
