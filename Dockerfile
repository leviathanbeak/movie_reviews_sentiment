FROM python:3.7.5-slim
RUN apt-get update -y
RUN apt-get install -y python3-pip python3-dev build-essential
COPY . /web
WORKDIR /web
RUN pip3 install -r web/requirements.txt
ENTRYPOINT ["python3"]
CMD ["web/app.py"]

