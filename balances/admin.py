from django.contrib import admin

from balances.models import LeaveBalance


@admin.register(LeaveBalance)
class LeaveBalanceAdmin(admin.ModelAdmin):

    list_display = ['employee','annual_leave_allowed','annual_leave_remaining', 'year']

    search_fields = ['employee__email']
