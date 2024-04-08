FROM python:3.9-slim

COPY ./requirements.txt /requirements.txt
RUN pip3 install -r /requirements.txt

WORKDIR /
COPY ./app /


CMD [ "gunicorn", "--workers=5", "--threads=1", "-b 0.0.0.0:8080", "app:server"]