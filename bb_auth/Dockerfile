FROM python:3.10

WORKDIR /app
RUN apt-get update && apt-get install -y curl && apt-get clean
COPY requirements.txt /app/requirements.txt

RUN pip install -r /app/requirements.txt
RUN pip install gunicorn

COPY . /app/

COPY entrypoint.sh /entrypoint.sh
ENTRYPOINT ["bash", "-e", "/entrypoint.sh"]
