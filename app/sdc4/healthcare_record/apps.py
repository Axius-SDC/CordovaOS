"""
Django app configuration for healthcare_record.
"""
from django.apps import AppConfig


class Healthcare_recordConfig(AppConfig):
    """App configuration for healthcare_record."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'healthcare_record'

    def ready(self):
        """
        Import signals when app is ready.

        This ensures that signal handlers are registered when Django starts.
        """
        import healthcare_record.signals  # noqa: F401
