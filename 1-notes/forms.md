# [Trabajando con formularios en Django](https://docs.djangoproject.com/en/2.2/topics/forms/#building-a-form-in-django)

Resumen de los pasos a tener en cuenta al usar forms en Django:

1. Creación
2. Views (Envío y procesamiento de información)
3. Templates

https://docs.djangoproject.com/en/2.2/topics/forms/modelforms/#the-save-method

### is_valid()

A Form instance has an `is_valid()` method, which runs validation routines for all its fields. When this method is called, if all fields contain valid data, it will:

- return True
- place the form’s data in its cleaned_data attribute.
