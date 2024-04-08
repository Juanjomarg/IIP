FROM debian
COPY ./app/ /app/
WORKDIR /app
RUN apt-get update && apt-get upgrade -y

RUN apt-get install -y gunicorn

RUN apt-get install -y software-properties-common wget xz-utils
RUN wget https://www.python.org/ftp/python/3.11.3/Python-3.11.3.tar.xz
RUN tar -xf Python-3.11.3.tar.xz
RUN cd Python-3.11.3
RUN ./configure --enable-optimizations
RUN make altinstall

RUN pip3 install -r requirements.txt
EXPOSE 4284
CMD ["gunicorn", "--bind", "0.0.0.0:4284", "--log-level", "debug", "app:server"]
