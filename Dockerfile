# Use the official Python image.
FROM python:3.12-slim

# Set the working directory in the container.
WORKDIR /app

# Copy the requirements.txt file into the container.
COPY requirements.txt .

# Install dependencies.
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project directory into the container.
COPY . .

# Specify the command to run your application.
CMD ["python", "main.py"]
