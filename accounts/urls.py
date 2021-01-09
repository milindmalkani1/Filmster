from django.urls import path, include, reverse_lazy, re_path
from . import views
from django.contrib.auth import views as auth_views

app_name = "accounts"

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', auth_views.LoginView.as_view(
        template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(
        template_name='accounts/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('change-password/', auth_views.PasswordChangeView.as_view(
        template_name='accounts/change_password.html',
        success_url=reverse_lazy('accounts:change_password_done')), name='change_password'),
    path('change-password/done/', auth_views.PasswordChangeDoneView.as_view(
        template_name='accounts/password_change_done.html'),
        name='change_password_done'),

    path('reset-password/', auth_views.PasswordResetView.as_view(
        template_name='accounts/reset_password.html',
        email_template_name='accounts/reset_password_email.html',
        success_url=reverse_lazy('accounts:password_reset_done')),
        name='reset_password'),

    path('reset-password/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='accounts/reset_password_done.html'),
        name='password_reset_done'),

    path('reset-password/confirm/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(
        success_url=reverse_lazy('accounts:password_reset_complete'),
        template_name='accounts/reset_password_confirm.html'),
        name='password_reset_confirm'),

    path('reset-password/complete/',
        auth_views.PasswordResetCompleteView.as_view(
        template_name='accounts/reset_password_complete.html'),
        name='password_reset_complete'),
]
