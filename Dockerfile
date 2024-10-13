FROM python:3

RUN apt-get update && apt-get install -y \
    python3-dev \
    build-essential \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY ./requirements.txt /requirements.txt

RUN pip install --upgrade pip && \
    pip install -r /requirements.txt --no-cache-dir --default-timeout=100

COPY . .

