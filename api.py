# This file serves as the controller for the backend. Contains stored procedures

from database import *
from constraints import *
import hashlib
import random

# Register user function; inserts tuples into the user table

def validate_user_registration(username, password, status, fname, lname, UserType):
	set_connection()
	 # execute the query
	# isDeclined_result = db_isDeclined(username)
	# if isDeclined_result == 1:
		
    hashed_password = hashlib.md5(password).hexdigest()
    user_insert_result = user_insert(username, hashed_password,status, fname, lname, UserType)








# Login function 
# returns:
#      0 for failed login
#      1 for admin login
#      2 for admin-visitor login
#      3 for manager login 
#      4 for manager-visitor login
#      5 for staff login 
#      6 for staff-visitor login
#      7 for visitor login 

def login(username, password):
	# establish connection to DB
	set_connection()

	# execute the query 
	hashed_password = hashlib.md5(password).hexdigest()
	login_response = db_login(username, hashed_password)

	# close the connection to the DB
	close_connection()

	return login_response


# Function that check if user is an admin
# 
# returns:
#   0 - User is not
#   1 - User is

def isAdmin(username):
    # set up connection
    set_connection()

    # execute the query
    isAdmin = db_emp_isAdmin(username)

    # close connection
    close_connection()

    return isAdmin