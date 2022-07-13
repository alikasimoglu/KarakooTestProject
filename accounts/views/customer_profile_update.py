from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import UpdateView
from accounts.models import Customer
from accounts.permissions import user_is_customer


@method_decorator([login_required(login_url=reverse_lazy("accounts:login")), user_is_customer], name='dispatch')
class CustomerProfileUpdateView(UpdateView):
    model = Customer
    fields = ('first_name', 'last_name', 'phone', 'representative_name', 'representative_phone')
    context_object_name = "customer"
    template_name = 'accounts/customer_profile_update.html'

    def form_valid(self, form):
        messages.success(self.request, 'Customer information has been successfully updated!')
        return super().form_valid(form)

    def dispatch(self, request, *args, **kwargs):
        handler = super().dispatch(request, *args, **kwargs)
        user = self.request.user.id
        customer = self.get_object()
        if customer.profile_id != user:
            raise PermissionDenied
        return handler
