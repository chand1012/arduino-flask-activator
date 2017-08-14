# Use this as a base for the email, just make it limit it to no subject
# https://gist.github.com/chand1012/5c6c0238defe017b1856a81ce6382d0f
from flask import Flask
import requests
import imaplib
import email
name = "Arduino Activator"
imap_ssl_host = 'imap.gmail.com'
imap_ssl_port = 993
user = ""
password = ""

app = Flask(name)

@app.route('/')
def hello_world():
    return "WIP!"
    #this will be used to house the standalone app webpage that will allow for
    #control from a chrome "app"
@app.route('/incoming')
def more():
