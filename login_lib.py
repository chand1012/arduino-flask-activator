from json import loads
import imaplib
import email
def email_login_info(file_name='login.json'):
    try:
        file_keys = open(file_name)
    except:
        file_keys = open(file_name, 'w')
        raw_json = '''
        {
            "email":"",
            "password:""
        }
         '''
        print("Error! JSON file does not exist!")

    parsed_json = loads(file_keys.read())

    return parsed_json

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

#add unseen function
