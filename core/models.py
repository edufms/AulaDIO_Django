from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Evento(models.Model):
    titulo = models.CharField(max_length=100, verbose_name="Titulo do Evento")
    descricao = models.TextField(
        blank=True, null=True, verbose_name="Descrição do Evento")
    data_evento = models.DateTimeField(verbose_name='Data do Evento')
    data_criacao = models.DateTimeField(auto_now=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'eventos'

    def __str__(self):
        return self.titulo
