from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('Persona/list', views.persona_list, name='persona_list'),
    path('Persona/create', views.persona_create, name='persona_create'),
    path('Cliente/list', views.cliente_list, name='cliente_list'),
    path('Cliente/create', views.cliente_create, name='cliente_create'),
    path('Producto/list', views.producto_list, name='producto_list'),
    path('Producto/create', views.producto_create, name='producto_create'),
    path('Vendedor/list', views.vendedor_list, name='vendedor_list'),
    path('Vendedor/create', views.vendedor_create, name='vendedor_create'),
]
