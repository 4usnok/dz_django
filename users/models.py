from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name="Email")

    img_avatar = models.ImageField(
        verbose_name="Img",
        help_text="Загрузите своё фото профиля",
        upload_to="users/avatars/",
        blank=True,
        null=True,
        )
    number_phone = models.CharField(
        verbose_name="Number",
        help_text="Введите пожалуйста номер телефона",
        max_length=50,
        blank=True,
        null=True,
        )
    country = models.CharField(
        verbose_name="Country",
        help_text="Введите пожалуйста страну",
        max_length=50,
        null=True,
        )

    USERNAME_FIELD = "email" # В качестве уникального поля, используется email
    REQUIRED_FIELDS = [] # При создании пользователя через команду createsuperuser, никаких доп.полей не используется

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email

