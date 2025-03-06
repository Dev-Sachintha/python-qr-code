import qrcode
import qrcode.constants

qr = qrcode.QRCode(version=1,
                   error_correction=qrcode.constants.ERROR_CORRECT_L,
                   box_size=20,
                   border=2)

qr.add_data("http://verbo-web-application.vercel.app")
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save("myqr.png")
