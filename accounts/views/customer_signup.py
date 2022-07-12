from django.contrib.auth import login
from django.shortcuts import redirect, get_object_or_404
from django.views.generic import CreateView
from accounts.forms import CustomerSignUpForm
from accounts.models import User, Employee
from mainsite.models import Company


class CustomerSignUpView(CreateView):
    model = User
    form_class = CustomerSignUpForm
    template_name = 'accounts/customer_signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'customer'
        return super().get_context_data(**kwargs)

    # def get_initial(self):
    #     company = get_object_or_404(Company)
    #     initial = super(CustomerSignUpView, self).get_initial()
    #     initial['company'] = Company.objects.get(employee__company=company.pk)
    #     return initial

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('mainsite:index')
