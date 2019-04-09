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
                                        db="company")

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
#      0 for failed login
#      1 for regular_user login
#      2 for admin login
#      3 for admin-visitor login
#      4 for manager login 
#      5 for manager-visitor login
#      6 for staff login 
#      7 for staff-visitor login
#      8 for visitor login 
# 

def db_login(username, password):
    query0 = "SELECT * FROM User WHERE Username= '%s' AND Password = '%s'"
    response0 = _cursor.execute(query0 % (username, password))
    query1 = "SELECT * FROM User WHERE Username = '%s' AND Password ='%s' AND Status != '%s' AND UserType ='%s'"
    response1 = _cursor.execute(query1 % (username, password, 'User'))
    query2= "SELECT * FROM Employee WHERE Username = '%s' AND Password = '%s' AND EmployeeType ='%s'"
    response2 = _cursor.execute(query2 % (username, password,'Admin'))
    query3 = "SELECT * FROM User WHERE Username = '%s' AND Password ='%s' AND Status != '%s' AND UserType ='%s'"
    response3 = _cursor.execute(query3 % (username, password,'Declined', 'Admin-Visitor'))
    query4 = "SELECT * FROM User WHERE Username = '%s' AND Password ='%s' AND Status != '%s' AND UserType ='%s'"
    response4 = _cursor.execute(query3 % (username, password,'Declined', 'Manager'))
    query5 = "SELECT * FROM User WHERE Username = '%s' AND Password ='%s' AND Status != '%s' AND UserType ='%s'"
    response5 = _cursor.execute(query3 % (username, password,'Declined', 'Manager-Visitor'))
    query6 = "SELECT * FROM User WHERE Username = '%s' AND Password ='%s' AND Status != '%s' AND UserType ='%s'"
    response6 = _cursor.execute(query3 % (username, password,'Declined', 'Staff'))
    query7 = "SELECT * FROM User WHERE Username = '%s' AND Password ='%s' AND Status != '%s' AND UserType ='%s'"
    response7 = _cursor.execute(query3 % (username, password,'Declined', 'Staff-Visitor'))
    query8 = "SELECT * FROM User WHERE Username = '%s' AND Password ='%s' AND Status != '%s' AND UserType ='%s'"
    response8 = _cursor.execute(query3 % (username, password,'Declined', 'Visitor'))
    _cursor.fetchall()

    if response0 == 0:
        return 0
    elif response1 == 1:
        return 1
    elif response2 == 1:
        return 2
    elif response3 == 1:
        return 3
    elif response4 == 1:
        return 4
    elif response5 == 1:
        return 5
    elif response6 == 1:
        return 6
    elif response7 == 1:
        return 7
    elif response8 == 1:
        return 8
    else:
        return 0


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



