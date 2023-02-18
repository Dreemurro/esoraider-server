#!/usr/bin/env bash

set -o errexit
set -o nounset
set -o pipefail

# We are using `gunicorn` for production, see:
# http://docs.gunicorn.org/en/stable/configure.html

# Check that $CURRENT_ENV is set to "production",
# fail otherwise, since it may break things:
echo "CURRENT_ENV is $CURRENT_ENV"
if [ "$CURRENT_ENV" != 'production' ]; then
  echo 'Error: CURRENT_ENV is not set to "production".'
  echo 'Application will not start.'
  exit 1
fi

export CURRENT_ENV

# Start gunicorn:
# Docs: http://docs.gunicorn.org/en/stable/settings.html
/usr/local/bin/gunicorn \
  --config python:docker.blacksheep.gunicorn_config \
  esoraider_server.app:app