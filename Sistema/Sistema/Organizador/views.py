from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Organizador
from django.urls import reverse_lazy

class OrganizadorListView(ListView):
    model = Organizador

class OrganizadorCreateView(CreateView):
    model = Organizador
    fields = ['nome', 'cpf', 'email']

class OrganizadorDetailView(DetailView):
    model = Organizador

class OrganizadorUpdateView(UpdateView):
    model = Organizador
    fields = ['nome', 'cpf', 'email']

class OrganizadorDeleteView(DeleteView):
    model = Organizador
    success_url = reverse_lazy('organizador:list')