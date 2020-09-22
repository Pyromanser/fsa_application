# This Dockerfile uses multi-stage build to customize DEV and PROD images:
# https://docs.docker.com/develop/develop-images/multistage-build/
FROM python:3.8.3-alpine3.12 as python_base

ARG DJANGO_ENV

ENV LANG C.UTF-8
ENV LANGUAGE C.UTF-8
ENV LC_ALL C.UTF-8

ENV DJANGO_ENV=${DJANGO_ENV} \
    # python:
    PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    # pip:
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    # dockerize:
    DOCKERIZE_VERSION=v0.6.1

RUN apk --no-cache add \
    bash \
    build-base \
    curl \
    gcc \
    gettext \
    git \
    libffi-dev \
    linux-headers \
    openssl \
    musl-dev \
    libxml2-dev \
    libxslt-dev \
    libgcc \
    postgresql-dev \
    jpeg-dev \
    zlib-dev \
    freetype-dev \
    lcms2-dev \
    openjpeg-dev \
    tiff-dev \
    tk-dev \
    tcl-dev \
    tini \
  # Installing `pipenv` package manager:
  && pip install -U --no-cache-dir pip \
  # see issue #4220
  && pip install --no-cache-dir pipenv==2018.11.26

# Copy only requirements, to cache them in docker layer:
WORKDIR /pysetup

COPY ./Pipfile ./Pipfile.lock /pysetup/

# Project initialization:
RUN pipenv install --dev --system


FROM python_base as development_build

# Installing `dockerize` utility:
# https://github.com/jwilder/dockerize
RUN wget "https://github.com/jwilder/dockerize/releases/download/${DOCKERIZE_VERSION}/dockerize-alpine-linux-amd64-${DOCKERIZE_VERSION}.tar.gz" \
  && tar -C /usr/local/bin -xzvf "dockerize-alpine-linux-amd64-${DOCKERIZE_VERSION}.tar.gz" \
  && rm "dockerize-alpine-linux-amd64-${DOCKERIZE_VERSION}.tar.gz"

# This is a special case. We need to run this script as an entry point:
COPY ./docker/django/docker-entrypoint.sh ./docker/django/wait-for-command.sh ./docker/django/runserver.sh ./docker/django/gunicorn.sh /
RUN chmod +x /docker-entrypoint.sh /wait-for-command.sh /runserver.sh /gunicorn.sh

# This dir will become the mountpoint of development code:
WORKDIR /code

ENTRYPOINT ["/sbin/tini", "--", "/docker-entrypoint.sh"]
