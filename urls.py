from django.urls import path
from .views import TicketListView, TicketDetailView
from . import views

urlpatterns = [
    path('', views.home, name='ticketing-home'),
    path('ticket/<int:pk>/', TicketDetailView.as_view(), name='ticket-detail'),
    path('tickets/', TicketListView.as_view(), name='ticketing-tickets'),
]