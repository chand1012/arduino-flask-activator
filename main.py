# Use this as a base for the email, just make it limit it to no subject
# https://gist.github.com/chand1012/5c6c0238defe017b1856a81ce6382d0f
from flask import Flask
from login_lib import *
# we will need this later
# import requests
imap_ssl_host = 'imap.gmail.com'
imap_ssl_port = 993
logins = email_login_info()
user = logins['email']
password = logins['password']

app = Flask(__name__)
current = 0
last = 0

@app.route('/')
def hello_world():
    return "WIP!"
    #this will be used to house the standalone app webpage that will allow for
    #control from a chrome "app"

@app.route('/incoming', methods=['GET', 'POST'])
def more(): # needs fixed to eliminate duplicates
    global last
    global current
    latest_email = get_latest_email(user, password)
    thing = latest_email[0]
    current = latest_email[2]
    subject = thing['subject']
    if 'Coffee' in subject and last != current:
        print("Making coffee!")
        return "Making Coffee"
        last = current
    else:
        print("Not making coffee!")
        return "Not making coffee"
