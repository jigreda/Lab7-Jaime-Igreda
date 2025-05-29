from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_destinos, name='listar'),
    path('añadir/', views.añadir_destino, name='añadir'),
    path('modificar/<int:id>/', views.modificar_destino, name='modificar'),
    path('eliminar/<int:id>/', views.eliminar_destino, name='eliminar'),
]
