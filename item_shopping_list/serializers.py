from rest_framework import serializers

from item_shopping_list.models import ShoppingList, Item


# ADMIN
class AdminManageItemSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'name', 'category', 'manufacturer', 'price', 'description')
        model = Item


# MODERATOR
class ModeratorShoppingListItemSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'quantity')
        model = ShoppingList


class ModeratorShoppingListSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'user', 'item', 'quantity')
        model = ShoppingList


# USER
class UserShoppingListSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('item', 'quantity')
        model = ShoppingList


class UserEditShoppingListSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'quantity')
        model = ShoppingList


class CatalogueSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'name', 'category', 'manufacturer', 'price', 'description')
        model = Item
