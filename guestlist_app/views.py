from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic import DeleteView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from .models import GuestList
from django.urls import reverse
from django.urls import reverse_lazy

# Create your views here.

class GuestListView(ListView):
    model = GuestList
    template_name = "guestlist_app/guestlist.html"

class DeleteGuest(DeleteView):
    model = GuestList
    success_url = reverse_lazy("index")



class CreateGuest(CreateView):
    model = GuestList
    fields = [
        "first_name",
        "last_name"
    ]

    def get_success_url(self):
        return reverse_lazy("index")

class UpdateAttendance(UpdateView):
    model = GuestList
    fields = [
        "attending"
    ]

    def get_initial(self):
        initial = super().get_initial()
        initial["guest_id"] = GuestList.objects.get(id=self.kwargs["pk"])
        return initial
