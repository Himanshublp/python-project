import smtplib as s

# Define the SMTP server and port
smtp_server = 'smtp.gmail.com'
smtp_port = 587

# Create an SMTP object
ob = s.SMTP(smtp_server, smtp_port)

# Greet the server
ob.ehlo()

# Start TLS for security
ob.starttls()

# Login to your email account
email = "shuklah849@gmail.com"
password = "himanshu@7800182966"  # Use an app-specific password or environment variable
ob.login(email, password)

# Email content
subject = "test python"
body = "I Love Python"
message = f"Subject: {subject}\n\n{body}"

# List of recipients
listadd = ["himanshublp2966@gmail.com", "shuklahim168@gmail.com"]

# Send the email
try:
    ob.sendmail(email, listadd, message)
    print("Email sent successfully!")
except Exception as e:
    print(f"Failed to send email: {e}")

# Terminate the SMTP session
ob.quit()
