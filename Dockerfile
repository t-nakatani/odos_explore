FROM python:3.10

RUN apt-get update && \
    apt-get install -y build-essential wget vim

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /work
