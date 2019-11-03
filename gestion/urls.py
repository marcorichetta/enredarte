from django.urls import path
from .views import (
    Dashboard,
    ViewPrueba,
    LocalidadCreate
)

from .forms import FormPrueba

urlpatterns = [
     path('', Dashboard.as_view(), name='index'),
     path('prueba/', ViewPrueba.as_view(form_class=FormPrueba), name='prueba'),
     path('localidad/new/', LocalidadCreate, name='crearLocalidad')
]
