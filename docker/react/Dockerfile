FROM node:14.4.0-alpine3.12 as development_build

ARG ENV

ENV LANG C.UTF-8
ENV LANGUAGE C.UTF-8
ENV LC_ALL C.UTF-8

WORKDIR /app

## add `/app/node_modules/.bin` to $PATH
#ENV PATH /app/node_modules/.bin:$PATH

RUN apk --no-cache add tini

# install app dependencies
COPY ./fsa_frontend/package.json ./fsa_frontend/yarn.lock ./
RUN yarn install

# This is a special case. We need to run this script as an entry point:
COPY ./docker/react/docker-entrypoint.sh ./docker/react/runserver.sh /
RUN chmod +x /docker-entrypoint.sh /runserver.sh

ENTRYPOINT ["/sbin/tini", "--", "/docker-entrypoint.sh"]