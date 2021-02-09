FROM python:3.8.2-buster

WORKDIR /usr/src/app

RUN apt-get update

COPY requirements.txt .

RUN pip install -r ./requirements.txt

WORKDIR /usr/src/app

COPY . .

CMD ["sh", "server_start.sh"]
