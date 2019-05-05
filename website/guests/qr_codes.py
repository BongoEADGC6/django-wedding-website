import qrcode
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO
import uuid
from guests.models import Party, Guest


def qr_codes(path):
    qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
            )
    qr.add_data('Some data')
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
