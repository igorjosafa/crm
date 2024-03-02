from django.shortcuts import render, redirect

# Create your views here.

#aqui eu coloco a view do app. ou seja, o que aparecerá no navegador.
from django.http import HttpResponse
from .forms import ClienteForm
from telegram_bot import enviar_mensagem_telegram


def mostra_formulario_cadastro(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            enviar_mensagem_telegram(f"O cliente {form.cleaned_data['cnpj']} - {form.cleaned_data['nome']} foi cadastrado com sucesso.")
            return render(request, 'pagina_sucesso.html', {'nome': form.cleaned_data['nome']})
    else:
        form = ClienteForm()
    return render(request, 'cadastro_cliente.html', {'form': form})
