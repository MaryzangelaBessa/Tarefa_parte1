from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Participante
from django.urls import reverse_lazy

class ParticipanteListView(ListView):
    model = Participante

class ParticipanteCreateView(CreateView):
    model = Participante
    fields = ['nome', 'cpf', 'email', 'rg', 'status']

class ParticipanteDetailView(DetailView):
    model = Participante

class ParticipanteUpdateView(UpdateView):
    model = Participante
    fields = ['nome', 'cpf', 'email', 'rg', 'status']

class ParticipanteDeleteView(DeleteView):
    model = Participante
    success_url = reverse_lazy('participante:list')