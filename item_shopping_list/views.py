# Create your views here.
from rest_framework import generics

from item_shopping_list.models import ShoppingListItem
from item_shopping_list.permissions import IsModerator, IsUser
from item_shopping_list.serializers import UserShoppingListSerializer, ModeratorShoppingListSerializer, \
    UserEditShoppingListSerializer


# MODERATOR
class ModeratorShoppingListItem(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsModerator]
    queryset = ShoppingListItem.objects.all()
    serializer_class = ModeratorShoppingListSerializer


class ModeratorShowShoppingList(generics.ListAPIView):
    permission_classes = [IsModerator]
    serializer_class = ModeratorShoppingListSerializer

    def get_queryset(self):
        user = self.kwargs['user']
        return ShoppingListItem.objects.filter(user=user)


# USER
class UserShowShoppingList(generics.ListAPIView):
    permission_classes = [IsUser]
    serializer_class = UserShoppingListSerializer

    def get_queryset(self):
        return ShoppingListItem.objects.filter(user=self.request.user)


class UserAddShoppingList(generics.CreateAPIView):
    permission_classes = [IsUser]
    serializer_class = UserShoppingListSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class UserEditShoppingList(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsUser]
    queryset = ShoppingListItem.objects.all()
    serializer_class = UserEditShoppingListSerializer
