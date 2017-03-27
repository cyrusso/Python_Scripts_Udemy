#!/usr/bin/python

import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

toaddr = 'dastangoo@airport.ir'
fromaddr = 'hamed.dastangoo@gmail.com'
text = 'test message sent from python'
username = 'hamed.dastangoo'
password = 'Dr@g0ng1a$s'
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = 'Test'
msg.attach(MIMEText(text))
server = smtplib.SMTP('smtp.gmail.com:587')
server.ehlo()
server.starttls()
server.ehlo()
server.login(username,password)
server.sendmail(fromaddr, toaddr, msg.as_string())
server.quit()

