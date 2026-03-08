"""
Django app configuration for property_registry.
"""
from django.apps import AppConfig


class Property_registryConfig(AppConfig):
    """App configuration for property_registry."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'property_registry'

    def ready(self):
        """
        Import signals when app is ready.

        This ensures that signal handlers are registered when Django starts.
        """
        import property_registry.signals  # noqa: F401
