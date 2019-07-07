from django.core.management import BaseCommand
from guests import qr_codes

# Usage
# python manage.py qr_codes /path/to/output/file/

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('filename', type=str, help='Path to output file')

        # Optional argument
        # parser.add_argument('-p', '--prefix', type=str, help='Define a username prefix', )

    def handle(self, *args, **kwargs):
        filename = kwargs['filename']
        print ("Generating QR Codes")
        qr_codes.create_qr_codes(filename)
