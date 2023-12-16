# syntax=docker/dockerfile:1.4
FROM python:3.12-bookworm

WORKDIR /app

COPY requirements.txt /app
RUN pip3 install -r requirements.txt

COPY . /app
ENTRYPOINT ["flask", "--app",  "ivr_phone_tree_python",  "run",  "-h", "0.0.0.0"]
