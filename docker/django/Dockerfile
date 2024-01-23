# define an alias for the specfic python version used in this file
FROM python:3.12-slim-bullseye as python

# build stage
FROM python as build-stage

# install apt packages
RUN apt-get update && apt-get install --no-install-recommends -y \
  # dependencies for building Python packages
  build-essential

# requirements are installed here to ensure they're cached
COPY requirements.txt .

# create Python dependency and sub-dependency Wheels
RUN pip wheel --wheel-dir /usr/src/app/wheels  \
  -r requirements.txt

# run stage
FROM python as run-stage

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN addgroup --system django \
  && adduser --system --ingroup django django

# copy scripts and +x them
COPY ./docker/django/scripts /scripts
RUN chmod -R +x /scripts
RUN chown -R django:django /scripts

# install required system dependencies
RUN apt-get update && apt-get install --no-install-recommends -y \
  # translations dependencies
  gettext \
  # clean up unused files
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && rm -rf /var/lib/apt/lists/*

# copy python dependency wheels from build-stage
COPY --from=build-stage /usr/src/app/wheels  /wheels/

# use wheels to install python dependencies
RUN --mount=type=cache,target=~/.cache/pip pip install  \
  --no-cache-dir  \
  --no-index  \
  --find-links=/wheels/  \
  /wheels/* \
  && rm -rf /wheels/

# copy application code to WORKDIR
COPY --chown=django:django .. /app

# make django owner of the WORKDIR directory as well
RUN chown django:django /app

USER django
WORKDIR /app

ENTRYPOINT ["/scripts/entrypoint.sh"]