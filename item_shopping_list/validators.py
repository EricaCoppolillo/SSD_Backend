from django.core.exceptions import ValidationError


def validate_price(value: int) -> None:
    if not value >= 0:
        raise ValidationError('Price can\'t be negative')
    if not value <= 100000000:
        raise ValidationError('Price can\'t be greater than 1,000,000.00')


def validate_quantity(value: int) -> None:
    if not value >= 1:
        raise ValidationError('Quantity can\'t be less than 1')
    if not value <= 999:
        raise ValidationError('Quantity can\'t be greater than 999')
