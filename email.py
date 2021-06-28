#before starting make sure you have enabled access for unsecured apps in your google settings for the sender mail.
import smtplib, ssl

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "sendermail@gmail.com"  # Enter your address
receiver_email = "recivermail@gmail.com"  # Enter receiver address
password = '#######'# do not store password directly
message = """\
Subject: Hi there

This message is sent from Python."""

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
