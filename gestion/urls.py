from django.urls import path
from .views import (
    Dashboard,
    ViewPrueba,
    LocalidadCreate
)

from .forms import FormPrueba

urlpatterns = [
     path('', Dashboard.as_view(), name='index'),

     # Prueba Select2
     path('prueba/', ViewPrueba.as_view(form_class=FormPrueba), name='prueba'),
     # Usada con AJAX en el modalform de creación del cliente
     path('localidad/new/', LocalidadCreate, name='crearLocalidad')
]
