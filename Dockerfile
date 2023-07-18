# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /src
COPY requirements.txt /src/
RUN pip install -r requirements.txt
COPY . /src/

CMD python manage.py migrate && python manage.py loaddata ial_app/fixtures/* && gunicorn ialwebsite.wsgi:application --bind 0.0.0.0:$PORT
