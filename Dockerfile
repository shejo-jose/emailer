# Use official Python base image
FROM python:3.13

# Set working directory inside container
WORKDIR /app

# Copy uv project files first (for dependency install)
COPY pyproject.toml ./
COPY uv.lock ./

# Install uv package
RUN pip install uv

# Install dependencies using uv
RUN uv sync --no-cache

# Copy the rest of your project files
COPY . .

# Expose the port your FastAPI app runs on
EXPOSE 2266

# Command to run FastAPI with uv
CMD ["uv", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "2266"]
