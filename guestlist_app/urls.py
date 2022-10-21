from django.urls import path
from django.urls import include
from .views import GuestView
from .views import GuestListList
from .views import DeleteGuest
from .views import CreateGuest
from .views import UpdateAttendance
from .views import CreateGuestList

urlpatterns = [
    path("", GuestListList.as_view(), name="index"),
    path("list/add/", CreateGuestList.as_view(), name="add-list"),
    path("list/<list_id>/", GuestView.as_view(), name="guests"),
    path("list/<list_id>/guest/<int:pk>/delete", DeleteGuest.as_view(), name="del_guest"),
    path("list/<list_id>/guest/add/", CreateGuest.as_view(), name="add_guest"),
    path("list/<list_id>/guest/<int:pk>/change", UpdateAttendance.as_view(), name="change_attd"),
    path("__reload__/", include("django_browser_reload.urls")),
]