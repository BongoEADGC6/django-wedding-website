from django.core.management import BaseCommand
from guests import csv_import

# Usage
# python manage.py import_guests /path/to/file/

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('filename', type=str, help='Path to file')

        # Optional argument
        # parser.add_argument('-p', '--prefix', type=str, help='Define a username prefix', )

    def handle(self, *args, **kwargs):
        filename = kwargs['filename']
        csv_import.import_guests(filename)
