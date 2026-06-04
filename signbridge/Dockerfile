FROM python:3.12-slim

WORKDIR /app

# Install system dependencies required for mysqlclient and video encoding
RUN apt-get update && apt-get install -y \
    default-libmysqlclient-dev \
    build-essential \
    pkg-config \
    ffmpeg \
    curl \
    && rm -rf /var/lib/apt/lists/*

RUN pip install pipenv

COPY Pipfile Pipfile.lock ./
RUN pipenv install --system --skip-lock

COPY . .

RUN useradd -m appuser && chown -R appuser:appuser /app
USER appuser

EXPOSE 8000

HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:8000/ || exit 1

CMD ["sh", "-c", "python manage.py runserver 0.0.0.0:8000"]
