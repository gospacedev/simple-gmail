import smtplib
import ssl
from email.message import EmailMessage

sender_email = input("Enter sender's gmail: ")
password = input("Enter sender's password: ")
receiver_email = input("Enter recevier's gmail: ")
subject = input("Enter email subject: ")
body = input("Enter email body: ")

message = EmailMessage()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
message.set_content(body)

context = ssl.create_default_context()

print("Sending Email!")

#You can change this to your email provider
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())

print("Success")
