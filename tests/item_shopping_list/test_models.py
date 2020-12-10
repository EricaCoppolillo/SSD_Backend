import pytest
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from mixer.backend.django import mixer


@pytest.fixture()
def item_shopping_list(db):
    return mixer.blend()


# ShoppingListItem name
def test_shopping_list_item_name_length_less_than_1_raises_exception(db):
    shopping_list_item = mixer.blend('item_shopping_list.ShoppingListItem', name='', category='Smartphone',
                                     description='ciao', quantity=1)
    with pytest.raises(ValidationError):
        shopping_list_item.full_clean()


def test_shopping_list_item_name_length_more_than_25_raises_exception(db):
    shopping_list_item = mixer.blend('item_shopping_list.ShoppingListItem', name='a' * 26, category='Smartphone',
                                     description='ciao', quantity=1)
    with pytest.raises(ValidationError):
        shopping_list_item.full_clean()


def test_shopping_list_item_name_forbidden_characters_raises_exception(db):
    shopping_list_item = mixer.blend('item_shopping_list.ShoppingListItem', name='.', category='Smartphone',
                                     description='ciao', quantity=1)
    with pytest.raises(ValidationError):
        shopping_list_item.full_clean()


# ShoppingListItem category
def test_shopping_list_item_category_not_smartphone_or_computer_raises_exception(db):
    shopping_list_item = mixer.blend('item_shopping_list.ShoppingListItem', category='pippo',
                                     description='ciao', quantity=1)
    with pytest.raises(ValidationError):
        shopping_list_item.full_clean()


# ShoppingListItem manufacturer
def test_shopping_list_item_manufacturer_length_less_than_2_raises_exception(db):
    shopping_list_item = mixer.blend('item_shopping_list.ShoppingListItem', manufacturer='m', category='Smartphone',
                                     description='ciao', quantity=1)
    with pytest.raises(ValidationError):
        shopping_list_item.full_clean()


def test_shopping_list_item_manufacturer_length_more_than_20_raises_exception(db):
    shopping_list_item = mixer.blend('item_shopping_list.ShoppingListItem', manufacturer='a' * 21,
                                     category='Smartphone',
                                     description='ciao', quantity=1)
    with pytest.raises(ValidationError):
        shopping_list_item.full_clean()


def test_shopping_list_item_manufacturer_forbidden_characters_raises_exception(db):
    shopping_list_item = mixer.blend('item_shopping_list.ShoppingListItem', manufacturer='.', category='Smartphone',
                                     description='ciao', quantity=1)
    with pytest.raises(ValidationError):
        shopping_list_item.full_clean()


# ShoppingListItem price
def test_shopping_list_item_price_less_than_0_raises_exception(db):
    shopping_list_item = mixer.blend('item_shopping_list.ShoppingListItem', price=-1, category='Smartphone',
                                     description='ciao', quantity=1)
    with pytest.raises(ValidationError):
        shopping_list_item.full_clean()


def test_shopping_list_item_price_greater_than_100_billion_cents_raises_exception(db):
    shopping_list_item = mixer.blend('item_shopping_list.ShoppingListItem', price=100000000000, category='Smartphone',
                                     description='ciao', quantity=1)
    with pytest.raises(ValidationError):
        shopping_list_item.full_clean()


# ShoppingListItem description
def test_shopping_list_item_description_length_more_than_100_raises_exception(db):
    shopping_list_item = mixer.blend('item_shopping_list.ShoppingListItem', description='a' * 101,
                                     category='Smartphone',
                                     quantity=1)
    with pytest.raises(ValidationError):
        shopping_list_item.full_clean()


def test_shopping_list_item_description_forbidden_characters_raises_exception(db):
    shopping_list_item = mixer.blend('item_shopping_list.ShoppingListItem', description='\\', category='Smartphone',
                                     quantity=1)
    with pytest.raises(ValidationError):
        shopping_list_item.full_clean()


# ShoppingListItem __str__()
def test_shopping_list_item_str(db):
    user = mixer.blend(get_user_model(), username='test')
    shopping_list_item = mixer.blend('item_shopping_list.ShoppingListItem', user=user, name='Test')
    assert str(shopping_list_item) == 'test - Test'


# ShoppingListItem quantity
def test_shopping_list_item_quantity_less_than_1_raises_exception(db):
    shopping_list_item = mixer.blend('item_shopping_list.ShoppingListItem', category='Smartphone',
                                     description='ciao', quantity=0)
    with pytest.raises(ValidationError):
        shopping_list_item.full_clean()


def test_shopping_list_item_quantity_greater_than_5_raises_exception(db):
    shopping_list_item = mixer.blend('item_shopping_list.ShoppingListItem', category='Smartphone',
                                     description='ciao', quantity=6)
    with pytest.raises(ValidationError):
        shopping_list_item.full_clean()
