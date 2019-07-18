from django.urls import path
from .views import (
    ClienteListView,
    ClienteDetailView,
    ClienteCreateView,
    ClienteUpdateView,
    ClienteDeleteView,
)
from . import views

urlpatterns = [
     path('', ClienteListView.as_view(), name='cliente'),
     path('new/',
          ClienteCreateView.as_view(), name='createCliente'),
     path('<int:pk>/',
          ClienteDetailView.as_view(), name='detailCliente'),
     path('<int:pk>/delete',
          ClienteDeleteView.as_view(), name='deleteCliente'),
     path('<int:pk>/update/',
          ClienteUpdateView.as_view(), name='updateCliente'),
]
