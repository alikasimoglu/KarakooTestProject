from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView
from accounts.models import Employee
from accounts.permissions import user_is_employee
from mainsite.forms import CompanyCreateForm
from mainsite.models import Company


@method_decorator([login_required(login_url=reverse_lazy("accounts:login")), user_is_employee], name='dispatch')
class CompanyCreateView(CreateView):
    model = Company
    form_class = CompanyCreateForm
    template_name = 'mainsite/company_create_form.html'

    def get_initial(self):
        user = self.request.user
        initial = super(CompanyCreateView, self).get_initial()
        initial['employee'] = Employee.objects.get(profile=user)
        return initial


@method_decorator([login_required(login_url=reverse_lazy("accounts:login")), user_is_employee], name='dispatch')
class CompanyDetailView(DetailView):
    model = Company
    context_object_name = "company"
    template_name = 'mainsite/company_details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


@method_decorator([login_required(login_url=reverse_lazy("accounts:login")), user_is_employee], name='dispatch')
class CompanyUpdateView(UpdateView):
    model = Company
    context_object_name = "company"
    template_name = 'mainsite/company_update.html'
    fields = ('company_name', 'company_email', 'company_phone', 'additional_info', 'is_accepted', 'is_email_sent', 'is_registred')

    def form_valid(self, form):
        messages.success(self.request, 'Copmany information has been successfully updated!')
        return super().form_valid(form)


@method_decorator([login_required(login_url=reverse_lazy("accounts:login")), user_is_employee], name='dispatch')
class CompanyDeleteView(DeleteView):
    model = Company
    template_name = 'mainsite/company_delete.html'
    success_url = reverse_lazy('mainsite:company_list')

    def form_valid(self, form):
        messages.success(self.request, 'Copmany has been successfully deleted!')
        return super().form_valid(form)


@method_decorator([login_required(login_url=reverse_lazy("accounts:login")), user_is_employee], name='dispatch')
class CompanyListView(ListView):
    model = Company
    context_object_name = "companies"
    template_name = 'mainsite/company_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
