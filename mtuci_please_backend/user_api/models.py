from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin


class AppUserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not username:
            raise ValueError('Необходимо указать имя пользователя')
        if not email:
            raise ValueError('Необходимо указать почту')
        if not password:
            raise ValueError('Необходимо указать пароль')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email, password=None):
        user = self.create_user(username, email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user


class AppUser(AbstractBaseUser, PermissionsMixin):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=50)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    objects = AppUserManager()


    def __str__(self):
        return self.username
