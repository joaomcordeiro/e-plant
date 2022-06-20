import RPi.GPIO as GPIO
import time


#GPIO SETUP
channel = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

def callback(channel):
        if GPIO.input(channel):
                print("Water Detected!")
        else:

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
<head>
<style>
table {
  border-collapse: collapse;
  width: 100%;
}
th {
  text-align: center;
  padding: 8px;
  font-family: 'Ascender Sans', sans-serif;
}

tr{
  background-color: #77b300;
}

tr1{
  background-color: white;
}

tr2{
  background-color: black;
}

</style>
</head>
<body>
<table>
  <tr1>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  </tr1>
  <tr>
    <tr>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  </tr>
  <tr>
    <tr>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  </tr>
    <tr>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  </tr>
    <th></th>
  <th>Looks Like Your Plant needs some Water</th>
  <th></th>
  <th></th>
  </tr>
    <th></th>
  <th></th>
  <th></th>
  <th></th>
  </tr>
    <th></th>
  <th></th>
  <th></th>
  <th></th>
  </tr>
      <th></th>
  <th></th>
  <th></th>
  <th></th>
  </tr>
      <th></th>
  <th></th>
  <th></th>
  <th></th>
  </tr>
      <th></th>
  <th></th>
  <th></th>
  <th></th>
  </tr>
      <th></th>
  <th></th>
  <th></th>
  <th></th>
  </tr>
      <th></th>
  <th></th>
  <th></th>
  <th></th>
  </tr>
      <th></th>
  <th></th>
  <th></th>
  <th></th>
  </tr>
      <th></th>
  <th></th>
  <th></th>
  <th></th>
  </tr>
      <th></th>
  <th></th>
  <th></th>
  <th></th>
  </tr>
      <th></th>
  <th></th>
  <th></th>
  <th></th>
  </tr>
      <th></th>
  <th></th>
  <th></th>
  <th></th>
  </tr>      <th></th>
  <th></th>
  <th></th>
  <th></th>
  </tr>
        <th></th>
  <th></th>
  <th></th>
  <th></th>
  </tr>
        <th></th>
  <th></th>
  <th></th>
  <th></th>
  </tr>
        <th></th>
  <th></th>
  <th></th>
  <th></th>
  </tr>
        <th></th>
  <th></th>
  <th></th>
  <th></th>
  </tr>

  <th></th>
  <th></th>
  <th></th>
  <th></th>
  </tr>

  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  </tr>
</table>

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

server.sendmail(sender, recipient, text)

print('Mail sent')
               

GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)  # let us know when the pin goes HIGH or LOW
GPIO.add_event_callback(channel, callback)  # assign function to GPIO PIN, Run function on change

# infinite loop
while True:
        time.sleep(1)
