# This file serves as the controller for the backend. Contains stored procedures

from database import *
from constraints import *
import hashlib
import random

# Register user function; inserts tuples into the user table

def validate_user_registration(Username, Password, Status, Firstname, Lastname, UserType):
	set_connection()
	# execute the query
	# isDeclined_result = db_isDeclined(username)
	# if isDeclined_result == 1:
	hashed_password = hashlib.md5(Password).hexdigest()
	user_insert_result = user_insert(Username, hashed_password,Status, Firstname, Lastname, UserType)
	if user_insert_result == 0:
		return 0
	elif user_insert_result == 1:
		return 1 
	else:
		return 2


# Register employee function:
def validate_employee_registration(Username, EmployeeID, Phone, EmployeeAddress, EmployeeCity, EmployeeState, EmployeeZipcode, EmployeeType):
	set_connection()
	employee_insert_result = employee_insert(Username, EmployeeID, Phone, EmployeeAddress, EmployeeCity, EmployeeState, EmployeeZipcode, EmployeeType)
	if employee_insert_result == 0:
		return 0
	elif employee_insert_result == 1:
		user_delete(Username)
		return 1 
	else:
		return 2



# Login function 
# returns:
#   0 if there was an error in logging in
#   UserType if user successfully logged in

def login(username, password):
	# establish connection to DB
	set_connection()

	# execute the query 
	hashed_password = hashlib.md5(password).hexdigest()
	login_response = db_login(username, hashed_password)

	# close the connection to the DB
	close_connection()

	return login_response

# Usernamefunction 
# returns:
#   0 if there was an error in logging in
#   Username if user successfully logged in

# def who_am_i(username, password):
# 	# establish connection to DB
# 	set_connection()

# 	# execute the query 
# 	hashed_password = hashlib.md5(password).hexdigest()
# 	login_response = db_login_username(username, hashed_password)

# 	# close the connection to the DB
# 	close_connection()

# 	return login_response


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

# Function to generate employeeID once account has been approved by administrator
# returns:
# ID if account status == approved
# NULL if account status == pending

def employeeid_generator():
	set_connection()
	isApproved = status_checker()
	if isApproved == 1:
		id = random.randint(100000000,999999999)
		return id
	elif isApproved == 2 or isApproved == 0:
		id = null
		return id


# Function to determine employee type for login
def emptype_checker(Username):
	set_connection()
	usertype_result = get_emptype(Username)
	return usertype_result


# Function to determine user type for back
def usertype_checker(Username):
	set_connection()
	usertype_result = get_usertype(Username)
	return usertype_result