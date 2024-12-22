#!/usr/bin/env bash

set -o errexit
set -o nounset
set -o pipefail

# We are using `granian` for production, see:
# hhttps://github.com/emmett-framework/granian/

# Start granian:
granian \
    --host 0.0.0.0 \
    --port 8000 \
    --interface asgi \
    --no-ws \
    esoraider_server.app:app