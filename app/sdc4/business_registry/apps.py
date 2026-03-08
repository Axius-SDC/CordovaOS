"""
Django app configuration for business_registry.
"""
from django.apps import AppConfig


class Business_registryConfig(AppConfig):
    """App configuration for business_registry."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'business_registry'

    def ready(self):
        """
        Import signals when app is ready.

        This ensures that signal handlers are registered when Django starts.
        """
        import business_registry.signals  # noqa: F401
