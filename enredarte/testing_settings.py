# Testing settings - Reference: https://www.mattlayman.com/blog/2020/django-testing-toolbox/
# ------------------------------------------------------------------------------

from .settings import *  # noqa

# An in-memory database should be good enough for now.
DATABASES = {"default": {"ENGINE": "django.db.backends.sqlite3", "NAME": ":memory:"}}


class DisableMigrations(object):
    def __contains__(self, item):
        return True

    def __getitem__(self, item):
        return None


MIGRATION_MODULES = DisableMigrations()
