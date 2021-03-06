# Postgres

-   https://docs.djangoproject.com/en/2.2/intro/tutorial02/

-   https://www.digitalocean.com/community/tutorials/how-to-use-postgresql-with-your-django-application-on-ubuntu-14-04

`show timezone` muestra la tz actual de la DB. [Info](https://stackoverflow.com/questions/6663765/postgres-default-timezone)

Django usa UTF por defecto.

### [Eliminar datos de tablas](https://www.postgresql.org/message-id/15aa6b3e0906171358i712e5e1hd44f9dfb3fb386c2@mail.gmail.com)

-   `DELETE` también elimina todos los registros.

-   `TRUNCATE` elimina todos los registros más rápido que `DELETE` (Postgres extension)
-   Con la opción `CASCADE` se eliminan también todos los registros de las tablas
    que tengan Foreign Keys asociadas a la tabla objetivo.

Ejemplo:

```SQL
TRUNCATE TABLE provincia
RESTART IDENTITY /* Reinciar los índices */
CASCADE; /* Aplicar en todas las tablas asociadas con provincia */
```
