import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

message = Mail(
    from_email='ispg4103@ispgaya.pt',
    to_emails='joaomcordeiro98@gmail.com',
    subject='Hello Friend, Looks Like Your Plant Needs Some Water')
try:
    sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e.message)
