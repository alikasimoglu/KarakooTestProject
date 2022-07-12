from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import UpdateView
from accounts.models import Employee
from accounts.permissions import user_is_employee


@method_decorator([login_required(login_url=reverse_lazy("accounts:login")), user_is_employee], name='dispatch')
class EmployeeProfileUpdateView(UpdateView):
    model = Employee
    fields = ('first_name', 'last_name', 'phone')
    context_object_name = "employee"
    template_name = 'accounts/employee_profile_update.html'

    def form_valid(self, form):
        messages.success(self.request, 'Employee information has been successfully updated!')
        return super().form_valid(form)
