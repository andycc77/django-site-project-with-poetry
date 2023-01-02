# django-site-project-with-poetry

## Init

### Install Poetry

```bash
poetry install
```

This command will guide you through creating your pyproject.toml config.

### Add dependencies

```bash
poetry add Django
```


### Migrations

```bash
poetry run python manage.py migrate
```

### Run Server

```bash
poetry run python manage.py runserver
```

### Create a super user

```bash
poetry run python manage.py createsuperuser
```