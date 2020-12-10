from django.contrib.auth import get_user_model
from django.core.validators import RegexValidator
from django.db import models

# Create your models here.
from django.db.models import CheckConstraint

from item_shopping_list.validators import validate_price, validate_quantity


class ShoppingListItem(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    quantity = models.IntegerField(validators=[validate_quantity])
    name = models.CharField(max_length=25, validators=[RegexValidator(r'^[A-Za-z0-9 \-\_]+$')])
    category = models.CharField(max_length=10, validators=[RegexValidator(r'^(Smartphone|Computer)$')])
    manufacturer = models.CharField(max_length=20, validators=[RegexValidator(r'^[A-Za-z \_\-\&]{2,20}$')])
    price = models.IntegerField(validators=[validate_price])
    description = models.TextField(blank=True,
                                   validators=[RegexValidator(r'^[A-Za-z0-9\_\-\(\)\.\,\;\&\:\=\è\'\"\! ]{1,100}$')])

    def __str__(self) -> str:
        return str(self.user) + " - " + self.name

