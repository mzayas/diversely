from django.db import models


# Create your models here.
class Position(models.Model):
    title = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    term = models.CharField(max_length=50)
