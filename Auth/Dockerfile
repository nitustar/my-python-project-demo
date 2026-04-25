# Use official Python image
FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV TZ=Asia/Kolkata 

# Set work directory
WORKDIR /app

# Install ONLY essential build tools
# We keep gcc because some python packages (like pandas/numpy) might need it to compile
# RUN apt-get update && apt-get install -y \
#     gcc \
#     python3-dev \
#     && rm -rf /var/lib/apt/lists/*

# Copy requirements first for better caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Expose port
EXPOSE 8000

# Run migrations then start the Django Dev Server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
# CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]