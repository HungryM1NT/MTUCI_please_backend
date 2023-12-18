#!/bin/sh

python manage.py makemigrations
python manage.py migrate --no-input
# python manage.py collectstatic --no-input
python manage.py loaddata persons.json
# python mtuci_please_backend/manage.py runserver 0.0.0.0:8000
gunicorn mtuci_please_backend.wsgi:application --bind 0.0.0.0:8000
