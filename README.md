# [Django](https://docs.djangoproject.com/en/2.2/intro/tutorial01/)

```
django-admin startproject enredarte

python manage.py startapp gestion
```

# Postgres

- https://docs.djangoproject.com/en/2.2/intro/tutorial02/

- https://www.digitalocean.com/community/tutorials/how-to-use-postgresql-with-your-django-application-on-ubuntu-14-04

`show timezone` muestra la tz actual de la DB. [Info](https://stackoverflow.com/questions/6663765/postgres-default-timezone)

Django usa UTF por defecto.

## Migrar data

```
python manage.py makemigrations

python manage.py migrate

python manage.py createsuperuser
```