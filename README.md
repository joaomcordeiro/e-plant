# ePlant, is Raspberry Pi System that with an email notifier that warns you if your plant needs water.
# Most common reasons hoousehold plants die are related to constant high humidity levels.
# Light conditions in households arent as good as in a greenhouse, making photosynthesis harder and, conconsequently, harder for the roots to absorb all the water
# This inspires the growth of bacteria that leads to so called "root rot" and kills your plant by killing the roots.
# How to use ePlant? Easy!
# On moisture.py file "channel" represents the pin on thr Pi. Here, GPIO Pin 21 (Pin 40) was used as you can see in channel = 21 (line 6)
# On send.py file there more to it than in moisture.py.
# SMTPLib was the python library used for sending emails
# server = smtplib.SMTP('smtp-mail.outlook.com',587) ----> This is the info needed to set Outlook. If your not using Outlook, beware using Google might not be as straightforward. As of May 2022, Google no longer allows the use of GMail in less secure app.  
# sender = "INSERT EMAIL THAT WILL SENT IT"
# recipient = "INSERT EMAIL THAT WILL RECEIVE IT"
# bcc = "INSERT EMAIL THAT WILL RECEIVE IT" -----> not mandatory 
# sender_password = "INSERT SENDERS PASSWORD"
# And that's it! You're all set!
#
# BONUS
# You can also insert your own HTML body in order to fully costumize the email!
