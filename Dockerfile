FROM python:3.8-slim-buster

WORKDIR /app

COPY src/ .

RUN pip install -r requirements.txt

ENTRYPOINT [ "python", "/app/uuid-hunter.py" ]

RUN ["ls"]
