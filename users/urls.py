from django.urls import path
from django.contrib.auth import views as auth_views

from .views import register

urlpatterns = [
    path("register/", register, name="register"),
    # If user is logged in, redirect to 'login' url
    path(
        "login/",
        auth_views.LoginView.as_view(
            template_name="users/login.html", redirect_authenticated_user=True
        ),
        name="login",
    ),
    path(
        "logout/",
        auth_views.LogoutView.as_view(template_name="users/logout.html"),
        name="logout",
    ),
]
