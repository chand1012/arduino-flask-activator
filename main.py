# Use this as a base for the email, just make it limit it to no subject
# https://gist.github.com/chand1012/5c6c0238defe017b1856a81ce6382d0f
from flask import Flask
from login_lib import *
# we will need this later
# import requests
import imaplib
import email
name = "Arduino Activator"
imap_ssl_host = 'imap.gmail.com'
imap_ssl_port = 993
last = 0
current = 0
logins = email_login_info()
user = logins['email']
password = logins['password']
def get_latest_email(username, epass):
    FROM_EMAIL  = username
    FROM_PWD    = epass
    SMTP_SERVER = "imap.gmail.com"
    SMTP_PORT   = 993

    mail = imaplib.IMAP4_SSL(SMTP_SERVER)
    mail.login(FROM_EMAIL,FROM_PWD)

    mail.select('inbox')
    etype, data = mail.search(None, 'ALL')
    mail_ids = data[0]
    id_list = mail_ids.split()
    first_email_id = int(id_list[0])
    latest_email_id = int(id_list[-1])
    typ, data = mail.fetch(str(latest_email_id), '(RFC822)' )

    for response_part in data:
        if isinstance(response_part, tuple):
            msg = email.message_from_string(response_part[1].decode('utf-8'))
            return [msg, first_email_id, latest_email_id]

app = Flask(name)

@app.route('/')
def hello_world():
    return "WIP!"
    #this will be used to house the standalone app webpage that will allow for
    #control from a chrome "app"
@app.route('/incoming', methods=['GET', 'POST'])
def more():
    latest_email = get_latest_email(user, password)
    thing = latest_email[0]
    current = latest_email[2]
    subject = thing['subject']
    if 'Coffee' in subject and last != current:
        print("Making coffee!")
        last = current
    else:
        print("Not making coffee!")
