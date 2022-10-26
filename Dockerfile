FROM ubuntu:22.04

LABEL maintainer="techiaith"

ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=Europe/London

RUN apt update -q \
 && apt install -y -qq tzdata bash build-essential git curl wget software-properties-common \
    vim ca-certificates libffi-dev libssl-dev libsndfile1 libbz2-dev liblzma-dev locales \
    libboost-all-dev libboost-tools-dev libboost-thread-dev cmake  \
    python3 python3-pip python3-setuptools python3-dev curl zip zlib1g-dev vim \
    ffmpeg sox alsa-utils \
 && python3 -m pip install --upgrade pip

WORKDIR /usr/local/bin
RUN git clone https://github.com/marian-nmt/moses-scripts.git

COPY app/requirements.txt /tmp
RUN python3 -m pip install -r /tmp/requirements.txt


RUN mkdir -p /app && \
    mkdir -p /var/log/app

WORKDIR /app

COPY app /app/

EXPOSE 8008

CMD ["/bin/bash", "-c", "/app/start.sh"]
