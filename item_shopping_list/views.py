# Create your views here.
from rest_framework import generics

from item_shopping_list.models import ShoppingList, Item
from item_shopping_list.serializers import UserShoppingListSerializer, ModeratorShoppingListItemSerializer, \
    ModeratorShoppingListSerializer, CatalogueSerializer, AdminManageItemSerializer, UserEditShoppingListSerializer


# ADMIN
class AdminAddItem(generics.CreateAPIView):
    serializer_class = AdminManageItemSerializer


class AdminEditItem(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = AdminManageItemSerializer


# MODERATOR
class ModeratorShoppingListItem(generics.RetrieveUpdateDestroyAPIView):
    queryset = ShoppingList.objects.all()
    serializer_class = ModeratorShoppingListItemSerializer


class ModeratorShowShoppingList(generics.ListAPIView):
    serializer_class = ModeratorShoppingListSerializer

    def get_queryset(self):
        user = self.kwargs['user']
        return ShoppingList.objects.filter(user=user)


# USER
class UserShowShoppingList(generics.ListAPIView):
    serializer_class = UserShoppingListSerializer

    def get_queryset(self):
        return ShoppingList.objects.filter(user=self.request.user)


class UserAddShoppingList(generics.CreateAPIView):
    serializer_class = UserShoppingListSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class UserEditShoppingList(generics.RetrieveUpdateDestroyAPIView):
    queryset = ShoppingList.objects.all()
    serializer_class = UserEditShoppingListSerializer


class Catalogue(generics.ListAPIView):
    queryset = Item.objects.all()
    serializer_class = CatalogueSerializer
