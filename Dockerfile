# ==============================================================================
# ShopSphere - Production Dockerfile for Containerized Deployment
# Distributed Commerce Platform: A DevOps-Driven E-Commerce Application
# ==============================================================================

FROM python:3.11-slim

# Prevent Python from writing .pyc files and enable unbuffered logging
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PORT=5000

# Set application working directory
WORKDIR /app

# Install system dependencies if required and upgrade pip
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy application source code
COPY app/ /app/app/
COPY run.py /app/run.py

# Create instance directory for SQLite persistence
RUN mkdir -p /app/instance

# Expose standard container port
EXPOSE 5000

# Container Healthcheck using the native /api/health endpoint
HEALTHCHECK --interval=30s --timeout=5s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:5000/api/health || exit 1

# Launch the ShopSphere Flask Application
CMD ["python", "run.py"]
