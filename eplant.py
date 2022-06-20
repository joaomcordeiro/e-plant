from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import ssl
import RPi.GPIO as GPIO
import time

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import ssl
server = smtplib.SMTP('smtp-mail.outlook.com',587)
server.starttls()
sender = "eplantnotifier@outlook.com"
recipient = "ispg4103@ispgaya.pt"
bcc = "joaomcordeiro98@gmail.com"
sender_password = "ispg12345"
msg = MIMEMultipart()
html_message = """
<html>
<body>
<p style="font-family:verdana">A PUTA DA PLANTA PRECISA DE AGUA</p>
<p style="font-family:'Courier New'">A PUTA DA PLANTA PRECISA DE AGUA</p>
</body>
</html>
"""

msg.attach(MIMEText(html_message, "html"))

msg['From']= sender

msg['To']= recipient

msg['Subject']= "Automatic ePlant Notifier"

msg["Bcc"] = bcc

msg["Cc"] = recipient

text = msg.as_string()

server.login(sender ,sender_password)
#GPIO SETUP
channel = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

def callback(channel):
        if GPIO.input(channel):

server.sendmail(sender, recipient, text)

print('Mail sent')
        else:
                print("Water Detected!")

GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)  # let us know when the pin goes HIGH or LOW
GPIO.add_event_callback(channel, callback)  # assign function to GPIO PIN, Run function on change

# infinite loop
while True:
        time.sleep(1)
