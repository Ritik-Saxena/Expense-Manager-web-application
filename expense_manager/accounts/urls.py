from django.urls import re_path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # user register, login, logout
    re_path(r'user/register', views.userRegister, name='user_register'),
    re_path(r'user/login', views.userLogin, name='user_login'),
    re_path(r'user/logout', views.userLogout, name='user_logout'),

    
    # forgot password
    re_path(r'^reset-password/$', 
        auth_views.PasswordResetView.as_view(template_name="accounts/reset_password.html"), 
        name='password_reset'),
    
    re_path(r'^reset-password/sent/$', 
        auth_views.PasswordResetDoneView.as_view(template_name="accounts/reset_password_sent.html"), 
        name='password_reset_done'),
    
    re_path(r'reset-password/(?P<uidb64>[A-Za-z0-9]+)/(?P<token>.+)/$', 
        auth_views.PasswordResetConfirmView.as_view(template_name="accounts/reset_password_confirm.html"), 
        name='password_reset_confirm'),

    re_path(r'^reset-password/complete/$', 
        auth_views.PasswordResetCompleteView.as_view(template_name="accounts/reset_password_complete.html"), 
        name='password_reset_complete'),



]
