# django-site-project-with-poetry

## Init

### Setup Poetry

```bash
poetry init
```

This command will guide you through creating your pyproject.toml config.

### Add dependencies

```bash
poetry add Django
```

### Create Django project

```bash
poetry run django-admin startproject project .
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