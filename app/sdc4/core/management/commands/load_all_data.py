"""
Django management command to bulk-load all XML instances across all DM apps.

Iterates the DM registry, locates each app's import_data/ directory and
XSD schema, and runs BulkImportProcessor.process_directory() for each.
"""
import importlib
from pathlib import Path

from django.conf import settings
from django.core.management.base import BaseCommand

from sdc4_shared.utils.dm_registry import get_dm_registry


class Command(BaseCommand):
    help = 'Bulk-load all XML instances for every registered data model'

    def add_arguments(self, parser):
        parser.add_argument(
            '--app',
            type=str,
            help='Only load data for this specific app (e.g. civil_registry)',
        )

    def handle(self, *args, **options):
        registry = get_dm_registry()
        filter_app = options.get('app')

        total_imported = 0
        total_failed = 0
        total_skipped = 0

        for dm_ct_id, model_class in registry.items():
            app_label = model_class._meta.app_label

            if filter_app and app_label != filter_app:
                continue

            # Locate import_data directory
            import_dir = Path(settings.BASE_DIR) / 'import_data' / app_label
            if not import_dir.exists():
                self.stdout.write(
                    self.style.WARNING(f'  No import_data/ for {app_label}, skipping')
                )
                continue

            xml_count = len(list(import_dir.glob('*.xml')))
            if xml_count == 0:
                self.stdout.write(
                    self.style.WARNING(f'  No XML files in {import_dir}, skipping')
                )
                continue

            # Locate XSD schema
            dmlib_dir = Path(settings.MEDIA_ROOT) / 'dmlib'
            xsd_path = dmlib_dir / f'dm-{dm_ct_id}.xsd'
            if not xsd_path.exists():
                self.stdout.write(
                    self.style.ERROR(f'  XSD not found: {xsd_path}')
                )
                continue

            # Import FIELD_METADATA from the app's wizard_config
            try:
                wc = importlib.import_module(f'{app_label}.utils.wizard_config')
                field_metadata = wc.FIELD_METADATA
            except (ImportError, AttributeError) as e:
                self.stdout.write(
                    self.style.ERROR(f'  Cannot load FIELD_METADATA for {app_label}: {e}')
                )
                continue

            # Import the app's BulkImportProcessor
            try:
                bip_mod = importlib.import_module(f'{app_label}.utils.bulk_import')
                BulkImportProcessor = bip_mod.BulkImportProcessor
            except (ImportError, AttributeError) as e:
                self.stdout.write(
                    self.style.ERROR(f'  Cannot load BulkImportProcessor for {app_label}: {e}')
                )
                continue

            dm_label = getattr(model_class, 'DM_LABEL', app_label)

            self.stdout.write(
                self.style.MIGRATE_HEADING(
                    f'\n{app_label} ({xml_count} XML files)'
                )
            )

            processor = BulkImportProcessor(
                model_class=model_class,
                xsd_path=xsd_path,
                dm_ct_id=dm_ct_id,
                dm_label=dm_label,
                field_metadata=field_metadata,
            )
            result = processor.process_directory(import_dir)

            self.stdout.write(
                f'  Imported: {result.successful}  '
                f'Failed: {result.failed}  '
                f'Skipped: {result.skipped}'
            )
            total_imported += result.successful
            total_failed += result.failed
            total_skipped += result.skipped

        self.stdout.write(
            self.style.SUCCESS(
                f'\nDone. Imported: {total_imported}  '
                f'Failed: {total_failed}  '
                f'Skipped (duplicates): {total_skipped}'
            )
        )
