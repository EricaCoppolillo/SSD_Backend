import pytest
from allauth import models
from django.contrib.auth import get_user_model, models
from mixer.backend.django import mixer
from rest_framework.status import HTTP_403_FORBIDDEN, HTTP_405_METHOD_NOT_ALLOWED, HTTP_200_OK

from tests.item_shopping_list.test_urls_utils import get_client, parse

path = '/api/v1/users/'


@pytest.fixture()
def users(db):
    return [
        mixer.blend(get_user_model()),
        mixer.blend(get_user_model()),
        mixer.blend(get_user_model()),
    ]


@pytest.fixture()
def user_fixture(db):
    return {
        'id': 1
    }


def test_moderator_get_ok_and_number_of_elements(users):
    user = mixer.blend(get_user_model())
    group = mixer.blend(models.Group, name='moderator')
    group.user_set.add(user)
    client = get_client(user)
    response = client.get(path)
    assert response.status_code == HTTP_200_OK
    obj = parse(response)
    assert len(obj) == len(users)


def test_moderator_post_not_allowed(users, user_fixture):
    user = mixer.blend(get_user_model())
    group = mixer.blend(models.Group, name='moderator')
    group.user_set.add(user)
    client = get_client(user)
    response = client.post(path, data=user_fixture)
    assert response.status_code == HTTP_405_METHOD_NOT_ALLOWED


def test_moderator_put_not_allowed(users, user_fixture):
    user = mixer.blend(get_user_model())
    group = mixer.blend(models.Group, name='moderator')
    group.user_set.add(user)
    client = get_client(user)
    response = client.put(path, data=user_fixture)
    assert response.status_code == HTTP_405_METHOD_NOT_ALLOWED


def test_moderator_delete_not_allowed(users):
    user = mixer.blend(get_user_model())
    group = mixer.blend(models.Group, name='moderator')
    group.user_set.add(user)
    client = get_client(user)
    response = client.delete(path)
    assert response.status_code == HTTP_405_METHOD_NOT_ALLOWED


def test_user_get_method_forbidden(users):
    user = mixer.blend(get_user_model(), id=1)
    client = get_client(user)
    response = client.get(path)
    assert response.status_code == HTTP_403_FORBIDDEN


def test_user_post_method_forbidden(users, user_fixture):
    user = mixer.blend(get_user_model(), id=1)
    client = get_client(user)
    response = client.post(path, data=user_fixture)
    assert response.status_code == HTTP_403_FORBIDDEN


def test_user_put_method_forbidden(users, user_fixture):
    user = mixer.blend(get_user_model(), id=1)
    client = get_client(user)
    response = client.put(path, data=user_fixture)
    assert response.status_code == HTTP_403_FORBIDDEN


def test_user_delete_forbidden(users):
    user = mixer.blend(get_user_model(), id=1)
    client = get_client(user)
    response = client.delete(path)
    assert response.status_code == HTTP_403_FORBIDDEN
