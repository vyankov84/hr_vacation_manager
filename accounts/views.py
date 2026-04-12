from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView

from accounts.forms import EmployeeRegisterForm


class EmployeeRegister(CreateView):
    form_class = EmployeeRegisterForm
    template_name = 'accounts/employee-register.html'
    success_url = reverse_lazy('accounts:login')


class EmployeeLogin(LoginView):
    template_name = 'accounts/login.html'


class EmployeeLogout(LogoutView):
    next_page = reverse_lazy('accounts:login')