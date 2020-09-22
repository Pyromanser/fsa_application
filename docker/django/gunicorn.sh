#!/usr/bin/env sh

set -o errexit
set -o nounset

# We are using `gunicorn` for production, see:
# http://docs.gunicorn.org/en/stable/configure.html

if [ -z "$DJANGO_ENV" ]; then
  echo "ERROR: DJANGO_ENV is Empty"
  echo 'Application will not start.'
  exit 1
fi

echo "ENV is $DJANGO_ENV"
if [ "$DJANGO_ENV" = 'dev' ]; then
  echo "Run manage.py migrate"
  python /code/manage.py migrate --noinput
#  echo "Flushing database"
#  python /code/manage.py flush --noinput
#  echo "Importing test data"
#  python /code/manage.py loaddata test_data.json
  echo "Run manage.py collectstatic"
  python /code/manage.py collectstatic --noinput
  echo "Run gunicorn"
  exec gunicorn fsa_backend.wsgi -w 4 -b 0.0.0.0:8000 --chdir=/code --log-file=- --worker-tmp-dir /dev/shm --log-level debug
else
  echo "ERROR: DJANGO_ENV isn't valid"
  echo 'Application will not start.'
  exit 1
fi