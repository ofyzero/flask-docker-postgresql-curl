# pull official base image
FROM python:3.9.5-slim-buster

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install system dependencies
RUN apt-get update && apt-get install -y netcat

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

# copy project
COPY . /usr/src/app/

# run entrypoint.sh
#ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
#FROM python:3.8-slim
#
#WORKDIR /usr/src/app
#
#COPY ../.. .
#
#RUN pip install -r requirements.txt
#
#EXPOSE 5000
#
#CMD ["flask", "run", "-h", "0.0.0.0"]