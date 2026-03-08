"""
Django app configuration for law_enforcement_record.
"""
from django.apps import AppConfig


class Law_enforcement_recordConfig(AppConfig):
    """App configuration for law_enforcement_record."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'law_enforcement_record'

    def ready(self):
        """
        Import signals when app is ready.

        This ensures that signal handlers are registered when Django starts.
        """
        import law_enforcement_record.signals  # noqa: F401
