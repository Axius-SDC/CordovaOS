"""
Django app configuration for education_record.
"""
from django.apps import AppConfig


class Education_recordConfig(AppConfig):
    """App configuration for education_record."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'education_record'

    def ready(self):
        """
        Import signals when app is ready.

        This ensures that signal handlers are registered when Django starts.
        """
        import education_record.signals  # noqa: F401
