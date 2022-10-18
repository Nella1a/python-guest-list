from django.shortcuts import render
from django.views.generic import ListView
from .models import GuestList
# Create your views here.

class GuestListView(ListView):
    model = GuestList
    template_name = "guestlist_app/index.html"