## Imágenes

---

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
