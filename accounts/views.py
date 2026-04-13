from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView

from accounts.forms import EmployeeRegisterForm
from accounts.models import EmployeeUser


class EmployeeRegister(CreateView):
    form_class = EmployeeRegisterForm
    template_name = 'accounts/employee-register.html'
    success_url = reverse_lazy('accounts:login')


class EmployeeLogin(LoginView):
    template_name = 'accounts/login.html'


class EmployeeLogout(LogoutView):
    next_page = reverse_lazy('accounts:login')


class EmployeeDetailView(LoginRequiredMixin, DetailView):
    model = EmployeeUser
    context_object_name = 'employee'
    template_name = 'accounts/employee-details.html'

    def get_object(self, queryset = None):
        return self.request.user