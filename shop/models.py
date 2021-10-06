from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    img = models.CharField(max_length=200)
    info = models.CharField(max_length=200)
    amt = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class User(models.Model):
    username = models.CharField(max_length=50)
    cart = models.CharField(max_length=2000)

    def __str__(self):
        return self.username

