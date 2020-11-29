import pytest
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from mixer.backend.django import mixer


# Item name
def test_item_name_length_less_than_1_raises_exception(db):
    item = mixer.blend('item_shopping_list.Item', name='')
    with pytest.raises(ValidationError):
        item.full_clean()


def test_item_name_length_more_than_50_raises_exception(db):
    item = mixer.blend('item_shopping_list.Item', name='a' * 51)
    with pytest.raises(ValidationError):
        item.full_clean()


def test_item_name_forbidden_characters_raises_exception(db):
    item = mixer.blend('item_shopping_list.Item', name='.')
    with pytest.raises(ValidationError):
        item.full_clean()


# Item category
def test_item_category_length_less_than_1_raises_exception(db):
    item = mixer.blend('item_shopping_list.Item', category='')
    with pytest.raises(ValidationError):
        item.full_clean()


def test_item_category_length_more_than_20_raises_exception(db):
    item = mixer.blend('item_shopping_list.Item', category='a' * 21)
    with pytest.raises(ValidationError):
        item.full_clean()


def test_item_category_forbidden_characters_raises_exception(db):
    item = mixer.blend('item_shopping_list.Item', category='.')
    with pytest.raises(ValidationError):
        item.full_clean()


# Item manufacturer
def test_item_manufacturer_length_less_than_1_raises_exception(db):
    item = mixer.blend('item_shopping_list.Item', manufacturer='')
    with pytest.raises(ValidationError):
        item.full_clean()


def test_item_manufacturer_length_more_than_50_raises_exception(db):
    item = mixer.blend('item_shopping_list.Item', manufacturer='a' * 51)
    with pytest.raises(ValidationError):
        item.full_clean()


def test_item_manufacturer_forbidden_characters_raises_exception(db):
    item = mixer.blend('item_shopping_list.Item', manufacturer='.')
    with pytest.raises(ValidationError):
        item.full_clean()


# Item price
def test_item_price_less_than_0_raises_exception(db):
    item = mixer.blend('item_shopping_list.Item', price=-1)
    with pytest.raises(ValidationError):
        item.full_clean()


def test_item_price_greater_than_100_million_cents_raises_exception(db):
    item = mixer.blend('item_shopping_list.Item', price=100000001)
    with pytest.raises(ValidationError):
        item.full_clean()


# Item description
def test_item_description_length_less_than_1_raises_exception(db):
    item = mixer.blend('item_shopping_list.Item', description='')
    with pytest.raises(ValidationError):
        item.full_clean()


def test_item_description_length_more_than_500_raises_exception(db):
    item = mixer.blend('item_shopping_list.Item', description='a' * 501)
    with pytest.raises(ValidationError):
        item.full_clean()


def test_item_description_forbidden_characters_raises_exception(db):
    item = mixer.blend('item_shopping_list.Item', description='\\')
    with pytest.raises(ValidationError):
        item.full_clean()


# Item __str__()
def test_item_str(db):
    item = mixer.blend('item_shopping_list.Item', id=1, name='Test')
    assert str(item) == '1 - Test'


# ShoppingList quantity
def test_shopping_list_quantity_less_than_1_raises_exception(db):
    shopping_list = mixer.blend('item_shopping_list.ShoppingList', quantity=0)
    with pytest.raises(ValidationError):
        shopping_list.full_clean()


def test_shopping_list_quantity_greater_than_999_raises_exception(db):
    shopping_list = mixer.blend('item_shopping_list.ShoppingList', quantity=1000)
    with pytest.raises(ValidationError):
        shopping_list.full_clean()


# ShoppingList __str__
def test_shopping_list_str(db):
    user = mixer.blend(get_user_model(), username='john')
    item = mixer.blend('item_shopping_list.Item', id=1, name='iPhone')
    shopping_list = mixer.blend('item_shopping_list.ShoppingList', user=user, item=item, quantity=3)
    assert str(shopping_list) == 'john - iPhone - 3'
