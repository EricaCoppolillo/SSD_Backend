from django.urls import path, re_path

from item_shopping_list.views import UserShowShoppingList, ModeratorShoppingListItem, ModeratorShowShoppingList, \
    UserAddShoppingList, UserEditShoppingList

urlpatterns = [
    # MODERATOR
    re_path('shopping-list/mod/(?P<user>\\d+)', ModeratorShowShoppingList.as_view()),
    path('shopping-list/mod/edit/<int:pk>', ModeratorShoppingListItem.as_view()),

    # USER
    path('shopping-list/', UserShowShoppingList.as_view()),
    path('shopping-list/add/', UserAddShoppingList.as_view()),
    path('shopping-list/edit/<int:pk>', UserEditShoppingList.as_view()),
]
