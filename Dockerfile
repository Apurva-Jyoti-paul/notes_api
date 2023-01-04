# pull official base image
FROM python:3.7-slim-buster

# set work directory
WORKDIR /usr/src/notes_api

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN apt-get update
RUN apt-get install curl -y 
#install psycopg2 dependencis for postgres

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt


# copy project
COPY . .
HEALTHCHECK CMD curl --fail http://localhost:8000/admin || exit 1

ENTRYPOINT [ "bash","./entrypoint.sh" ]
