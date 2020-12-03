import pytest
from allauth import models
from django.contrib.auth import get_user_model, models
from mixer.backend.django import mixer
from rest_framework.status import HTTP_403_FORBIDDEN, HTTP_405_METHOD_NOT_ALLOWED, HTTP_201_CREATED

from tests.item_shopping_list.test_urls_utils import get_client

path = '/api/v1/shopping-list/add/'


@pytest.fixture()
def shopping_list_items(db):
    return [
        mixer.blend('item_shopping_list.ShoppingListItem'),
        mixer.blend('item_shopping_list.ShoppingListItem'),
        mixer.blend('item_shopping_list.ShoppingListItem'),
    ]


@pytest.fixture()
def shopping_list_item(db):
    return {
        'quantity': 1,
        'name': 'name',
        'category': 'Smartphone',
        'manufacturer': 'manufacturer',
        'price': 1,
        'description': 'description',
    }


def test_moderator_get_forbidden(db):
    user = mixer.blend(get_user_model())
    group = mixer.blend(models.Group, name='moderator')
    group.user_set.add(user)
    client = get_client(user)
    response = client.get(path)
    assert response.status_code == HTTP_403_FORBIDDEN


def test_moderator_post_forbidden(shopping_list_item):
    user = mixer.blend(get_user_model())
    group = mixer.blend(models.Group, name='moderator')
    group.user_set.add(user)
    client = get_client(user)
    response = client.post(path, data=shopping_list_item)
    assert response.status_code == HTTP_403_FORBIDDEN


def test_moderator_put_forbidden(shopping_list_item):
    user = mixer.blend(get_user_model())
    group = mixer.blend(models.Group, name='moderator')
    group.user_set.add(user)
    client = get_client(user)
    response = client.put(path, data=shopping_list_item)
    assert response.status_code == HTTP_403_FORBIDDEN


def test_moderator_delete_forbidden(db):
    user = mixer.blend(get_user_model())
    group = mixer.blend(models.Group, name='moderator')
    group.user_set.add(user)
    client = get_client(user)
    response = client.delete(path)
    assert response.status_code == HTTP_403_FORBIDDEN


def test_user_get_method_not_allowed(db):
    user = mixer.blend(get_user_model())
    client = get_client(user)
    response = client.get(path)
    assert response.status_code == HTTP_405_METHOD_NOT_ALLOWED


def test_user_post_created(shopping_list_item):
    user = mixer.blend(get_user_model())
    client = get_client(user)
    response = client.post(path, data=shopping_list_item)
    assert response.status_code == HTTP_201_CREATED


def test_user_put_method_not_allowed(shopping_list_item):
    user = mixer.blend(get_user_model())
    client = get_client(user)
    response = client.put(path, data=shopping_list_item)
    assert response.status_code == HTTP_405_METHOD_NOT_ALLOWED


def test_user_delete_method_not_allowed(db):
    user = mixer.blend(get_user_model())
    client = get_client(user)
    response = client.delete(path)
    assert response.status_code == HTTP_405_METHOD_NOT_ALLOWED
