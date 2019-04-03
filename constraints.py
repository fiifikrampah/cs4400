# This file checks user registration entries on the front end. 

import re

'''
Globals:
'''
email_requirement = "(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
username_requirement = "(^[a-zA-Z0-9_.-]{3,50}$)"
password_requirement = "(^[a-zA-Z0-9_.-]{8,50}$)"


# check email format
#
# returns
#     1 - email matches format
#     0 - email doesn't match format
def constraint_email_format(email):
    email_regex = re.compile(email_requirement)
    if email_regex.match(email) is None:
        return 0
    else:
        return 1

# check username format
#
# returns
#     1 - username matches format
#     0 - usernmae doesn't match format
def constraint_username_format(username):
    username_regex = re.compile(username_requirement)
    if username_regex.match(username) is None:
        return 0
    else:
        return 1

# check password format
#
# returns
#     1 - password matches format
#     0 - password doesn't match format
def constraint_password_format(password):
    password_regex = re.compile(password_requirement)
    if password_regex.match(password) is None:
        return 0
    else:
        return 1
