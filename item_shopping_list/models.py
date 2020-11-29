from django.contrib.auth import get_user_model
from django.core.validators import RegexValidator
from django.db import models

# Create your models here.
from item_shopping_list.validators import validate_price, validate_quantity


class Item(models.Model):
    name = models.CharField(max_length=50, validators=[RegexValidator(r'^[\w\s,\'"]+$')])
    category = models.CharField(max_length=20, validators=[RegexValidator(r'^[\w\s]+$')])
    manufacturer = models.CharField(max_length=50, validators=[RegexValidator(r'^[\w\s,\'"]+$')])
    price = models.IntegerField(validators=[validate_price])
    description = models.TextField(validators=[RegexValidator(r'^[\w\s,.:;()\'"]{1,500}$')])

    def __str__(self) -> str:
        return str(self.id) + " - " + self.name


class ShoppingList(models.Model):
    # TODO: ask to prof if these fks need to be tested
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(validators=[validate_quantity])

    def __str__(self) -> str:
        return str(self.user) + " - " + str(self.item.name) + " - " + str(self.quantity)
