"""
Django app configuration for tax_and_revenue_record.
"""
from django.apps import AppConfig


class Tax_and_revenue_recordConfig(AppConfig):
    """App configuration for tax_and_revenue_record."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tax_and_revenue_record'

    def ready(self):
        """
        Import signals when app is ready.

        This ensures that signal handlers are registered when Django starts.
        """
        import tax_and_revenue_record.signals  # noqa: F401
