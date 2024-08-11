from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None
    email = models.EmailField(
        verbose_name="Email",
        unique=True,
    )
    phone = models.CharField(
        max_length=35,
        verbose_name='Телефон',
        blank=True,
        null=True,
        help_text='Введите номер телефона',
    )
    country = models.CharField(
        max_length=50,
        verbose_name='Страна',
        blank=True,
        null=True,
        help_text='Введите страну',
    )
    avatar = models.ImageField(
        blank=True,
        null=True,
        verbose_name='Аватар',
        help_text='Загрузите аватар',
        upload_to="users/avatar",
    )
    token = models.CharField(max_length=100, blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

    def __str__(self):
        return self.email
