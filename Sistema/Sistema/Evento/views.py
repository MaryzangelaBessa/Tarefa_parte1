from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Evento
from django.urls import reverse_lazy

class EventoListView(ListView):
    model = Evento

class EventoCreateView(CreateView):
    model = Evento
    fields = ['titulo','data', 'hora', 'tipo', 'local']

class EventoDetailView(DetailView):
    model = Evento

class EventoUpdateView(UpdateView):
    model = Evento
    fields = ['titulo','data', 'hora', 'tipo', 'local']
    
class EventoDeleteView(DeleteView):
    model = Evento
    success_url = reverse_lazy('evento:list')