# email-cli
Allows simple text to be emailed

## Usage
You can change this to your email provider like:
smtp.gmail.com -> smtp.mail.yahoo.com
```python
with smtplib.SMTP_SSL("smtp.mail.yahoo.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())
```
