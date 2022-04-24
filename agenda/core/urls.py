from django.urls import path

from core.views import AgendaCompromissosCreate, AgendaCompromissosUpdate
from core.views import AgendaCompromissosListView, AgendaCompromissosDetailView

app_name = 'core'

urlpatterns = [
    path('home/', AgendaCompromissosCreate.as_view(), name='home'),
    path('view/', AgendaCompromissosListView.as_view(), name='view'),
    path('edit/<int:pk>/', AgendaCompromissosUpdate.as_view(), name='edit'),
]