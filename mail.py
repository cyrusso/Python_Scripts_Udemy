#!/usr/bin/python

import smtplib, imaplib, os
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

def read():
    os.system('clear')
    mailserver = imaplib.IMAP4_SSL('imap.gmail.com',993)
    username = 'hamed.dastangoo'
    password = 'Dr@g0ng1a$s'
    mailserver.login(username,password)
    status, count = mailserver.select('Inbox')
    status, data = mailserver.fetch(count[0], '(UID BODY[TEXT])')
    print data[0][1]
    mailserver.close()
    mailserver.logout()
    choice = raw_input("Press x to clear screen: ")
    if choice == "x":
        os.system("clear")

def send():
    fromaddr = raw_input("Enter your email address: ")
    toaddr = raw_input("Enter the receiver's email address: ")
    text = raw_input("Enter the message: ")
    subject = raw_input("Enter the Subject: ")
    username = raw_input("Enter your username: ")
    password = raw_input("Enter your password: ")
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = subject
    msg.attach(MIMEText(text))
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(username,password)
    server.sendmail(fromaddr, toaddr, msg.as_string())
    server.quit()
    choice = raw_input("Email sent. Press x to clear the screen: ")
    if choice == "x":
        os.system("clear")

while 1:
    os.system("clear")
    print("Email Program")
    print("")
    print("1. Read email")
    print("2. Send email")
    print("3. Exit")
    print("")
    choice = raw_input("Enter a choice: ")
    if choice == "1":
        read()
    elif choice == "2":
        send()
    elif choice == "3":
        break;
