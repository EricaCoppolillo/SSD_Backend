from rest_framework import serializers

from item_shopping_list.models import ShoppingListItem


# TODO: some refactor

# MODERATOR
class ModeratorShoppingListSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'name', 'category', 'manufacturer', 'price', 'description', 'quantity')
        model = ShoppingListItem


# USER
class UserShoppingListSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'name', 'category', 'manufacturer', 'price', 'description', 'quantity')
        model = ShoppingListItem


class UserEditShoppingListSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'quantity')
        model = ShoppingListItem
