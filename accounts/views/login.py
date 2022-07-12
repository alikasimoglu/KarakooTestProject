from django.views.generic import TemplateView


class LoginView(TemplateView):
    template_name = "accounts/login.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
