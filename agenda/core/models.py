
from django.db import models
from django.urls import reverse

class AgendaCompromissos(models.Model):
    Agendado = 1
    Realizado = 2
    Cancelado = 3

    STATUS_CHOICES = (
        (Agendado, 'Agendado'),
        (Realizado, 'Realizado'),
        (Cancelado, 'Cancelado'),
    )
    
    compromisso = models.CharField(max_length=255, unique=True)
    data = models.DateField()
    hora_inicio = models.TimeField()
    hora_termino = models.TimeField()
    local = models.CharField(max_length=255)
    status = models.IntegerField(choices=STATUS_CHOICES)
    observacoes = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.compromisso

    class Meta:
        db_table = 'AgendaCompromissos'