from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path('balances/', include('balances.urls')),
    path('leave-request/', include('leave_requests.urls')),
    path('reporting/', include('reporting.urls')),
    path('notifications/', include('notifications.urls')),

]
