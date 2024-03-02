from django.db import models

# Create your models here.
class Cliente(models.Model):
    cnpj = models.CharField(max_length=18)
    nome = models.CharField(max_length=100)

    #mudando a representação do nome
    def __str__(self):
        return f'{self.cnpj} - {self.nome}'