from django.db import models

class Product(models.Model):
    name = models.CharField("Product name", max_length=200)
    term = models.IntegerField()
