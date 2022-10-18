from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic import DeleteView
from django.views.generic import CreateView
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

    def get_context_data(self):
        context = super().get_context_data()
        context["delete_all"] = self.kwargs["del_all"]
        return context

class CreateGuest(CreateView):
    model = GuestList
    fields = [
        "first_name",
        "last_name"
    ]

    def get_success_url(self):
        return reverse_lazy("index")

