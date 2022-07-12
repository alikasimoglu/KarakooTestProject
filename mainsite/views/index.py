from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView


@method_decorator([login_required(login_url=reverse_lazy("accounts:login"))], name='dispatch')
class IndexView(TemplateView):
    template_name = "mainsite/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
