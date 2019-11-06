import decimal
from decimal import Decimal
from django.db import models


class Topping(models.Model):
    name = models.CharField(max_length=30)
    price = models.DecimalField(max_length=4, max_digits=4, decimal_places=2, default=1.99)
    def __str__(self):
        return self.name

class Pizza(models.Model):
    toppings = models.ManyToManyField(Topping, null=True)
    name = models.CharField(max_length=30)
    price =  models.DecimalField(max_length=4, max_digits=4, decimal_places=2, default=4.99)
    size = models.CharField(max_length=12)
    def __str__(self):
        return self.name