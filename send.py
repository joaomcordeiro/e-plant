from email.mime.text import MIMEText

from email.mime.multipart import MIMEMultipart

import smtplib

import ssl

server = smtplib.SMTP('smtp-mail.outlook.com',587)

server.starttls()

sender = "eplantnotifier@outlook.com"
recipient = "ispg4103@ispgaya.pt"
bcc = "joaomcordeiro98@gmail.com"
sender_password = "INSERT PASSWORD"
msg = MIMEMultipart()
html_message = """
html_message = """
<html>
<bodystyle="background-color:#77b300;">
<p style="font-family:verdana">Hi, it looks like your plant needs some water!</p>
</body>
</html>

"""body>

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

server.sendmail(sender, recipient, text)

print('Mail sent')
