# se eu quero popular o banco de dados eu posso criar um formulário de cadastro

from django import forms
from .models import Empresa, UsuarioResponsavel

class EmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = ['nome', 'cnpj', 'endereco', 'responsavel']

class ResponsavelForm(forms.ModelForm):
    class Meta:
        model = UsuarioResponsavel
        fields = ['nome', 'username', 'email', 'password', 'cpf']
        widgets = {
            'password': forms.PasswordInput(),
        }