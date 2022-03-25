from django.db import models

# Create your models here.

class Agendamento(models.Model):
    data_horario = models.DateField()
    nome_cliente = models.CharField()
    email_cliente = models.EmailField()
    telefone_cliente = models.CharField()
    pass