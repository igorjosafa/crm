#depois de criar o app, criei este arquivo para indicar em que endereço ele será selecionado

from django.urls import path

from . import views

urlpatterns = [
    path("", views.mostra_formulario_cadastro, name="mostra_formulario_cadastro"),
]