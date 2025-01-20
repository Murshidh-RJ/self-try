import qrcode

data=input("Enter the text url : ").strip()
filename=input("Enter the filename : ").strip()
qr=qrcode.QRCode(border=4,box_size=10)
qr.add_data(data)
image =qr.make_image(fill_color="black", back_color='white')
image.save(filename)
print(f"QR code saved as {filename}")