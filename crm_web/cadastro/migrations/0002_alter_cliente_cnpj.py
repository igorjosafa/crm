# Generated by Django 5.0.2 on 2024-03-01 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='cnpj',
            field=models.CharField(max_length=14),
        ),
    ]