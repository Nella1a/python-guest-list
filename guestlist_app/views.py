from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic import DeleteView
from .models import GuestList
from django.urls import reverse
from django.urls import reverse_lazy

# Create your views here.

class GuestListView(ListView):
    model = GuestList
    template_name = "guestlist_app/index.html"

class DeleteGuest(DeleteView):
    model = GuestList
    success_url = reverse_lazy("index")
