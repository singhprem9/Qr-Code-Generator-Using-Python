from turtle import back, fillcolor
import qrcode
from PIL import Image

qr = qrcode.QRCode(version=1,
                   error_correction=qrcode.constants.ERROR_CORRECT_H,
                   box_size=12, border=4,)

qr.add_data("https://github.com/singhprem9")

qr.make(fit=True)
img=qr.make_image(fill_color="blue", back_color="black")
img.save("github_link.png")
