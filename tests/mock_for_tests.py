

class UserData:
    valid_data = {
        'username': 'John',
        'password': 'ffff3333!',
        'confirm_password': 'ffff3333!',
    }

    invalid_passwords_length = {
        'username': 'John',
        'password': 'ffff3333!ffffff',
        'confirm_password': 'ffff3333!ffffff',
    }

    invalid_username = {
        'username': 'test3',
        'password': 'ffff3333!',
        'confirm_password': 'ffff3333!',
    }

    no_passwords_match = {
        'username': 'John',
        'password': 'ffff3333!',
        'confirm_password': 'test',
    }

    blank_passwords = {
        'username': 'John',
    }

    blank_username = {
        'password': 'ffff3333!',
        'confirm_password': 'ffff3333!',
    }

    nonexistent_user = {
        'username': 'Jackson',
        'password': 'ffff3333!',
    }


