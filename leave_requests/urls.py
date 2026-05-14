from django.urls import path
from leave_requests import views

app_name = 'leave_requests'

urlpatterns = [
    path('calendar/', views.calendar_view, name='calendar_view')
]