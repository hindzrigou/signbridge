FROM python:3.12-slim

WORKDIR /app

# Install system dependencies required for mysqlclient and video encoding
RUN apt-get update && apt-get install -y \
    default-libmysqlclient-dev \
    build-essential \
    pkg-config \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

RUN pip install pipenv

COPY Pipfile Pipfile.lock ./
RUN pipenv install --system --skip-lock

COPY . .

EXPOSE 8000

CMD ["sh", "-c", "python manage.py runserver 0.0.0.0:8000"]
