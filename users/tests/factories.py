import factory


class CustomUserFactory(factory.DjangoModelFactory):
    class Meta:
        model = "users.CustomUser"
