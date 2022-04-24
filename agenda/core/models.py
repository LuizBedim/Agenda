
from django.db import models


class AgendaCompromissos(models.Model):
    STATUS_CHOICES = (
        ('a', 'Agendado'),
        ('r', 'Realizado'),
        ('c', 'Cancelado'),
    )
    
    compromisso = models.CharField(max_length=255)
    data = models.DateField()
    hora_inicio = models.TimeField()
    hora_termino = models.TimeField()
    local = models.CharField(max_length=255)
    status = models.IntegerField(choices=STATUS_CHOICES)
    observacoes = models.TextField(blank=True, null=True)

    def __str__(self):
        return "{} - {} ".format(self.compromisso, self.status)
    
    class Meta:
        db_table = 'AgendaCompromissos'