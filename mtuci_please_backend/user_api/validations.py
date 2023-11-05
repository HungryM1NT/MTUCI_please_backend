from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
UserModel = get_user_model()


def custom_validation(data):
    username = data['username'].strip()
    email = data['email'].strip()
    password = data['password'].strip()

    if not username or UserModel.objects.filter(username=username).exists():
        raise ValidationError('Выберите другое имя пользователя')
    if not email:
        raise ValidationError('Выберите другую почту')
    if not password or len(password) < 8:
        raise ValidationError('Выберите другой пароль (8 символов и больше)')

    return data


def validate_username(data):
    username = data['username'].strip()
    if not username:
        raise ValidationError('Необходимо ввести имя пользователя')
    return True


def validate_password(data):
    password = data['password'].strip()
    if not password:
        raise ValidationError('Необходимо ввести пароль')
    return True
