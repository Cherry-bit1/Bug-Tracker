from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Ticket
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    context = {
        'tickets': Ticket.objects.all(),
        'title': 'Dashboard'
    }
    return render(request, 'ticketing/home.html', context)

class TicketListView(ListView):
    model = Ticket
    template_name = 'ticketing/tickets.html'
    context_object_name = 'tickets'
    ordering = ['-date_submitted']

class TicketDetailView(DetailView):
    model = Ticket

@login_required
def tickets(request):
    context = {
        'tickets': Ticket.objects.all(),
        'title': 'Issues'
    }
    return render(request, 'ticketing/tickets.html', context)
