#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from dotenv import load_dotenv

def main():
    """Run administrative tasks."""
    load_dotenv()  # Load environment variables from .env file

    DJANGO_ENV = os.getenv('DJANGO_ENV', 'local')

    if DJANGO_ENV == 'production':
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "speech_processing_backend.settings.production")
    elif DJANGO_ENV == 'staging':
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "speech_processing_backend.settings.staging")
    else:
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "speech_processing_backend.settings.local")

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
