from django.db import models

# Create models here.
class Idea(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
