from django.urls import path
from accounts import views

app_name = 'accounts'

urlpatterns = [
    path('', views.EmployeeDetailView.as_view(), name='details'),
    path('register/', views.EmployeeRegister.as_view(), name='register'),
    path('login/', views.EmployeeLogin.as_view(), name='login'),
    path('logout/', views.EmployeeLogout.as_view(), name='logout'),

]