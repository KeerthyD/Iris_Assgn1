# Example Dockerfile for FastAPI + ML model
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy everything to the container
COPY . /app

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose port
EXPOSE 8000

# Command to run the FastAPI server
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]
