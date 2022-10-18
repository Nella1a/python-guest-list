from django.urls import path
from .views import GuestListView
from .views import DeleteGuest
from .views import CreateGuest

urlpatterns = [
    path("", GuestListView.as_view(), name="index"),
    path("guest/<int:pk>/delete", DeleteGuest.as_view(), name="del_guest"),
    path("guest/add/", CreateGuest.as_view(), name="add_guest"),
]