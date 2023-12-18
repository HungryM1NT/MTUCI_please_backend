FROM python:3.10-slim

ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE mtuci_please_backend.settings
RUN pip install --upgrade pip

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . /app

# COPY ./entrypoint.sh .

WORKDIR /app/mtuci_please_backend
ENTRYPOINT ["sh", "/app/entrypoint.sh"]