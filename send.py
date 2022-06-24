from email.mime.text import MIMEText

from email.mime.multipart import MIMEMultipart

import smtplib

import ssl

server = smtplib.SMTP('smtp-mail.outlook.com',587)

server.starttls()

sender = "eplantnotifier@outlook.com"
recipient = "ispg4103@ispgaya.pt"
bcc = "joaomcordeiro98@gmail.com"
sender_password = "INSERt PASSWORD"
msg = MIMEMultipart()
html_message = """
<html>
<head>
<style>
table {
 	 border-collapse: collapse;
    padding-left: 10px;
    width:100%;
    font-family: 'Ascender Sans', sans-serif;
    font-color: white;
    font-size:11px;
    text-align:center;
    background-color:#77b300;
}

th, td {
    padding:5px 10px;
}

th {
    color:#77b300;
    border-top:15px solid DarkOliveGreen;
    border-bottom:25px solid black;
    background-color:#77b300;
}
</style>
</head>
<body>
<table>
  <tr>
  <th></th>
  <th>Hi, it's time to water your plant!</th>
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
