FROM python:3.9-slim

COPY .requirements.txt /requirements.txt
RUN pip3 install -r /requirements.txt

COPY ./app/ /app/
WORKDIR /app

EXPOSE 4284
CMD gunicorn --bind 4284:8080 --log-level debug app:server