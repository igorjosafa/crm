# se eu quero popular o banco de dados eu posso criar um formulário de cadastro

from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'cnpj']
