from django.contrib import admin

from item_shopping_list.models import Item, ShoppingList

# Register your models here.

admin.site.register(Item)
admin.site.register(ShoppingList)
