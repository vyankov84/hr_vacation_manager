from django.contrib.auth.models import AbstractUser
from django.db import models

from accounts.choices import DepartmentType


class EmployeeUser(AbstractUser):

    first_name = models.CharField(
        max_length=100,
        blank=True,
    )

    last_name = models.CharField(
        max_length=100,
        blank=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    department = models.CharField(
        max_length=15,
        choices=DepartmentType.choices,
        default=DepartmentType.OTHER,
    )

    email = models.EmailField(
        unique=True,
        error_messages={"unique":"This email is already taken!"}
    )

    is_team_leader = models.BooleanField(
        default=False,
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']


    def __str__(self):
        full_name = f"{self.first_name} {self.last_name}".strip()
        return full_name if full_name else self.username
