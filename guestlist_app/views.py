from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic import DeleteView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from .models import GuestList
from .models import Guests
from django.urls import reverse
from django.urls import reverse_lazy

# Create your views here.
class GuestListList(ListView):
    model = GuestList
    template_name = "guestlist_app/index.html"


class CreateGuestList(CreateView):
    model = GuestList
    fields = ["title"]

    def  get_success_url(self):
        return reverse("index")



class GuestView(ListView):
  model = Guests
  template_name ="guestlist_app/guestlist.html"

  def get_queryset(self):
     hello = Guests.objects.filter(list=self.kwargs["list_id"])
     print("###", hello)
     return hello

  def get_context_data(self):
      context = super().get_context_data()
      context["guestlist"] = GuestList.objects.get(id=self.kwargs["list_id"])
      print("*****", context)
      return context


class DeleteGuest(DeleteView):
    model = Guests
    success_url = reverse_lazy("index")



class CreateGuest(CreateView):
    model = Guests
    fields = [
        "list",
        "first_name",
        "last_name",
    ]

    def get_success_url(self):
        return reverse_lazy("index")

class UpdateAttendance(UpdateView):
    model = Guests
    fields = [
        "attending"
    ]

    def get_initial(self):
        initial = super().get_initial()
        initial["guest_id"] = GuestList.objects.get(id=self.kwargs["pk"])
        return initial
