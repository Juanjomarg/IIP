FROM debian
COPY ./app/ /app/
WORKDIR /app
RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y gunicorn
RUN apt-get install -y python3.9.19
RUN pip3 install -r requirements.txt
EXPOSE 4284
CMD ["gunicorn", "--bind", "0.0.0.0:4284", "--log-level", "debug", "app:server"]
