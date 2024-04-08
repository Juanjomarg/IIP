FROM debian
COPY ./app/ /app/
WORKDIR /app
RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y software-properties-common wget xz-utils build-essential zlib1g-dev gunicorn \
    && rm -rf /var/lib/apt/lists/*

RUN wget https://www.python.org/ftp/python/3.11.3/Python-3.11.3.tar.xz \
    && tar -xf Python-3.11.3.tar.xz \
    && cd Python-3.11.3 \
    && ./configure --enable-optimizations \
    && make -j$(nproc) \
    && make altinstall

CMD ["python3.11", "--version"]
RUN pip3 install -r requirements.txt

EXPOSE 4284

CMD ["gunicorn", "--bind", "0.0.0.0:4284", "--log-level", "debug", "app:server"]
