from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from accounts.models import EmployeeUser


@admin.register(EmployeeUser)
class EmployeeUserAdmin(UserAdmin):

    list_display = [
        'username',
        'email',
        'first_name',
        'last_name',
        'department',
        'is_team_leader',
        'is_staff',
    ]

    list_filter = ('department', 'is_team_leader', 'is_staff')

    fieldsets = UserAdmin.fieldsets + (
        ('HR Information', {
            'fields': ('department', 'is_team_leader'),
        }),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ('HR Information', {
            'fields': ('department', 'is_team_leader'),
        }),
    )

