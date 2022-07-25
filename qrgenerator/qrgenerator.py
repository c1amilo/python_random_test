import pyqrcode
import png

#Link to convert to QR Code
link = "https://www.incoelectronica.com/"
qr_code = pyqrcode.create(link)
qr_code.png("qr.png", scale=5)