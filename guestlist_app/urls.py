from django.urls import path
from django.urls import include
from .views import GuestListView
from .views import DeleteGuest
from .views import CreateGuest
from .views import UpdateAttendance

urlpatterns = [
    path("", GuestListView.as_view(), name="index"),
    path("guest/<int:pk>/delete", DeleteGuest.as_view(), name="del_guest"),
    path("guest/add/", CreateGuest.as_view(), name="add_guest"),
    path("guest/<int:pk>/change", UpdateAttendance.as_view(), name="change_attd"),
    path("__reload__/", include("django_browser_reload.urls")),
]