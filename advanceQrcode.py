import qrcode

# Create an instance of QRCode
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=20,
    border=4,
)

# Add data to the QR code
qr.add_data("https://github.com/Himanshublp")
qr.make(fit=True)

# Create the image with the specified colors
img = qr.make_image(fill_color="red", back_color="white")
img.save("GitHubRepository.png")
