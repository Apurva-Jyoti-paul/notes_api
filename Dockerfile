# pull official base image
FROM python:3.7-slim-buster

# set work directory
ENV HOME=/home/app
ENV APP_HOME=/home/app/notes_api
ENV PYTHONPATH=${APP_HOME}:/usr/local/lib/python3.8/site-packages
RUN mkdir -p ${APP_HOME}
WORKDIR ${APP_HOME}

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update \
    && apt-get install gcc python3-dev musl-dev -y \
    && apt-get install supervisor nginx -y

# Supervisord folders
RUN mkdir -p /var/log/supervisor/; \
    touch /tmp/supervisor.sock

# nginx files
RUN mkdir -p /run/nginx/; \
    touch /run/nginx/nginx.pid

# Install requirements
COPY requirements.txt ./requirements.txt

RUN pip install --upgrade pip \
    && pip install -r requirements.txt \
    && pip install gunicorn

RUN mkdir -p /var/log/containerlogs



# Copy necessary configurations files
RUN rm /etc/nginx/sites-enabled/default
COPY docker/nginx.conf /etc/nginx/sites-enabled/default
COPY docker/runserver.sh ${APP_HOME}/gunicorn_start.sh
COPY docker/serverScript.conf ${APP_HOME}/supervisord.conf

# Copy project
COPY . ${APP_HOME}

ENTRYPOINT [ "supervisord", "-n", "-c", "/home/app/notes_api/supervisord.conf" ]
