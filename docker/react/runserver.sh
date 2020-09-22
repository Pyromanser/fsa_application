#!/usr/bin/env sh

set -o errexit
set -o nounset

if [ -z "$ENV" ]; then
  echo "ERROR: ENV is Empty"
  echo 'Application will not start.'
  exit 1
fi

echo "ENV is $ENV"
if [ "$ENV" = 'dev' ]; then
  echo "Run server"
  yarn start
else
  echo "ERROR: ENV isn't valid"
  echo 'Application will not start.'
  exit 1
fi
