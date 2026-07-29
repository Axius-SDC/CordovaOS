"""
Django app configuration for maritime_port_authority.
"""
from django.apps import AppConfig


class Maritime_port_authorityConfig(AppConfig):
    """App configuration for maritime_port_authority."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'maritime_port_authority'

    def ready(self):
        """
        Import signals when app is ready.

        This ensures that signal handlers are registered when Django starts.
        """
        import maritime_port_authority.signals  # noqa: F401
