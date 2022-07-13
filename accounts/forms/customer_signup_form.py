from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.forms import TextInput
from accounts.models import User, Customer


class CustomerSignUpForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=TextInput(attrs={'readonly': 'readonly'}))
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    phone = forms.CharField(required=False)
    representative_name = forms.CharField(required=False)
    representative_phone = forms.CharField(required=False)

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2', 'first_name', 'last_name', 'phone', 'representative_name', 'representative_phone')

    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_customer = True
        user.save()

        customer = Customer.objects.create(profile=user)
        customer.profile.email = self.cleaned_data.get('email')
        customer.first_name = self.cleaned_data.get('first_name')
        customer.last_name = self.cleaned_data.get('last_name')
        customer.phone = self.cleaned_data.get('phone')
        customer.representative_name = self.cleaned_data.get('representative_name')
        customer.representative_phone = self.cleaned_data.get('representative_phone')
        customer.save()
        return user
