from django.contrib import admin

# Register your models here.
from .models import Empresa, UsuarioResponsavel, UsuarioFuncionario

admin.site.register(Empresa)
admin.site.register(UsuarioResponsavel)
admin.site.register(UsuarioFuncionario)