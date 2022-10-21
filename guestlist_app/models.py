from django.db import models

# Create your models here.
class GuestList(models.Model):
    title = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Guestlists"






class Guests(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    attending = models.BooleanField(default=True)
    list = models.ForeignKey(GuestList, on_delete=models.CASCADE)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

    class Meta:
        verbose_name_plural = "Guests"