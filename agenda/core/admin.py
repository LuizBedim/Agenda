from django.contrib import admin

from core.models import AgendaCompromissos

@admin.register(AgendaCompromissos)
class AgendaCompromissosAdmin(admin.ModelAdmin):
    list_display = ('compromisso', 'data', 'hora_inicio', 'hora_termino', 'local')
    list_filter = ('data', 'local')