# pull official base image
FROM python:3.9-alpine

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update \
    && apk add git gcc python3-dev musl-dev mariadb-dev libffi-dev

# install dependencies
RUN pip install --upgrade pip setuptools wheel
RUN pip install pipenv
COPY Pipfile* ./
RUN pipenv lock --requirements > /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

# copy project
COPY . .

# collect static
RUN python3 manage.py collectstatic --noinput
