import smtplib
import ssl
from email import encoders
from email.mime.multipart import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

sender_email = 'eldritchTest1@gmail.com'
password = 'P@ss1234'

context = ssl.create_default_context()

# 端口465好像是在gmail官方说明里查的，具体忘了
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)

    def send_mail(subject, mail_text, mail_address):

        message = MIMEMultipart("alternative")
        message["Subject"] = subject
        message["From"] = sender_email
        message["To"] = mail_address
        text = mail_text
        part1 = MIMEText(text, "plain")
        message.attach(part1)

        text = message.as_string()

        server.sendmail(
            sender_email, mail_address, message.as_string())

    mail_text = 'Hello World!'
    receiver = 'Zixi'
    mail_address = 'zixixu2017@gmail.com'
        
    subject = f"{receiver}, the Redfin data is updated"
    send_mail(subject, mail_text, mail_address)
    print(subject+"sended!!!!!!")