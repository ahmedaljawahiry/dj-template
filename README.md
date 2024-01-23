# DJ-Template

This repository holds the backend for dj-template, which is primarily
a [Django](https://www.djangoproject.com/) project.

## Development

[Docker](https://docs.docker.com/get-started/) is recommended for local builds and development.

### Build

1. Enable [Docker BuildKit](https://www.docker.com/blog/faster-builds-in-compose-thanks-to-buildkit-support/), by setting the following env vars: 
    ```shell
    DOCKER_BUILDKIT=1
    COMPOSE_DOCKER_CLI_BUILD=1
    ```
2. Optionally - set an `IMAGE_PREFIX` env var, to avoid conflicts with other projects.
3. Create an empty `.env` file.
4. Run `docker-compose build`.

### Run

All necessary env variables are set in `.env.local`. If you'd like to add 
any extra (secret) vars, you can include them in a `.env` file.

Run `docker-compose up -d` to start all services. The following scripts are used: 

- Django: [docker/.../scripts/start-local.sh](./docker/django/scripts/start-local.sh).

- Celery Worker: [docker/.../scripts/celery/start-worker.sh](./docker/django/scripts/celery/start-worker.sh).

- Celery Beat: [docker/.../scripts/celery/start-beat.sh](./docker/django/scripts/celery/start-beat.sh).

Django should be running on port 8000, and the admin can be found at `/admin`.

To log in, [create
a superuser](https://docs.djangoproject.com/en/4.2/intro/tutorial02/#introducing-the-django-admin) 
by running the command `python manage.py createsuperuser` within the `django` container.

**Tip:** create the following aliases:
```shell
alias dj-run='docker-compose run --rm be.django'
alias djm-run='dj-run python manage.py'
alias dj-test='dj-run pytest'
```

#### pre-commit

Before committing work, setup [pre-commit](https://pre-commit.com/) to enable checks for
[Black](https://github.com/psf/black) and [isort](https://pycqa.github.io/isort/) formatting.

## Production

The Django image can be used to run Django, Celery Worker, and Celery Beat containers.
It is assumed that managed services will be used to run Postgres, Redis, Qdrant, etc.

The following scripts can be used for startup commands: 

- Django: [docker/.../scripts/start-production.sh](./docker/django/scripts/start-production.sh).

- Celery Worker: [docker/.../scripts/celery/start-worker.sh](./docker/django/scripts/celery/start-worker.sh).

- Celery Beat: [docker/.../scripts/celery/start-beat.sh](./docker/django/scripts/celery/start-beat.sh).

Django's development server is replaced by:

- [Gunicorn](https://gunicorn.org/) with [Uvicorn](https://www.uvicorn.org/) workers as the application 
server ([ASGI](https://asgi.readthedocs.io/en/latest/)).

- [Whitenoise](https://whitenoise.readthedocs.io/en/latest/) for serving static assets.

### Environment variables

The minimum variables required to run the app are in `.env.local`. At
the time of writing, these are:

```shell
DJANGO_SECRET_KEY=
DJANGO_ADMIN_URL=

REDIS_URL=

POSTGRES_HOST=
POSTGRES_PORT=
POSTGRES_DB=
POSTGRES_USER=
POSTGRES_PASSWORD=
```

Note: this is list is not exhaustive, and extra secrets may be required for
full functionality. Check [settings/](config/settings) for the full app config.