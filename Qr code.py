#1. pip install pyqrcode
#2. pip install pypng (to save image in png format:)

# import qrcode 
import qrcode as qr

# making qr code by using make function  
img = qr.make("https://github.com/singhprem9")

# save 
img.save("github_page.png")


