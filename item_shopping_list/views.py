# Create your views here.
from rest_framework import generics, permissions

from item_shopping_list.models import ShoppingList, Item
from item_shopping_list.permissions import IsModerator, IsUser
from item_shopping_list.serializers import UserShoppingListSerializer, ModeratorShoppingListItemSerializer, \
    ModeratorShoppingListSerializer, CatalogueSerializer, AdminManageItemSerializer, UserEditShoppingListSerializer


# ALL
class Catalogue(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Item.objects.all()
    serializer_class = CatalogueSerializer


# ADMIN
class AdminAddItem(generics.CreateAPIView):
    serializer_class = AdminManageItemSerializer


class AdminEditItem(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = AdminManageItemSerializer


# MODERATOR
class ModeratorShoppingListItem(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsModerator]
    queryset = ShoppingList.objects.all()
    serializer_class = ModeratorShoppingListItemSerializer


class ModeratorShowShoppingList(generics.ListAPIView):
    permission_classes = [IsModerator]
    serializer_class = ModeratorShoppingListSerializer

    def get_queryset(self):
        user = self.kwargs['user']
        return ShoppingList.objects.filter(user=user)


# USER
class UserShowShoppingList(generics.ListAPIView):
    permission_classes = [IsUser]
    serializer_class = UserShoppingListSerializer

    def get_queryset(self):
        return ShoppingList.objects.filter(user=self.request.user)


class UserAddShoppingList(generics.CreateAPIView):
    permission_classes = [IsUser]
    serializer_class = UserShoppingListSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class UserEditShoppingList(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsUser]
    queryset = ShoppingList.objects.all()
    serializer_class = UserEditShoppingListSerializer
