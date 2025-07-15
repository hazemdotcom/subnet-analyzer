# Use slim Python image
FROM python:3.10-slim

# Set working directory inside the container
WORKDIR /app

# Copy all project files into the container
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Label to detect container run environment (optional for logs)
ENV DOCKER_ENV=true

# Run analysis and visualization
CMD python subnet_analyzer.py && python visualize.py
