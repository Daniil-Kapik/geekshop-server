from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


def validate_name(value):
    if not value.isdigit():
        raise ValidationError(_(f'Имя не может содержать только цифры'), params={'value': value})