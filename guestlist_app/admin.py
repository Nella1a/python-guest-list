from django.contrib import admin
from .models import GuestList
from .models import Guests

# Register your models here.

admin.site.register(GuestList)
admin.site.register(Guests)