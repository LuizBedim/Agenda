from ast import Delete
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.views.generic import DetailView, ListView

from .models import AgendaCompromissos

from django.urls import reverse_lazy

#----- LIST -----
class AgendaCompromissosListView(ListView):
    model = AgendaCompromissos

#----- DETAIL -----
class AgendaCompromissosDetailView(DetailView):
    model = AgendaCompromissos

#----- CREATE -----
class AgendaCompromissosCreate(CreateView):
    model = AgendaCompromissos
    fields = ['compromisso', 'data', 'hora_inicio', 'hora_termino', 'local', 'status', 'observacoes']
    template_name = 'index.html'
    success_url = reverse_lazy('view')

#----- UPDATE -----
class AgendaCompromissosUpdate(UpdateView):
    model = AgendaCompromissos
    fields = ['compromisso', 'data', 'hora_inicio', 'hora_termino', 'local', 'status', 'observacoes']
    template_name = 'edit.html'
    success_url = reverse_lazy('view')

#----- DELETE -----
class AgendaCompromissosDelete(DeleteView):
    model = AgendaCompromissos
    template_name = 'delete.html'
    success_url = reverse_lazy('view')
