FROM python:3
USER root

RUN apt-get update

RUN mkdir -p /root/src
COPY requirements.txt /root/src
WORKDIR /root/src

RUN python -m pip install --upgrade pip
RUN python -m pip install --upgrade setuptools

# requirements.txtに書かれているパッケージをインストールする
RUN python -m pip install -r requirements.txt

COPY ./src /root/src