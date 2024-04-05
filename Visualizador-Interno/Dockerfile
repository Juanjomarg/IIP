FROM python:3.9.19-bookworm
COPY . /app/
WORKDIR /app
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 4284
CMD ["gunicorn", "--bind", "0.0.0.0:4284", "--log-level", "debug", "app:server"]
