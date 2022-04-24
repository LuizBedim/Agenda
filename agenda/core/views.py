from re import A
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import AgendaCompromissos

from django.urls import reverse_lazy

#----- CREATE -----
class AgendaCompromissosCreate(CreateView):
    model = AgendaCompromissos
    fields = ['compromisso', 'data', 'hora_inicio', 'hora_termino', 'local', 'status', 'observacoes']
    template_name = 'index.html'
    seccess_url = reverse_lazy('home')

#----- UPDATE -----
class AgendaCompromissosUpdate(UpdateView):
    pass