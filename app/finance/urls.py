from django.urls import path
from . import views

urlpatterns = [
    path("Clientes", views.list_clientes, name= 'list'),
    path("Transacciones", views.list_transacciones, name = 'list')
]