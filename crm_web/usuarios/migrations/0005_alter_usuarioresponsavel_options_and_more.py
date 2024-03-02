# Generated by Django 5.0.2 on 2024-03-02 13:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0004_usuarioresponsavel_empresa_funcionario'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usuarioresponsavel',
            options={'verbose_name_plural': 'Usuários Responsáveis'},
        ),
        migrations.RenameField(
            model_name='empresa',
            old_name='funcionario',
            new_name='responsavel',
        ),
        migrations.RemoveField(
            model_name='usuarioresponsavel',
            name='empresas',
        ),
    ]
