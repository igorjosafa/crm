#depois de criar o app, criei este arquivo para indicar em que endereço ele será selecionado

from django.urls import path

from . import views

urlpatterns = [
    path("empresa", views.cadastrar_empresa, name="cadastrar_empresa"),
    path("responsavel", views.cadastrar_responsavel, name="cadastrar_responsavel"),
    path("funcionario", views.cadastrar_funcionario, name="cadastrar_funcionario"),
    path("erro", views.pagina_de_erro, name="pagina_de_erro")
]