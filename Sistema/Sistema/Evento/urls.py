from django.urls import path
from .views import (EventoListView, EventoCreateView, EventoDetailView,
                    EventoUpdateView, EventoDeleteView)

from .apps import EventoConfig

app_name = EventoConfig.name
urlpatterns = [
    path('', EventoListView.as_view(), name='list'),
    path('add/', EventoCreateView.as_view(), name='add'),
    path('<int:pk>/detail/', EventoDetailView.as_view(), name='detail'),
    path('<int:pk>/edit/', EventoUpdateView.as_view(), name='edit'),
    path('<int:pk>/delete/', EventoDeleteView.as_view(), name='delete'),
]
