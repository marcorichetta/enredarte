#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

# TODO: #6 Crear config con docker + testing
def main():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "enredarte.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    """
    Django runs twice to support live-reloading! In order to support live-reloading files and
    attaching to the correct process, we use a bit of Django's internals to check if we need to
    start up our debugger.

    See:
    - https://github.com/django/django/blob/master/django/utils/autoreload.py#L26
    - https://ytec.nl/blog/debugging-django-vscode-without-using-noreload/
    """
    if (
        os.environ.get("RUN_MAIN") or os.environ.get("WERKZEUG_RUN_MAIN")
    ) and os.environ.get("VSCODE_DEBUGGER", True):

        import ptvsd  # noqa

        ptvsd_port = 4000

        try:
            ptvsd.enable_attach(address=("0.0.0.0", ptvsd_port))
            print("Started ptvsd at port %s." % ptvsd_port)
        except OSError:
            print("ptvsd port %s already in use." % ptvsd_port)

    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
