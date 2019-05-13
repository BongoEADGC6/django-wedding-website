import qrcode
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO
from guests.models import Party, Guest
from django.conf import settings
from django.urls import reverse

def gen_qr_code(url):
    qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=6,
            border=4,
            )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    return img

def create_qr_codes(output_dir):
    to_send_to = Party.in_default_order().filter(is_invited=True, invitation_sent=None).exclude(is_attending=False)
    table_data = str()
    for party in to_send_to:
        print("Creating QR for: {} - {}".format(party.name, party.invitation_id))
        rsvp_url = reverse('invitation', args=[party.invitation_id])
        rsvp_url = "https://{}{}".format(settings.BASE_URL, rsvp_url)
        print("URL: {}".format(rsvp_url))
        qr_img = gen_qr_code(rsvp_url)
        qr_img_path = "{}/img/{}.png".format(output_dir, party.invitation_id)
        qr_img_static ="img/{}.png".format(party.invitation_id)
        qr_img.save(qr_img_path)
        body_text = """
            If you have a smartphone or tablet please scan the code using your<br>
            camera app (use Lens from the Google Assistant for Samsung devices)<br>
            or navigate to the following link to submit your RSVP<br>
            {} <br>
            <br>
            If there are any issues or questions, please feel free to contact us directly at<br>
            Phone: 732-245-9653 <br>
            Email: mrmrshults@gmail.com <br>
            Thank you! <br>
            Cliff & Melissa
            """.format(rsvp_url)
        table_entry = """
            <div>
            <table class="tg">
              <tr>
                <td class="tg-0lax" colspan="2">************************</td>
              </tr>
              <tr>
                <td class="tg-0lax" colspan="2">{}</td>
              </tr>
              <tr>
                <td class="tg-0lax"><img src="{}"></td>
                <td class="tg-0lax">{}</td>
              </tr>
            </table>
            </div>
            """.format(party.name, qr_img_static, body_text)
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
        """.format(table_data)
    with open("{}/qr.html".format(output_dir), "w") as f:
            f.write(html_text)

