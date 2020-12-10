# Create your views here.
from http.client import HTTPException

from django.contrib.auth import get_user_model
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseBadRequest
from rest_framework import generics
from rest_framework.exceptions import APIException
from rest_framework.status import HTTP_400_BAD_REQUEST

from item_shopping_list.models import ShoppingListItem
from item_shopping_list.permissions import IsModerator, IsUser
from item_shopping_list.serializers import UserShoppingListSerializer, ModeratorShoppingListSerializer, \
    UserEditShoppingListSerializer, ModeratorUserListSerializer


# MODERATOR
class ModeratorUserList(generics.ListAPIView):
    permission_classes = [IsModerator]
    serializer_class = ModeratorUserListSerializer

    def get_queryset(self):
        return get_user_model().objects.filter(is_superuser=False).exclude(groups__name='moderator')


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
        if ShoppingListItem.objects.filter(user=self.request.user).count() >= 10:
            raise APIException('There are more than 10 items in your shopping list')
        serializer.save(user=self.request.user)


class UserEditShoppingList(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsUser]
    queryset = ShoppingListItem.objects.all()
    serializer_class = UserEditShoppingListSerializer
