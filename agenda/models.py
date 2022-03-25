from django.db import models

# Create your models here.

class Agendamento(models.Model):
    data_horario = models.DateField()
    nome_cliente = models.CharField(max_length=100)
    email_cliente = models.EmailField()
    telefone_cliente = models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.nome_cliente
    pass