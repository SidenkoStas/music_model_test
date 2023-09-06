FROM python:alpine3.17

LABEL authors="Sidenko"

WORKDIR /app

ADD requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ADD . .

RUN python manage.py makemigrations
RUN python manage.py migrate
