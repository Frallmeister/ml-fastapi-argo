# Use an official lightweight Python image
FROM python:3.10-slim

# Set working directory in the container
WORKDIR /app

# Install Python dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the application code and model into the container
COPY . .

# Expose the port FastAPI will run on (80 in this case)
EXPOSE 80

# Start the FastAPI server using uvicorn
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "80"]
