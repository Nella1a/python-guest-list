from django.urls import path
from .views import GuestListView
from .views import DeleteGuest

urlpatterns = [
    path("", GuestListView.as_view(), name="index"),
    path("guest/<int:pk>/", DeleteGuest.as_view(), name="del_guest")
]