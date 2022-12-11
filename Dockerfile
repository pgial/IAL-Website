# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /src
COPY requirements.txt /src/
RUN pip install -r requirements.txt
COPY . /src/

RUN python manage.py migrate

RUN python manage.py loaddata ial_app/fixtures/*

CMD ['python' 'manage.py' 'runserver' '0.0.0.0:8000']