from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('profiles/', include('accounts.urls')),
    path('balances/', include('balances.urls')),
    path('leave-request/', include('leave_requests.urls')),
    path('reporting/', include('reporting.urls')),
    path('notifications/', include('notifications.urls')),

]
