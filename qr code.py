import qrcode

text = input("enter a text or url: ")

qr =qrcode.QRCode(
    box_size=5,
    border=1
)

qr.add_data(text)
qr.make(fit=True)
print("this is your qrcode :)")
qr.print_ascii()