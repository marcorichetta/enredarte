# Crear nueva App y mover modelos

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
