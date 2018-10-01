from django.urls import path
from .views import (ParticipanteListView, ParticipanteCreateView, ParticipanteDetailView,
                    ParticipanteUpdateView, ParticipanteDeleteView)
from .apps import ParticipanteConfig

app_name = ParticipanteConfig.name
urlpatterns = [
    path('', ParticipanteListView.as_view(), name='list'),
    path('add/', ParticipanteCreateView.as_view(), name='add'),
    path('<int:pk>/detail/', ParticipanteDetailView.as_view(), name='detail'),
    path('<int:pk>/edit/', ParticipanteUpdateView.as_view(), name='edit'),
    path('<int:pk>/delete/', ParticipanteDeleteView.as_view(), name='delete'),
]