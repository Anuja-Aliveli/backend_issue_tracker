# Use official Python image
FROM python:3.11

# Set working directory inside the container
WORKDIR /app

# Copy requirements.txt to install dependencies
COPY requirements.txt ./

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application files
COPY . .

# Expose the port Django will run on
EXPOSE 8000

# Run database migrations and start the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
