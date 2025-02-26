# Use an official Python runtime as the base image
FROM python:3.10

# Set environment variables to prevent Python from writing .pyc files
ENV PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt .

# Install the required dependencies
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Install psycopg2 manually
RUN pip install psycopg2-binary

# Copy the rest of the application code to the working directory
COPY . .

# Expose the port on which the application will run
EXPOSE 8000

# Command to run FastAPI with Uvicorn
CMD ["uvicorn", "app.main:app", "--host=0.0.0.0", "--port=8000", "--workers", "4"]
