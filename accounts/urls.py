from django.urls import path
from django.contrib.auth import views as auth_views
from accounts.views import EmployeeSignUpView, EmployeeProfileView, EmployeeProfileUpdateView, CustomerSignUpView

app_name = 'accounts'
urlpatterns = [
    # Sign-up, Log-in and Logout
    path('signup/employee/', EmployeeSignUpView.as_view(), name='employee_signup'),
    path('signup/customer/', CustomerSignUpView.as_view(), name='customer_signup'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # Mainsite urls
    path('employee/profile/<int:pk>/', EmployeeProfileView.as_view(), name='employee_profile_detail'),
    path('employee/profile-update/<int:pk>/', EmployeeProfileUpdateView.as_view(), name='employee_profile_update'),
]
