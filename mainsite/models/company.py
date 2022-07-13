from django.db import models
from accounts.models import Employee
from django.urls import reverse


class Company(models.Model):
    is_active = models.BooleanField("Status (Active/Passive)", default=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, verbose_name="Assigned Employee")

    company_name = models.CharField("Company Name", max_length=50, unique=True)
    company_email = models.EmailField("Company Email", max_length=50, unique=True)
    company_phone = models.CharField("Company Phone", max_length=20, unique=True)
    additional_info = models.TextField("Additional Info", blank=True)

    is_accepted = models.BooleanField("Is Accepted? (Yes/No)", default=False)
    is_email_sent = models.BooleanField("Is Email Sent? (Yes/No)", default=False)
    is_registered = models.BooleanField("Is Registred? (Yes/No)", default=False)

    updated_on = models.DateTimeField("Updated on", auto_now=True)
    date_created = models.DateTimeField("Created on", auto_now_add=True)

    def __str__(self):
        return self.company_name

    def get_absolute_url(self):
        return reverse("mainsite:company_details", kwargs={'pk': self.pk})

    class Meta:
        verbose_name_plural = "Companies"
        verbose_name = "Company"
        ordering = ("-date_created", )
