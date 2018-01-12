FROM ubuntu:latest
MAINTAINER Kumar Yashojeet "yash@becloudready.com"
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
EXPOSE 5000
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY . /usr/src/app
RUN pip install Flask

