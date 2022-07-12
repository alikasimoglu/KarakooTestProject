from django.db import models
from django.urls import reverse
from accounts.models import User


class Employee(models.Model):
    is_active = models.BooleanField("Status (Active/Passive)", default=True)
    profile = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Profile", primary_key=True)

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone = models.CharField("Phone", max_length=20, blank=True)

    updated_on = models.DateTimeField("Updated on", auto_now=True)
    date_joined = models.DateTimeField("Created on", auto_now_add=True)

    def __str__(self):
        return self.profile.email

    def get_absolute_url(self):
        return reverse("accounts:employee_profile_detail", kwargs={'pk': self.pk})

    class Meta:
        verbose_name_plural = "Employees"
        verbose_name = "Employee"
        ordering = ("date_joined", )
