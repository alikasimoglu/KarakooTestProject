from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import DetailView
from accounts.models import Customer
from accounts.permissions import user_is_customer


@method_decorator([login_required(login_url=reverse_lazy("accounts:login")), user_is_customer], name='dispatch')
class CustomerProfileView(DetailView):
    model = Customer
    context_object_name = "customer"
    template_name = 'accounts/customer_profile_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def dispatch(self, request, *args, **kwargs):
        handler = super().dispatch(request, *args, **kwargs)
        user = self.request.user.id
        customer = self.get_object()
        if customer.profile_id != user:
            raise PermissionDenied
        return handler
