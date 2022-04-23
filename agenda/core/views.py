from multiprocessing import context
from django.shortcuts import render
from core.forms import AgendaCompromissos

def index(request):
    form = AgendaCompromissos()
    context = {
        'form': form
    }
    return render(request, 'index.html', context=context)
