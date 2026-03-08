"""
Django app configuration for employment_record.
"""
from django.apps import AppConfig


class Employment_recordConfig(AppConfig):
    """App configuration for employment_record."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'employment_record'

    def ready(self):
        """
        Import signals when app is ready.

        This ensures that signal handlers are registered when Django starts.
        """
        import employment_record.signals  # noqa: F401
