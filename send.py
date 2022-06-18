import sendgrid
import os
from sendgrid.helpers.mail import *

sg = sendgrid.SendGridAPIClient('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')
from_email = Email("ispg4103@ispgaya.pt")
to_email = To("joaomcordeiro98@gmail.com")
subject = "Sending with SendGrid is Fun"
content = Content("text/plain", "and easy to do anywhere, even with Python")
mail = Mail(from_email, to_email, subject, content)
response = sg.client.mail.send.post(request_body=mail.get())

print(response.status_code)
print(response.body)
print(response.headers)
