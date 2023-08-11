FROM python:3.11-slim-buster

WORKDIR /app

COPY . /app

RUN pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi
