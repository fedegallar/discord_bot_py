FROM python:3.6-slim-buster
RUN apt -y update
RUN apt -y install ffmpeg
WORKDIR /app
COPY requirements.txt /app/
RUN pip3 install -r requirements.txt
COPY . /app/
RUN python main.py