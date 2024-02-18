from django.db import models

# Create your models here.
class Site(models.Model):
    nom = models.CharField(max_length=25)
    url = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    identifiant = models.CharField(max_length=50, null=True)
    password = models.CharField(max_length=16)