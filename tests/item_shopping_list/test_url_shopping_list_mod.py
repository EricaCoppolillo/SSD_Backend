import pytest
from allauth import models
from django.contrib.auth import get_user_model, models
from mixer.backend.django import mixer
from rest_framework.status import HTTP_403_FORBIDDEN, HTTP_200_OK, HTTP_405_METHOD_NOT_ALLOWED

from tests.item_shopping_list.test_urls_utils import get_client, parse

path = '/api/v1/shopping-list/mod/1'


@pytest.fixture()
def shopping_list_items(db):
    user = mixer.blend(get_user_model(), id=1)
    return [

        mixer.blend('item_shopping_list.ShoppingListItem', user=user),
        mixer.blend('item_shopping_list.ShoppingListItem', user=user),
        mixer.blend('item_shopping_list.ShoppingListItem', user=user),
    ]


@pytest.fixture()
def shopping_list_item(db):
    return {
        'quantity': 1,
        'name': 'name',
        'category': 'category',
        'manufacturer': 'manufacturer',
        'price': 1,
        'description': 'description',
    }


def test_moderator_get_ok_and_correct_number_of_items(shopping_list_items):
    user = mixer.blend(get_user_model())
    group = mixer.blend(models.Group, name='moderator')
    group.user_set.add(user)
    client = get_client(user)
    response = client.get(path)
    assert response.status_code == HTTP_200_OK
    obj = parse(response)
    assert len(obj) == 3


def test_moderator_post_method_not_allowed(shopping_list_items, shopping_list_item):
    user = mixer.blend(get_user_model())
    group = mixer.blend(models.Group, name='moderator')
    group.user_set.add(user)
    client = get_client(user)
    response = client.post(path, data=shopping_list_item)
    assert response.status_code == HTTP_405_METHOD_NOT_ALLOWED


def test_moderator_put_method_not_allowed(shopping_list_items, shopping_list_item):
    user = mixer.blend(get_user_model())
    group = mixer.blend(models.Group, name='moderator')
    group.user_set.add(user)
    client = get_client(user)
    response = client.put(path, data=shopping_list_item)
    assert response.status_code == HTTP_405_METHOD_NOT_ALLOWED


def test_moderator_delete_method_not_allowed(shopping_list_items):
    user = mixer.blend(get_user_model())
    group = mixer.blend(models.Group, name='moderator')
    group.user_set.add(user)
    client = get_client(user)
    response = client.delete(path)
    assert response.status_code == HTTP_405_METHOD_NOT_ALLOWED


def test_user_get_forbidden(shopping_list_items):
    user = mixer.blend(get_user_model())
    mixer.blend('item_shopping_list.ShoppingListItem', user=user)
    client = get_client(user)
    response = client.get(path)
    assert response.status_code == HTTP_403_FORBIDDEN


def test_user_post_forbidden(shopping_list_items, shopping_list_item):
    user = mixer.blend(get_user_model())
    client = get_client(user)
    response = client.post(path, data=shopping_list_item)
    assert response.status_code == HTTP_403_FORBIDDEN


def test_user_put_forbidden(shopping_list_items, shopping_list_item):
    user = mixer.blend(get_user_model())
    client = get_client(user)
    response = client.put(path, data=shopping_list_item)
    assert response.status_code == HTTP_403_FORBIDDEN


def test_user_delete_forbidden(shopping_list_items):
    user = mixer.blend(get_user_model())
    client = get_client(user)
    response = client.delete(path)
    assert response.status_code == HTTP_403_FORBIDDEN
