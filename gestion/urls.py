from django.urls import path
from .views import (
    Dashboard,
    ViewPrueba
)

from .forms import FormPrueba

urlpatterns = [
     path('', Dashboard.as_view(), name='index'),
     path('prueba/', ViewPrueba.as_view(form_class=FormPrueba), name='prueba'),
]
