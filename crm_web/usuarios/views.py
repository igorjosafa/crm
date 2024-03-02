from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import EmpresaForm, ResponsavelForm, FuncionarioForm
from django.contrib.auth.models import User, Group
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Empresa, UsuarioResponsavel, UsuarioFuncionario

#cria o grupo de usuários da empresa
@receiver(post_save, sender=Empresa)
def criar_grupo_empresa(sender, instance, created, **kwargs):
    group_name = f"{instance.nome} Group"  # Nome do grupo baseado no nome da empresa
    group, created = Group.objects.get_or_create(name=group_name)
    if created:
        # Adicionar permissões ao grupo, se necessário
        pass  # Aqui você pode adicionar permissões ao grupo, se necessário

    #adicionando o responsável da empresa ao grupo
    if instance.responsavel:
            instance.responsavel.usuario.groups.add(group)

#criar o grupo de responsáveis
@receiver(post_save, sender=UsuarioResponsavel)
def criar_grupo_responsaveis(sender, instance, created, **kwargs):
    group_name = "Responsaveis Group"
    group, created = Group.objects.get_or_create(name=group_name)
    if instance.usuario:
        instance.usuario.groups.add(group)

#adicionar o funcionário ao grupo da empresa
@receiver(post_save, sender=UsuarioFuncionario)
def adicionar_grupo_funcionarios(sender, instance, created, **kwargs):
    group_name = f"{instance.empresa} Group"
    group, created = Group.objects.get_or_create(name=group_name)
    if instance.usuario:
        instance.usuario.groups.add(group)

@login_required
def cadastrar_empresa(request):
    if not request.user.is_superuser:
        return redirect('pagina_de_erro')  # Redirecionar para uma página de erro

    if request.method == 'POST':
        form = EmpresaForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'pagina_sucesso.html', {'nome': form.cleaned_data['nome']})
    else:
        form = EmpresaForm()

    return render(request, 'cadastrar_empresa.html', {'form': form})

def pagina_de_erro(request):
    return render(request, 'pagina_erro.html')

@login_required
def cadastrar_responsavel(request):
    if not request.user.is_superuser:
        return redirect('pagina_de_erro')  # Redirecionar para uma página de erro

    if request.method == 'POST':
        form = ResponsavelForm(request.POST)
        if form.is_valid():
            
            #criando o usuário
            usuario = User.objects.create_user(username = form.cleaned_data['username'], email = form.cleaned_data['email'], password = form.cleaned_data['password'])
            usuario.save()

            #criando uma entrada de responsável no banco
            objeto = form.save(commit=False)
            setattr(objeto, 'usuario', usuario)
            setattr(objeto, 'nome', form.cleaned_data['nome'])
            setattr(objeto, 'email', '')
            setattr(objeto, 'password', '')
            objeto.save()

            return render(request, 'pagina_sucesso_usuario.html')
    else:
        form = ResponsavelForm()

    return render(request, 'cadastrar_responsavel.html', {'form': form})

@login_required
def cadastrar_funcionario(request):
    if not request.user.groups.filter(name=Group.objects.get(name='Responsaveis Group')).exists():
        return redirect('pagina_de_erro')
    
    if request.method == 'POST':
        form = FuncionarioForm(request.POST)
        if form.is_valid():
            
            #criando o usuário
            usuario = User.objects.create_user(username = form.cleaned_data['username'], email = form.cleaned_data['email'], password = form.cleaned_data['password'])
            usuario.save()

            #criando uma entrada de funcionário no banco
            objeto = form.save(commit=False)
            setattr(objeto, 'usuario', usuario)
            setattr(objeto, 'nome', form.cleaned_data['nome'])
            setattr(objeto, 'empresa', form.cleaned_data['empresa'])
            setattr(objeto, 'email', '')
            setattr(objeto, 'password', '')
            objeto.save()

            return render(request, 'pagina_sucesso_usuario.html')
    else:
        empresas_do_responsavel = Empresa.objects.filter(responsavel=request.user.usuario_responsavel)
        form = FuncionarioForm(empresas=empresas_do_responsavel)

    return render(request, 'cadastrar_funcionario.html', {'form': form})