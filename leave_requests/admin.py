from django.contrib import admin
from leave_requests.models import LeaveRequest


@admin.register(LeaveRequest)
class LeaveRequestAdmin(admin.ModelAdmin):

    list_display = ['employee', 'leave_type', 'duration_off', 'start_date', 'end_date', 'created_at']

    list_filter = ['leave_type', 'start_date']


