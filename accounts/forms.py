from django.contrib.auth.forms import UserCreationForm
from accounts.models import EmployeeUser


class EmployeeRegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = EmployeeUser
        fields = ['email', 'first_name', 'last_name']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data['email']
        if commit:
            user.save()
        return user