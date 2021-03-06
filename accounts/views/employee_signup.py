from django.contrib.auth import login
from django.shortcuts import redirect
from django.views.generic import CreateView
from accounts.forms import EmployeeSignUpForm
from accounts.models import User


class EmployeeSignUpView(CreateView):
    model = User
    form_class = EmployeeSignUpForm
    template_name = 'accounts/employee_signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'employee'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('mainsite:index')
