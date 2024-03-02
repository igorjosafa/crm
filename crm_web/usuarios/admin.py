from django.contrib import admin

# Register your models here.
from .models import Empresa, UsuarioResponsavel

admin.site.register(Empresa)
admin.site.register(UsuarioResponsavel)