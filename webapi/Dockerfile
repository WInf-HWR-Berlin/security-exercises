# Variante 1: nur api
FROM python:latest

WORKDIR /app

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY src/ src/
ENTRYPOINT [ "python", "/app/src/start_server.py" ]

