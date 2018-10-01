from django.urls import path
from .views import (OrganizadorListView, OrganizadorCreateView, OrganizadorDetailView,
                    OrganizadorUpdateView, OrganizadorDeleteView)
from .apps import OrganizadorConfig

app_name = OrganizadorConfig.name
urlpatterns = [
    path('', OrganizadorListView.as_view(), name='list'),
    path('add/', OrganizadorCreateView.as_view(), name='add'),
    path('<int:pk>/detail/', OrganizadorDetailView.as_view(), name='detail'),
    path('<int:pk>/edit/', OrganizadorUpdateView.as_view(), name='edit'),
    path('<int:pk>/delete/', OrganizadorDeleteView.as_view(), name='delete'),
]