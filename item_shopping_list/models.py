from django.contrib.auth import get_user_model
from django.db import models


# Create your models here.


class Item(models.Model):
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    manufacturer = models.CharField(max_length=50)
    price = models.IntegerField()
    description = models.TextField()

    def __str__(self) -> str:
        return self.id + " - " + self.name


class ShoppingList(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField()
