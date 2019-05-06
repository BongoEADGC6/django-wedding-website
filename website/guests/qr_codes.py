import qrcode
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO
from guests.models import Party, Guest
from django.urls import reverse

def gen_qr_code(url):
    qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
            )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    return img

def create_qr_codes(output_file):
    to_send_to = Party.in_default_order().filter(is_invited=True, invitation_sent=None).exclude(is_attending=False)
    table_data = str()
    for party in to_send_to:
        print(party.invitation_id)
        rsvp_url = reverse('invitation', args=party.invitation_id)
        print(rsvp_url)
        qr_img = gen_qr_code(rsvp_url)
        body_text = """
            Please scan the code above with your smart phone or<br/>
            navigate to the following link to submit your RSVP<br/>
            {}
            """.format(rsvp_url)
        table_entry = """
              <tr>
                <td class="tg-0lax">{}</td>
                <td class="tg-0lax">{}</td>
              </tr>
            """.format(qr_img, body_text)
        table_data += "{}\n".format(table_entry)
    # Build full html page for printing
    table_text = """
        <table class="tg">
          {}
        </table>
        """.format(table_data)
    html_text = """
        <html>
        <head></head>
        <body>
          {}
        </body>
        </html>
        """.format(table_text)
    with read(output_file, "wr") as f:
            f.write(html_text)

