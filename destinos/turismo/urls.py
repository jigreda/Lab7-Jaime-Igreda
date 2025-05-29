from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_destinos, name='listar'),
    path('añadir/', views.añadir_destino, name='añadir'),
]
