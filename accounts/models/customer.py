from django.db import models
from accounts.models import User
from mainsite.models import Company


class Customer(models.Model):
    is_active = models.BooleanField("Status (Active/Passive)", default=True)
    profile = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Profile", primary_key=True)
    # company = models.OneToOneField(Company, on_delete=models.CASCADE, verbose_name="Company", primary_key=True)

    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    phone = models.CharField("Phone", max_length=20, blank=True)
    representative_name = models.CharField("Representative Name", max_length=50, blank=True)
    representative_phone = models.CharField("Representative Phone", max_length=20, blank=True)

    updated_on = models.DateTimeField("Updated on", auto_now=True)
    date_joined = models.DateTimeField("Created on", auto_now_add=True)

    def __str__(self):
        return self.profile.email

    class Meta:
        verbose_name_plural = "Customers"
        verbose_name = "Customer"
        ordering = ("date_joined", )
