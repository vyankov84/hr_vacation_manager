from django.conf import settings
from django.db import models

from accounts.models import EmployeeUser

class LeaveBalance(models.Model):

    employee = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name= 'balances'
    )

    annual_leave_allowed = models.PositiveIntegerField(default=20)
    annual_leave_remaining = models.PositiveIntegerField(default=20)

    year = models.PositiveIntegerField(default=2026)

    def __str__(self):
        return f"Balance for {self.employee.first_name} ({self.year})"

