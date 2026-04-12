from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='base.html'), name='home'),
    path('profiles/', include('accounts.urls')),
    path('balances/', include('balances.urls')),
    path('leave-request/', include('leave_requests.urls')),
    path('reporting/', include('reporting.urls')),
    path('notifications/', include('notifications.urls')),

]
