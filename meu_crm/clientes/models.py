from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome
