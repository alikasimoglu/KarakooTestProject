from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import DetailView
from accounts.models import Employee
from accounts.permissions import user_is_employee


@method_decorator([login_required(login_url=reverse_lazy("accounts:login")), user_is_employee], name='dispatch')
class EmployeeProfileView(DetailView):
    model = Employee
    context_object_name = "employee"
    template_name = 'accounts/employee_profile_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def dispatch(self, request, *args, **kwargs):
        handler = super().dispatch(request, *args, **kwargs)
        user = self.request.user.id
        employee = self.get_object()
        if employee.profile_id != user:
            raise PermissionDenied
        return handler
