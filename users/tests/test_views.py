from django.test import TestCase
from users.models import CustomUser
from django.urls import reverse
import pytest


@pytest.mark.django_db
def test_login_and_logout(client):
    """Tests logging in and logging out"""
    # Create a fake user
    user = CustomUser.objects.create_user("test", "test@user.com", "test_password")
    user.save()

    login_url = reverse("login")
    resp = client.post(login_url, {"username": "test", "password": "test_password"})

    # The login url should redirect to the home page
    assert resp.status_code == 302
    assert resp.url == reverse("core:home")

    # Log out the user
    logout_url = reverse("logout")
    resp = client.get(logout_url)

    # Similar to the login view, the logout view redirects to the login page
    assert resp.status_code == 302
    assert resp.url == reverse("login")
