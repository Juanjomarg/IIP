FROM python:3
COPY ./app/ /app/
WORKDIR /app

RUN apt-get update \
    && apt-get install -y gunicorn \
    && rm -rf /var/lib/apt/lists/*

CMD ["python3", "--version"]

RUN pip3 install -r requirements.txt
EXPOSE 4284
CMD ["gunicorn", "--bind", "0.0.0.0:4284", "--log-level", "debug", "app:server"]