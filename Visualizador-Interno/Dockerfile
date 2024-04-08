FROM python:3.9-slim-buster
RUN apt-get update

RUN mkdir /app
WORKDIR /app

COPY ./app/requirements.txt ./requirements.txt
RUN pip3 install -r ./requirements.txt

COPY ./app ./


CMD [ "gunicorn", "--workers=5", "--threads=1", "-b 0.0.0.0:8080", "app:server"]