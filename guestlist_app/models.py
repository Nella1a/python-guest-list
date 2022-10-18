from django.db import models

# Create your models here.

class GuestList(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    attending = models.BooleanField(default=True)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

