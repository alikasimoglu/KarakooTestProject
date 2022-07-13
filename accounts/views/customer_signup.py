from django.contrib.auth import login
from django.shortcuts import redirect
from django.views.generic import CreateView
from accounts.forms import CustomerSignUpForm
from accounts.models import User


class CustomerSignUpView(CreateView):
    model = User
    form_class = CustomerSignUpForm
    template_name = 'accounts/customer_signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'customer'
        return super().get_context_data(**kwargs)

    def get_initial(self):
        email_field = self.request.path
        initial = super(CustomerSignUpView, self).get_initial()
        initial['email'] = email_field[26:-1]
        return initial

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('mainsite:index')
