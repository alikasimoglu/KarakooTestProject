from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from accounts.models import User, Employee


class EmployeeSignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    phone = forms.CharField(required=False)

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2', 'first_name', 'last_name')

    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_employee = True
        user.save()
        employee = Employee.objects.create(profile=user)
        employee.profile.email = self.cleaned_data.get('email')
        employee.first_name = self.cleaned_data.get('first_name')
        employee.last_name = self.cleaned_data.get('last_name')
        employee.phone = self.cleaned_data.get('phone')
        employee.save()
        return user
