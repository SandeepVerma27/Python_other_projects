# -------simple------------
import qrcode as qr
img=qr.make("https://www.instagram.com/")
img.save("instagram.png")
