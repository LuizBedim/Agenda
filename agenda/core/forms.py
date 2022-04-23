
import re
from django import forms

STATUS_CHOICES = (
    ('a', 'Agendado'),
    ('r', 'Realizado'),
    ('c', 'Cancelado')
)

class AgendaCompromissos(forms.Form):
    compromisso = forms.CharField(max_length=255)
    data = forms.DateField(required=True)
    hora_inicio = forms.TimeField(required=True)
    hora_termino = forms.TimeField(required=True)
    local = forms.CharField(max_length=255)
    status = forms.ChoiceField(choices=STATUS_CHOICES)
    observacoes = forms.CharField(required=False)

