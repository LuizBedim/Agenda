from django.contrib import admin
from django.urls import path, include 
from core.views import AgendaCompromissosCreate, AgendaCompromissosUpdate, AgendaCompromissosDelete
from core.views import AgendaCompromissosListView, AgendaCompromissosDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', AgendaCompromissosCreate.as_view(), name='home'),
    path('view/', AgendaCompromissosListView.as_view(), name='view'),
    path('delete/<int:pk>/', AgendaCompromissosDelete.as_view(), name='delete'),
    path('edit/<int:pk>/', AgendaCompromissosUpdate.as_view(), name='edit'),


