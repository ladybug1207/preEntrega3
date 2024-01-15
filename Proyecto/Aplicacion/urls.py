from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('Persona/list', views.persona_list, name='persona_list'),
    path('Persona/create', views.persona_create, name='persona_create'),
]
