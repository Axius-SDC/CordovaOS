"""
Django app configuration for civil_registry.
"""
from django.apps import AppConfig


class Civil_registryConfig(AppConfig):
    """App configuration for civil_registry."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'civil_registry'

    def ready(self):
        """
        Import signals when app is ready.

        This ensures that signal handlers are registered when Django starts.
        """
        import civil_registry.signals  # noqa: F401
