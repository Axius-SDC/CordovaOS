FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    postgresql-client \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Create non-root user with UID/GID 1000 to match typical host user
ARG UID=1000
ARG GID=1000
RUN groupadd -g ${GID} appuser || true && \
    useradd -u ${UID} -g ${GID} -m -s /bin/bash appuser || true

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY --chown=appuser:appuser . .

# Create directories with correct ownership
RUN mkdir -p staticfiles mediafiles && \
    chown -R appuser:appuser staticfiles mediafiles

# Switch to non-root user
USER appuser

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
