from django.db import models
# from pages.models import customer




# Create your models here.
class customers(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)


def __str__(self):
    return self.first_name + " " + self.last_name