# Use Python base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy all project files into the container
COPY . /app

# Set the entry point as Python
ENTRYPOINT ["python"]

# Default command (runs Main.py by default)
CMD ["Main.py", "spec.json", "input.txt", "output.csv"]
