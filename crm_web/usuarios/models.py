from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User

class Empresa(models.Model):
    nome = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=18)
    endereco = models.CharField(max_length=200)
    responsavel = models.ForeignKey('UsuarioResponsavel', on_delete=models.SET_NULL, null=True, blank=True, related_name='empresa')

    def __str__(self):
        return self.nome
    
class UsuarioResponsavel(AbstractUser):
    usuario = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='usuario_responsavel')
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14, unique=True, verbose_name='CPF')
    
     # Defina related_name exclusivos para evitar conflitos
    groups = models.ManyToManyField(Group, verbose_name=_('groups'), blank=True, related_name='usuarios_grupos')
    user_permissions = models.ManyToManyField(Permission, verbose_name=_('user permissions'), blank=True, related_name='usuarios_permissoes')

    class Meta:
        verbose_name_plural = 'Usuários Responsáveis'

    def __str__(self):
        return f'{self.nome} - {self.cpf}'