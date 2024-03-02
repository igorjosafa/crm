# se eu quero popular o banco de dados eu posso criar um formulário de cadastro

from django import forms
from .models import Empresa, UsuarioResponsavel, UsuarioFuncionario

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

class FuncionarioForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        # Obter empresas disponíveis passadas como argumento
        empresas = kwargs.pop('empresas', None)
        super().__init__(*args, **kwargs)
        # Filtrar opções de empresas se empresas estiver definido
        if empresas is not None:
            self.fields['empresa'].queryset = empresas

    class Meta:
        model = UsuarioFuncionario
        fields = ['nome', 'username', 'email', 'password', 'cpf', 'empresa']
        widgets = {
            'password': forms.PasswordInput(),
        }
