# Create your views here.
from rest_framework import generics

from item_shopping_list.models import ShoppingList, Item
from item_shopping_list.serializers import UserShoppingListSerializer, ModeratorShoppingListItemSerializer, \
    ModeratorShoppingListSerializer, CatalogueSerializer


# MODERATOR
class ModeratorShoppingListItem(generics.RetrieveUpdateDestroyAPIView):
    queryset = ShoppingList.objects.all()
    serializer_class = ModeratorShoppingListItemSerializer


class ModeratorShoppingList(generics.ListAPIView):
    serializer_class = ModeratorShoppingListSerializer

    def get_queryset(self):
        user = self.kwargs['user']
        return ShoppingList.objects.filter(user=user)


# USER
class UserShoppingList(generics.ListAPIView):
    serializer_class = UserShoppingListSerializer

    def get_queryset(self):
        return ShoppingList.objects.filter(user=self.request.user)


class Catalogue(generics.ListAPIView):
    queryset = Item.objects.all()
    serializer_class = CatalogueSerializer
