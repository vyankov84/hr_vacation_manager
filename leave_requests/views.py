from django.shortcuts import render
import calendar
from datetime import date, timedelta

from leave_requests.choices import LeaveStatus
from leave_requests.models import LeaveRequest


def calendar_view(request):
    today = date.today()
    year = today.year

    approved_leaves = LeaveRequest.objects.filter(
        employee=request.user,
        status=LeaveStatus.APPROVED,
        start_date__year=year
    )

    vacation_days = set()
    for leave in approved_leaves:
        current_date = leave.start_date
        while current_date <= leave.end_date:
            if current_date.year == year:
                vacation_days.add(current_date)
            current_date += timedelta(days=1)

    cal = calendar.Calendar(firstweekday=0)
    yearly_calendar = []

    for month_num in range(1, 13):
        month_name = calendar.month_name[month_num]
        month_days = cal.monthdatescalendar(year, month_num)
        yearly_calendar.append({
            'name': month_name,
            'num': month_num,
            'weeks': month_days
        })

    context = {
        'year': year,
        'calendar': yearly_calendar,
        'vacation_days': vacation_days,
    }

    return render(request, 'leave_requests/calendar_page.html', context)
