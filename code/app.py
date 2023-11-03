x = "a"
from rmqrcode import QRImage
from rmqrcode import rMQR
import rmqrcode
import time

print("Type what you want in the rmQrCode (Maxium characters allowed are 361)")
print("")

x = input()

qr = rMQR.fit(
    x,
    ecc=rmqrcode.ErrorCorrectionLevel.M,
)

image = QRImage(qr, module_size=8)
image.save("my_qr.png")
print("File saved as my_qr.png")
time.sleep(1.5)
image.show()
print("Press any key to close")
input()