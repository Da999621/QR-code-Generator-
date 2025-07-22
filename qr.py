import qrcode

# taking UPI ID as input
upi_id = input("Enter UPI ID:")

# upi://pay?_ID&apn=NAME&am=Amount&cu=CURRENCY&tn=MESSAGE
#defining the payment url based on the upiu id and the payment app
# you can modify these urls based on the payment apps you want to support

phonepe_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
paytm_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
google_pay_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'

# create qr codes for each payment app
phonepe_qr = qrcode.make(phonepe_url)
paytm_qr = qrcode.make(paytm_url)
google_pay_qr = qrcode.make(google_pay_url)

# save the qr code to image file(optional)
phonepe_qr.save('phonepe_qr.png')
paytm_qr.save('paytm_qr.png')
google_pay_qr.save('google_pay_qr.png')

# display the qr code (you may need to install pil/pillow library)
phonepe_qr.show()
paytm_qr.show()
google_pay_qr.show()

