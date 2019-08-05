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

### [Eliminar datos de tablas](https://www.postgresql.org/message-id/15aa6b3e0906171358i712e5e1hd44f9dfb3fb386c2@mail.gmail.com)

- `DELETE` también elimina todos los registros.

- `TRUNCATE` elimina todos los registros más rápido que `DELETE` (Postgres extension)
 - Con la opción `CASCADE` se eliminan también todos los registros de las tablas 
    que tengan Foreign Keys asociadas a la tabla objetivo.

Ejemplo:

```SQL
TRUNCATE TABLE provincia 
RESTART IDENTITY /* Reinciar los índices */
CASCADE; /* Aplicar en todas las tablas asociadas con provincia */
```

## Migrar data

```bash
python manage.py makemigrations

python manage.py migrate

python manage.py createsuperuser
```

# Crear nueva App

1. `python manage.py startapp <nombre>`
2. Añadir en `settings.py`
3. Modificar `urls.py` del proyecto
4. Mover modelos principales
5. Tratar de ir chequeando en el siguiente orden
    1. `views.py`
    2. `urls.py`
    3. Templates
    4. forms y `models.py`
    5. `admin.py`
    6. Circular imports
    7. db_table = "appvieja.nombre" Para mantener la misma tabla.
    8. `makemigrations` y `migrate`
    9. https://stackoverflow.com/questions/30981578/django-1-8-migrations-circulardependencyerror

## Errores
***

### AttributeError: 'ManyToManyField' object has no attribute 'm2m_reverse_field_name' (**Pérdida de datos**)
[Solución](https://stackoverflow.com/a/37701209/6389248)

### ValueError: Related model 'proveedores.Proveedor' cannot be resolved (**Pérdida de datos**)
El modelo Proveedor no fue creado en la app proveedores al momento de correr
esta migración.
1. Borrar archivos de migración (Todos los creados)
2. Comentar el campo ManyToMany en cuestión
3. `makemigrations`
4. `migrate`

### ValueError: (you cannot alter to or from M2M fields, or add or remove through= on M2M fields)
No se pueden modificar ManyToMany fields. [StackOverflow](https://stackoverflow.com/questions/26927705/django-migration-error-you-cannot-alter-to-or-from-m2m-fields-or-add-or-remove)

1. Comentar el campo ManyToMany en el modelo
2. Hacer la migración
3. Quitar el comentario
4. Nuevamente hacer la migración

*Básicamente estamos eliminando y volviendo a crear el campo.
Esto posiblemente conlleve a pérdida de información ya que la 
tabla que relaciona los MaM será eliminada en la primera migración.*


## Imágenes
***
Crear un directorio 'media' donde se guardarán las imágenes subidas.

En el modelo, el arg `upload_to` define el directorio dentro de media
donde se ubicará la imagen:

```python
ImageField(upload_to='productos/', null=True)
```

`settings.py`

```python
###
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), "media)
```

`urls.py`

```python
from django.conf.urls.static import static
###
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

## Extra Views
https://github.com/AndrewIngram/django-extra-views/