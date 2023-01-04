FROM python:3.7-slim-buster as base

COPY ./requirements.txt .
RUN pip install -r requirements.txt
# Now multistage build
FROM python:3.7-slim-buster

WORKDIR /usr/src/notes_api

COPY --from=base /usr/local/lib/python3.7/site-packages/ /usr/local/lib/python3.7/site-packages/
COPY --from=base /usr/local/bin/ /usr/local/bin/
COPY . .
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
HEALTHCHECK CMD curl --fail http://localhost:8000/admin || exit 1
ENTRYPOINT [ "bash","./entrypoint.sh" ]
