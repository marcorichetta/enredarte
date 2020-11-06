from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    def __str__(self):
        return self.username

    def get_email(self):
        return self.email
