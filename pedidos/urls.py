from django.urls import path
from .views import (
    PedidoListView,
    PedidoDetailView,
    PedidoCreateView,
    PedidoUpdateView,
    PedidoDeleteView,
)

urlpatterns = [
    path('', PedidoListView.as_view(), name='pedido'),
    path('new/',
         PedidoCreateView.as_view(), name='createPedido'),
    path('<int:pk>/',
         PedidoDetailView.as_view(), name='detailPedido'),
    path('<int:pk>/delete',
         PedidoDeleteView.as_view(), name='deletePedido'),
    path('<int:pk>/update/',
         PedidoUpdateView.as_view(), name='updatePedido'),
]