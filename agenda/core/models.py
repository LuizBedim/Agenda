from django.db import models
from django.contrib.auth.models import User

class Compromisso(models.Model):
    compromisso = models.CharField(max_length=255)
    data = models.DateField()
    hora_inicio = models.TimeField(verbose_name='Hora do inicio')
    hora_termino = models.TimeField(verbose_name='Hora do termino')
    local = models.CharField(max_length=255)
    observacoes = models.TextField(blank=True, null=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.compromisso