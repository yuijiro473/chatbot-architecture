FROM python:3.9-slim-buster

# Add system dependencies for mysqlclient
RUN apt-get update \
    && apt-get install -y default-libmysqlclient-dev gcc

WORKDIR /app

COPY ./app/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ./app .

CMD ["python", "sample/app.py"]