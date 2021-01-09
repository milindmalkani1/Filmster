from django.contrib import admin
from django.urls import path, include
from filmster import views

urlpatterns = [
    path('', views.login_redirect, name="login_redirect"),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('portfolio/', include('portfolio.urls', namespace='portfolio')),
]
