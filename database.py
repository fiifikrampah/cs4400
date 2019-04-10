# This file interacts with the main database

from datetime import datetime
import pymysql
import traceback


# Establish a secure connection to the database (which will be hosted on some gatech server?)

#Global variables for use [local to this file. Do not get imported in the other python files:
_connected = False
_database = None
_cursor = None  

def set_connection(): 
    global _connected
    global _database
    global _cursor

    if not _connected:
        try:
            print("********************************************")
            print("*          Preparing for connection          *")

            _database = pymysql.connect(host="localhost",
                                        user="root",
                                        passwd="password",
                                        db="beltline")

            print("*    Connection is secure and ready to go     *")
            _cursor = _database.cursor()
            _connected = True
            if _connected:
                # _cursor.execute("SELECT VERSION()")
                # version = _cursor.fetchone()
                # print("Database version: {}".format(version[0]))
                print("*            Connection Setup Successfully!            *")
            else:
                print("*            Connection Setup Failed!              *")
            print("********************************************\n")

        except Exception as e:
            _connected = False
            traceback.print_exc()

def close_connection():
    global _connected

    if _connected:
        _database.close()
        _connected = False
    print("********************************************\n" +
          "*            Connection Closed            *\n" +
          "********************************************\n")

# Function that checks if user is an admin
# returns: 0 (not admin), 1 (admin)

def db_emp_isAdmin(username):
    query = "SELECT * FROM Employee WHERE Username = '%s' AND EmployeeType ='%s'"
    response = _cursor.execute(query % (username, 'Admin'))
    return _cursor.fetchall()



# Function that checks if a user's account is declined
# returns: 0 (approved/pending), 1 (declined)


# Might not need this anymore...might need to change to status_update function for admin to approve accounts
# def db_isDeclined(username):
#     query = "SELECT * FROM User WHERE Username = '%s' AND Status = '%s'"
#     response = _cursor.execute(query % (username, 'Declined'))
#     return _cursor.fetchall()


# Function to check the login status of a user
#
# returns:
#   0 if there was an error in logging in
#   UserType if user successfully logged in

def db_login(username, password):
    query0 = "SELECT Username, Password FROM AllUsers WHERE Username= '%s' AND Password = '%s' AND Status != '%s'"
    response0 = _cursor.execute(query0 % (username, password, "Declined"))
    _cursor.fetchall()

    # if login is bad, error out
    if response0 == 0:
        # print("bad login")
        return 0
    elif response0 ==1:
        query1 = "SELECT UserType from AllUsers WHERE Username = '%s'"
        response1 = _cursor.execute(query1 % (username))
        # print("good login")
        return(_cursor.fetchone())[0]
    else:
        return 0

# Function to hash all paswords stored in the database
def hash_password():
    set_connection()
    query = "UPDATE AllUsers SET Password = MD5(Password)"
    response = _cursor.execute(query)

    

# Register function to insert users or visitors into User table
# returns:
#   0 - successfully inserted
#   1 - primary key violation
#   2 - other violations
def user_insert(username, password, status, fname, lname, UserType):
    query = "INSERT INTO User(Username, Password, Status, FirstName, LastName, UserType) VALUES ('%s', '%s', '%s', '%s', '%s', '%s')"
    try:
        print("log :: executing user insertion query\n")
        _cursor.execute(query % (username, password, 'Pending', fname, lname, UserType))
        _database.commit()
        print("++ Successfully inserted " + username + " into database ++\n")
        return 0

    except Exception as e:
        print("---> run into Exception:")
        print("---> " + str(e) + '\n')  # print exception message
        if str(e)[1:5] == "1062":
            # violates primary key constraint
            return 1
        else:
            # other violation  
            return 2

# Email Register function to insert emails into UserEmail table 
#   0 - successfully inserted
#   1 - primary key violation
#   2 - other violations

def email_insert(username, email):
    query = "INSERT INTO UserEmail(Username, Email) VALUES('%s', '%s')"
    try:
        print("log :: executing user insertion query\n")
        _cursor.execute(query % (username, email))
        _database.commit()
        print("++ Successfully inserted " + email + " into database ++\n")
        return 0

    except Exception as e:
        print("---> run into Exception:")
        print("---> " + str(e) + '\n')  # print exception message
        if str(e)[1:5] == "1062":
            # violates primary key constraint
            return 1
        else:
            # other violation  
            return 2

# Register function to insert employee into Employee table
# returns:
#   0 - successfully inserted
#   1 - primary key violation
#   2 - other violations
def employee_insert(username, eID, phone, eAddress, eCity, eState, eZipcode, eType):
    query = "INSERT INTO Employee(Username, EmployeeID, Phone, EmployeeAddress, EmployeeCity, EmployeeState, EmployeeZipcode, EmployeeType) VALUES ('%s', '%d', '%d', '%s', '%s', '%s', '%d', '%s')"
    try:
        print("log :: executing user insertion query\n")
        _cursor.execute(query % (username, eID, phone, eAddress, eCity, eState, eZipcode, eType))
        _database.commit()
        print("++ Successfully inserted " + username + " into database ++\n")
        return 0

    except Exception as e:
        print("---> run into Exception:")
        print("---> " + str(e) + '\n')  # print exception message
        if str(e)[1:5] == "1062":
            # violates primary key constraint
            return 1
        else:
            # other violation  
            return 2


