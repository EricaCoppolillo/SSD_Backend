from django.contrib.auth import get_user_model
from rest_framework import serializers

from item_shopping_list.models import ShoppingListItem


# TODO: some refactor

# MODERATOR
class ModeratorUserListSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'username')
        model = get_user_model()


class ModeratorShoppingListSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'name', 'quantity')
        model = ShoppingListItem

    name = serializers.ReadOnlyField()


# USER
class UserShoppingListSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'name', 'category', 'manufacturer', 'price', 'description', 'quantity')
        model = ShoppingListItem


class UserEditShoppingListSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'quantity')
        model = ShoppingListItem
