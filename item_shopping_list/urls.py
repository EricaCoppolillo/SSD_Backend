from django.urls import path, re_path

from item_shopping_list.views import UserShoppingList, ModeratorShoppingListItem, ModeratorShoppingList, Catalogue

urlpatterns = [
    # MODERATOR
    re_path('shopping-list/(?P<user>\\d+)', ModeratorShoppingList.as_view()),
    path('modify-shopping-list-item/<int:pk>', ModeratorShoppingListItem.as_view()),

    # USER
    path('shopping-list/', UserShoppingList.as_view()),
    path('catalogue/', Catalogue.as_view()),
]
