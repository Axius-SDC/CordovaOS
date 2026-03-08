"""
Django app configuration for vital_statistics_record.
"""
from django.apps import AppConfig


class Vital_statistics_recordConfig(AppConfig):
    """App configuration for vital_statistics_record."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'vital_statistics_record'

    def ready(self):
        """
        Import signals when app is ready.

        This ensures that signal handlers are registered when Django starts.
        """
        import vital_statistics_record.signals  # noqa: F401
