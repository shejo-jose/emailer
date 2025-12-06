FROM python:3.13
WORKDIR /app
COPY pyproject.toml ./
COPY uv.lock ./
RUN pip install uv
RUN uv sync --no-cache
COPY . .
EXPOSE 2266
CMD ["uv", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "2266"]