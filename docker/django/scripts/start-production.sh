#!/bin/bash

set -o errexit
set -o pipefail
set -o nounset


python /app/manage.py collectstatic --noinput
python /app/manage.py migrate
/usr/local/bin/gunicorn -c /app/docker/django/gunicorn.conf.py config.asgi:application
