FROM python:latest

WORKDIR /app

# build / install dependencies

COPY requirements.txt ./


RUN pip install -r requirements.txt

EXPOSE 8080

COPY src/ src/
CMD ["python","src/start_server.py"]