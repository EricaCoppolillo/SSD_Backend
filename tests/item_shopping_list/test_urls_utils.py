import json

import mixer
import pytest
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from mixer.backend.django import mixer
from rest_framework.status import HTTP_200_OK, HTTP_403_FORBIDDEN, HTTP_201_CREATED
from rest_framework.test import APIClient


# TODO: test below urls                     GET POST    PUT DELETE  N.ITEMS
# catalogue/                                X                       X
# catalogue/add/                                X                   -
# catalogue/edit/item_id
# shopping-list/mod/user_id
# shopping-list/mod/edit/shopping_list_id
# shopping-list/
# shopping-list/add/
# shopping-list/edit/shopping_list_id

@pytest.fixture()
def items(db):
    return [
        mixer.blend('item_shopping_list.Item'),
        mixer.blend('item_shopping_list.Item'),
        mixer.blend('item_shopping_list.Item'),
    ]


@pytest.fixture()
def item(db):
    return {
        'name': 'name',
        'category': 'category',
        'manufacturer': 'manufacturer',
        'price': 1,
        'description': 'description',
    }


def get_client(user=None):
    res = APIClient()
    if user is not None:
        res.force_login(user)
    return res


def parse(response):
    response.render()
    content = response.content.decode()
    return json.loads(content)


# catalogue/
def test_any_get_catalogue_ok(db):
    path = '/api/v1/catalogue/'
    client = get_client()
    response = client.get(path)
    assert response.status_code == HTTP_200_OK


def test_get_catalogue_returns_all_items(items):
    path = '/api/v1/catalogue/'
    client = get_client()
    response = client.get(path)
    assert response.status_code == HTTP_200_OK
    obj = parse(response)
    assert len(obj) == len(items)


# catalogue/add/
def test_user_post_catalogue_add_forbidden(db, item):
    path = '/api/v1/catalogue/add/'
    user = mixer.blend(get_user_model())
    group = mixer.blend(Group, name='user')
    group.user_set.add(user)
    client = get_client(user)
    response = client.post(path, data=item)
    assert response.status_code == HTTP_403_FORBIDDEN


def test_moderator_post_catalogue_add_forbidden(db, item):
    path = '/api/v1/catalogue/add/'
    user = mixer.blend(get_user_model())
    group = mixer.blend(Group, name='moderator')
    group.user_set.add(user)
    client = get_client(user)
    response = client.post(path, data=item)
    assert response.status_code == HTTP_403_FORBIDDEN


def test_admin_post_catalogue_add_created(db, admin_user, item):
    path = '/api/v1/catalogue/add/'
    client = get_client(admin_user)
    response = client.post(path, data=item)
    assert response.status_code == HTTP_201_CREATED
