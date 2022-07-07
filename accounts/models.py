from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_employee = models.BooleanField('Is Employee?', default=False)
    is_customer = models.BooleanField('Is Customer?', default=False)

    class Meta:
        verbose_name_plural = "Accounts"
        verbose_name = "Account"
