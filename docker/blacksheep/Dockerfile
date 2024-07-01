# syntax = docker/dockerfile:1
# This Dockerfile uses multi-stage build to customize DEV and PROD images:
# https://docs.docker.com/develop/develop-images/multistage-build/

FROM python:3.11.9-slim-bookworm AS development_build

LABEL org.opencontainers.image.source=https://github.com/Dreemurro/esoraider-server

# `CURRENT_ENV` arg is used to make prod / dev builds:
ARG CURRENT_ENV \
    # Needed for fixing permissions of files created by Docker:
    UID=1000 \
    GID=1000

ENV CURRENT_ENV=${CURRENT_ENV} \
    # python:
    PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    PYTHONDONTWRITEBYTECODE=1 \
    # pip:
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_DEFAULT_TIMEOUT=100 \
    PIP_ROOT_USER_ACTION=ignore \
    # poetry:
    POETRY_VERSION=1.8.3 \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_CACHE_DIR='/var/cache/pypoetry' \
    POETRY_HOME='/usr/local'

SHELL ["/bin/bash", "-eo", "pipefail", "-c"]

# System deps (we don't use exact versions because it is hard to update them,
# pin when needed):
# hadolint ignore=DL3008
RUN apt-get update && apt-get upgrade -y \
    && apt-get install --no-install-recommends -y \
    curl \
    # Installing `poetry` package manager:
    # https://github.com/python-poetry/poetry
    && curl -sSL 'https://install.python-poetry.org' | python - \
    && poetry --version \
    # Cleaning cache:
    && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
    && apt-get clean -y && rm -rf /var/lib/apt/lists/*

WORKDIR /code

RUN groupadd -g "${GID}" -r web \
    && useradd -d '/code' -g web -l -r -u "${UID}" web \
    && chown web:web -R '/code'

# Copy only requirements, to cache them in docker layer
COPY --chown=web:web ./poetry.lock ./pyproject.toml /code/

# Project initialization:
# hadolint ignore=SC2046
RUN --mount=type=cache,target="$POETRY_CACHE_DIR" \
    echo "$CURRENT_ENV" \
    && poetry version \
    # Install deps:
    && poetry run pip install -U pip \
    && poetry install \
    $(if [ "$CURRENT_ENV" = 'production' ]; then echo '--only main'; fi) \
    --no-interaction --no-ansi --sync

# Running as non-root user:
USER web

# The following stage is only for production
FROM development_build AS production_build
COPY --chown=web:web . /code