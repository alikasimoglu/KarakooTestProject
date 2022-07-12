from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.forms import TextInput
from django.shortcuts import get_object_or_404

from accounts.models import User, Customer
from mainsite.models import Company


class CustomerSignUpForm(UserCreationForm):
    # company = forms.CharField(required=True, widget=TextInput(attrs={'readonly': 'readonly'}))
    email = forms.EmailField(required=True)
    representative_name = forms.CharField(required=False)
    representative_phone = forms.CharField(required=False)

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2', 'representative_name', 'representative_phone')

    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_customer = True
        user.save()

        # employee = get_object_or_404(Company)
        # customer_company = Company.objects.get(employee__company=employee.pk)

        customer = Customer.objects.create(profile=user)
        # customer_company.company_name = self.cleaned_data.get('company')
        customer.profile.email = self.cleaned_data.get('email')
        customer.representative_name = self.cleaned_data.get('representative_name')
        customer.representative_phone = self.cleaned_data.get('representative_phone')
        customer.save()
        return user
