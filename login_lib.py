from json import loads
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
