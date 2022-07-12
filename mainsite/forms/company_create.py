from django import forms
from django.forms import TextInput
from mainsite.models import Company


class CompanyCreateForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ('employee', 'company_name', 'company_email', 'company_phone', 'additional_info')

        widgets = {
            'employee': TextInput(attrs={'readonly': 'readonly', 'hidden': 'hidden'}),
        }
        labels = {
            'employee': '',
        }
