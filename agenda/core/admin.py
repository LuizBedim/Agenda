from django.contrib import admin
from core.models import Compromisso

class CompromissoAdmin(admin.ModelAdmin):
    list_display = ('compromisso', 'data', 'hora_inicio', 'hora_termino', 'local', 'usuario')
    list_filter = ('compromisso', 'data', 'local', 'usuario',)

admin.site.register(Compromisso, CompromissoAdmin)
