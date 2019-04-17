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
            print("*          Preparing for connection        *")

            _database = pymysql.connect(host="localhost",
                                        user="root",
                                        passwd="password",
                                        db="beltline")

            print("*   Connection is secure and ready to go   *")
            _cursor = _database.cursor()
            _connected = True
            if _connected:
                # _cursor.execute("SELECT VERSION()")
                # version = _cursor.fetchone()
                # print("Database version: {}".format(version[0]))
                print("*     Connection Setup Successfully!       *")
            else:
                print("*        Connection Setup Failed!          *")
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
# might not need this:
# def db_emp_isAdmin(username):
#     query = "SELECT * FROM Employee WHERE Username = '%s' AND EmployeeType ='%s'"
#     response = _cursor.execute(query % (username, 'Admin'))
#     return _cursor.fetchall()

# Function to check the login status of a user
#
# returns:
#   0 if there was an error in logging in
#   UserType if user successfully logged in

def db_login(username, password):
    query0 = "SELECT Username, Password FROM allusers WHERE Username= %s AND Password = %s AND Status != %s"
    response0 = _cursor.execute(query0 , (username, password, "Declined"))
    _cursor.fetchall()

    # if login is bad, error out
    if response0 == 0:
        # print("bad login")
        return 0
    elif response0 ==1:
        query1 = "SELECT UserType from allusers WHERE Username = %s"
        response1 = _cursor.execute(query1, (username))
        # print("good login")
        return(_cursor.fetchone())[0]
    else:
        return 0

# def db_login_username(username, password):
#     query0 = "SELECT Username, Password FROM allusers WHERE Username= %s AND Password = %s AND Status != %s"
#     response0 = _cursor.execute(query0 , (username, password, "Declined"))
#     _cursor.fetchall()

#     # if login is bad, error out
#     if response0 == 0:
#         # print("bad login")
#         return 0
#     elif response0 ==1:
#         query1 = "SELECT Username from allusers WHERE Username = %s"
#         response1 = _cursor.execute(query1, (username))
#         return(_cursor.fetchone())[0]
#     else:
#         return 0


# Function to hash all paswords stored in the database (Not needed because passwords in DB should already be hashed)
# def hash_password():
#     set_connection()
#     query = "UPDATE allusers SET Password = MD5(Password)"
#     response = _cursor.execute(query)


# Function to check the account status of a user (Utilized mainly for employees)
# returns:
#   0 if status == declined
#   1 if status == approved
#   2 if staus == pending
def status_checker(username):
    query = "SELECT Status FROM allusers WHERE Username= %s AND UserType =%s"
    response = _cursor.execute(query, (username, 'Employee'))
    result = _cursor.fetchone()[0]

    if result in ['Approved']:
        # NEED TO DO AN UPDATE STATEMENT SOMEWHERE WITH EMPLOYEEID
        return 1
    elif result in ['Pending']:
        return 2
    else:
        return 0


# Register function to insert users or visitors into User table
# returns:
#   0 - successfully inserted
#   1 - primary key violation
#   2 - other violations
def user_insert(Username, Password, Status, Firstname, Lastname, UserType):
    query = "INSERT INTO allusers(Username, Password, Status, Firstname, Lastname, UserType) VALUES (%s, %s, %s, %s, %s, %s)"
    try:
        print("log :: executing user insertion query\n")
        _cursor.execute(query, (Username, Password, Status, Firstname, Lastname, UserType))
        _database.commit()
        print("++ Successfully inserted " + Username + " into user table ++\n")
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

def email_insert(Username, Email):
    print(Username)
    print(Email)
    query = "INSERT INTO useremail(Username, Email) VALUES(%s, %s)"
    try:
        print("log :: executing user insertion query\n")
        _cursor.execute(query ,(Username, Email))
        _database.commit()
        print("++ Successfully inserted " + Email + " into email table ++\n")
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
def employee_insert(Username, EmployeeID, Phone, EmployeeAddress, EmployeeCity, EmployeeState, EmployeeZipcode, EmployeeType):
    query = "INSERT INTO employee(Username, EmployeeID, Phone, EmployeeAddress, EmployeeCity, EmployeeState, EmployeeZipcode, EmployeeType) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    try:
        print("log :: executing employee insertion query\n")
        _cursor.execute(query, (Username, EmployeeID, Phone, EmployeeAddress, EmployeeCity, EmployeeState, EmployeeZipcode, EmployeeType))
        _database.commit()
        print("++ Successfully inserted " + Username + " into employee table ++\n")
        return 0

    except Exception as e:
        print("---> run into Exception:")
        print("---> " + str(e) + '\n')  # print exception message
        if str(e)[1:5] == "1062":
            # violates primary key constraint username
            return 1
        else:
            # other violation
            return 2


def getSiteNames():
    querySitenames = """
        SELECT DISTINCT SiteName
        FROM site;"""
    response = _cursor.execute(querySitenames)
    return _cursor.fetchall()

def getTransitTypes():
    queryTransitType = """
        SELECT DISTINCT TransitType
        FROM transit;"""
    response = _cursor.execute(queryTransitType)
    return _cursor.fetchall()

def getAllTransit():
    queryTransit = """
        SELECT T.TransitRoute, T.TransitType, T.TransitPrice, C.Count
        FROM transit AS T
        INNER JOIN (
            SELECT TransitRoute, TransitType, Count(*) AS Count
            FROM connect
            GROUP BY TransitRoute, TransitType ) AS C
        ON T.TransitType = C.TransitType
        WHERE T.TransitRoute = C.TransitRoute
        """
    response = _cursor.execute(queryTransit)
    return _cursor.fetchall()

def getAllTransit2(user):
    queryTransit = """
        SELECT TransitDate, TransitRoute, TransitType, TransitPrice
        FROM (
            SELECT TT.Username, TT.TransitDate, TT.TransitRoute, TT.TransitType, T.TransitPrice
            FROM taketransit AS TT
            INNER JOIN (
              	SELECT TransitType, TransitRoute, TransitPrice
                FROM transit ) AS T
            ON TT.TransitType = T.TransitType
            WHERE TT.TransitRoute = T.TransitRoute
        ) AS A
        WHERE A.Username = '%s';
        """
    response = _cursor.execute(queryTransit % (user))
    return _cursor.fetchall();

def getFilteredTransit(site, type, minPrice, maxPrice):
    if(minPrice == ""):
        minPrice = -1
    if(maxPrice == ""):
        maxPrice = -1
    minPrice = float(minPrice)
    maxPrice = float(maxPrice)

    queryTransit = """
        SELECT DISTINCT TransitRoute, TransitType, TransitPrice, D.Count
        FROM (
            SELECT E.TransitRoute, E.TransitType, E.TransitPrice, E.Count, F.SiteName
            FROM (
                SELECT T.TransitRoute, T.TransitType, T.TransitPrice, C.Count
                FROM transit AS T
                INNER JOIN (
                    SELECT TransitRoute, TransitType, Count(*) AS Count
                    FROM connect
                    GROUP BY TransitRoute, TransitType
                ) AS C
                ON T.TransitType = C.TransitType
                WHERE T.TransitRoute = C.TransitRoute
            ) AS E
            INNER JOIN (
                SELECT TransitRoute, TransitType, SiteName
                FROM connect
            ) AS F
            ON F.TransitType = E.TransitType
            WHERE F.TransitRoute = E.TransitRoute
        ) AS D
        WHERE (D.SiteName = '%s' OR '%s' = '-ALL-')
        AND (D.TransitPrice >= %.1f OR %.1f = -1.0)
        AND (D.TransitPrice <= %.1f OR %.1f = -1.0)
        AND (D.TransitType = '%s' OR '%s' = '-ALL-');
        """
    response = _cursor.execute(queryTransit % (site, site, minPrice, minPrice, maxPrice, maxPrice, type, type));
    return _cursor.fetchall()

def getFilteredTransit2(user, site, type, route, startDate, endDate):
    if(route == ""):
        route = "-ALL-"
    query = """
        SELECT DISTINCT B.TransitDate, B.TransitRoute, B.TransitType, B.TransitPrice
        FROM (
            SELECT A.TransitDate, A.TransitRoute, A.TransitType, A.TransitPrice
            FROM (
                SELECT TT.Username, TT.TransitDate, TT.TransitRoute, TT.TransitType, T.TransitPrice
                FROM taketransit AS TT
                INNER JOIN (
                    SELECT *
                    FROM transit
                ) AS T
                ON TT.TransitType = T.TransitType
                WHERE TT.TransitRoute = T.TransitRoute
            ) AS A
            INNER JOIN (
                SELECT TransitRoute, TransitType, SiteName
                FROM connect
            ) AS C
            ON C.TransitType = A.TransitType
            WHERE C.TransitRoute = A.TransitRoute
            AND A.Username = '%s'
            AND (C.SiteName = '%s' OR '%s' = '-ALL-')
            AND (A.TransitType = '%s' OR '%s' = '-ALL-')
            AND (A.TransitRoute = '%s' OR '%s' = '-ALL-')
        ) AS B;
        """
        # add support for checking the dates
    response = _cursor.execute(query % (user, site, site, type, type, route, route))
    return _cursor.fetchall();

def logTransit(user, transit, date):
    transit = transit.replace("{", "").replace("}", "")
    fields = transit.split(", ")

    route = ""
    ttype = ""

    for field in fields:
        print(field)
        if(len(field) >= 14 and field[0:14]=="'TransitRoute'"):
            strings = field.split(": ")
            route = strings[1][1:len(strings[1])-1]
        if(len(field) >= 13 and field[0:13]=="'TransitType'"):
            strings = field.split(": ")
            ttype = strings[1][1:len(strings[1])-1]
    print(route)
    print(ttype)
    print(date)
    query = """
        INSERT INTO taketransit
        VALUES ('%s', '%s', '%s', '%s');
        """;
    response = _cursor.execute(query % (user, ttype, route, date))
    _database.commit();

# Delete user function:
# applications: if an employee cannot be added to employee table due to duplicate phone number, delete them from user table and throw duplicate exception
def user_delete(Username):
    query = "DELETE FROM allusers WHERE Username = '%s';"
    try:
        print("log :: executing user deletion query\n")
        _cursor.execute(query % (Username))
        _database.commit()
        print("++ Successfully delete " + Username + " from users table ++\n")
        return 0

    except Exception as e:
        print("---> run into Exception:")
        print("---> " + str(e) + '\n')  # print exception message
        return 1



# Function to determine type of employee
#
# return:
# Employeetype
def get_emptype(Username):
    query = "SELECT EmployeeType FROM employee WHERE Username= %s"
    response = _cursor.execute(query, (Username))
    return(_cursor.fetchone())[0]



    # if result in ['Admin']:
    #     return 1
    # elif result in ['Admin, Visitor']:
    #     return 2
    # elif result in ['Manager']:
    #     return 3
    # elif result in ['Manager, Visitor']:
    #     return 4
    # elif result in ['Staff']:
    #     return 5
    # elif result in ['Staff, Visitor']:
    #     return 6
    # else:
    #     return 0

# Function to determine type of employee
#
# return:
# UserType
def get_usertype(Username):
    query = "SELECT UserType FROM allusers WHERE Username= %s"
    response = _cursor.execute(query, (Username))
    return(_cursor.fetchone())[0]




def get_employee_info(user):
    query = """
        SELECT U.Firstname, U.Lastname, U.Username, S.SiteName, E.EmployeeID, E.Phone, E.EmployeeAddress, E.EmployeeCity, E.EmployeeState, E.EmployeeZipcode
        FROM allusers AS U
        INNER JOIN (
            SELECT Username, EmployeeID, Phone, EmployeeAddress, EmployeeCity, EmployeeState, EmployeeZipcode
            FROM employee
        ) AS E
        ON U.Username = E.Username
        INNER JOIN (
            SELECT SiteName, ManagerUsername
            FROM site
        ) AS S
        ON U.Username = S.ManagerUsername
        WHERE U.Username = '%s';
        """
    response = _cursor.execute(query % (user))
    return _cursor.fetchall();

def get_employee_emails(user):
    query = """
        SELECT Email
        FROM useremail
        WHERE Username = '%s';
        """

    response = _cursor.execute(query % (user));
    return _cursor.fetchall();

def getAllUsersList():
    query = """
        SELECT U.Username, Email.Count, U.UserType, U.Status
        FROM allusers AS U
        INNER JOIN (
          	SELECT DISTINCT Username, COUNT(Username) AS Count
            FROM useremail
            GROUP BY Username
        ) As Email
        ON U.Username = Email.Username;
        """
    response = _cursor.execute(query)
    return _cursor.fetchall();

def getFilteredUsersList(user, type, status):
    if(user == ""):
        user = "-ALL-";

    query = """
        SELECT U.Username, Email.Count, U.UserType, U.Status
        FROM allusers AS U
        INNER JOIN (
          	SELECT DISTINCT Username, COUNT(Username) AS Count
            FROM useremail
            GROUP BY Username
        ) As Email
        ON U.Username = Email.Username
        WHERE (U.Username = '%s' OR '%s' = '-ALL-')
        AND (U.UserType = '%s' OR '%s' = '-ALL-')
        AND (U.Status = '%s' OR '%s' = '-ALL-')
        """
    response = _cursor.execute(query % (user, user, type, type, status, status))
    return _cursor.fetchall();

def getManagerNames():
    query = """
        SELECT ManagerUsername
        FROM site;
        """
    response = _cursor.execute(query)
    return _cursor.fetchall();

def getAllSites():
    query = """
        SELECT SiteName, ManagerUsername, OpenEveryday
        FROM site;
        """
    response = _cursor.execute(query)
    return _cursor.fetchall();

def getFilteredSites(site, manager, openeveryday):
    query = """
        SELECT SiteName, ManagerUsername, OpenEveryday
        FROM site
        WHERE (SiteName = '%s' OR '%s' = '-ALL-')
        AND (ManagerUsername = '%s' OR '%s' = '-ALL-')
        AND (OpenEveryday = '%s' OR '%s' = '-ALL-')
        """
    response = _cursor.execute(query % (site, site, manager, manager, openeveryday, openeveryday))
    return _cursor.fetchall()

def getAllTransitsM():
    query = """
        SELECT C.TransitRoute, C.TransitType, C.TransitPrice, C.ConnectedCount, F.LoggedCount
        FROM (
            SELECT T.TransitRoute, T.TransitType, T.TransitPrice, E.ConnectedCount
            FROM transit AS T
            INNER JOIN (
                SELECT TransitRoute, TransitType, COUNT(*) AS ConnectedCount
                FROM connect
                GROUP BY TransitRoute, TransitType
            ) AS E
            ON E.TransitRoute = T.TransitRoute
            WHERE E.TransitType = T.TransitType
        ) AS C
        INNER JOIN (
            SELECT TransitRoute, TransitType, COUNT(*) AS LoggedCount
            FROM taketransit
            GROUP BY TransitRoute, TransitType
        ) AS F
        ON F.TransitRoute = C.TransitRoute
        WHERE F.TransitType = C.TransitType;
        """
    response = _cursor.execute(query)
    return _cursor.fetchall();

def getFilteredTransitsM(site, type, route, minPrice, maxPrice):
    if(minPrice == ""):
        minPrice = -1
    if(maxPrice == ""):
        maxPrice = -1;
    if(route == ""):
        route = "-ALL-"
    minPrice = float(minPrice)
    maxPrice = float(maxPrice)
    query = """
        SELECT DISTINCT D.TransitRoute, D.TransitType, D.TransitPrice, D.ConnectedCount, D.LoggedCount
        FROM (
            SELECT C.TransitRoute, C.TransitType, C.TransitPrice, C.ConnectedCount, F.LoggedCount, C.SiteName
            FROM (
                SELECT B.TransitRoute, B.TransitType, B.TransitPrice, B.ConnectedCount, A.SiteName
                FROM (
                    SELECT T.TransitRoute, T.TransitType, T.TransitPrice, E.ConnectedCount
                    FROM transit AS T
                    INNER JOIN (
                        SELECT TransitRoute, TransitType, COUNT(*) AS ConnectedCount
                        FROM connect
                        GROUP BY TransitRoute, TransitType
                    ) AS E
                    ON E.TransitRoute = T.TransitRoute
                    WHERE E.TransitType = T.TransitType
                ) AS B
                INNER JOIN (
                    SELECT TransitRoute, TransitType, SiteName
                    FROM connect
                ) AS A
                ON B.TransitRoute = A.TransitRoute
                WHERE B.TransitType = A.TransitType
            ) AS C
            INNER JOIN (
                SELECT TransitRoute, TransitType, COUNT(*) AS LoggedCount
                FROM taketransit
                GROUP BY TransitRoute, TransitType
            ) AS F
            ON F.TransitRoute = C.TransitRoute
            WHERE F.TransitType = C.TransitType
        ) AS D
        WHERE (D.SiteName = '%s' OR '%s' = '-ALL-')
        AND (D.TransitType = '%s' OR '%s' = '-ALL-')
        AND (D.TransitRoute = '%s' OR '%s' = '-ALL-')
        AND (D.TransitPrice >= %.1f OR %.1f = -1.0)
        AND (D.TransitPrice <= %.1f OR %.1f = -1.0);
        """
    response = _cursor.execute(query % (site, site, type, type, route, route, minPrice, minPrice, maxPrice, maxPrice))
    return _cursor.fetchall();

def update_employee(user, fname, lname, phone, visitor):
    query0 = """
        UPDATE allusers
        SET Firstname = '%s', Lastname = '%s'
        WHERE Username = '%s';
        """
    response = _cursor.execute(query0 % (fname, lname, user))
    _database.commit();

    query1 = """
        UPDATE employee
        SET Phone = '%s'
        WHERE Username = '%s';
        """
    response = _cursor.execute(query1 % (phone, user))
    _database.commit();

    # TODO UPDATE VISITOR
    # visitor = 0 ... isVisitor = false
    # visitor = 1 ... isVisitor = true

def deleteEmail(email):
    query = """
        DELETE FROM useremail
        WHERE Email = '%s';
        """
    response = _cursor.execute(query % (email))
    _database.commit();

def get_site_info(sitename):
    query = """
        SELECT *
        FROM site
        WHERE SiteName = '%s'
        """
    response = _cursor.execute(query % (sitename))
    return _cursor.fetchall();

def update_site(oldname, name, zip, address, manager, everyday):
    query = """
        UPDATE site
        SET SiteName = '%s', SiteAddress = '%s', SiteZipcode = '%s', OpenEveryday = '%s', ManagerUsername = '%s'
        WHERE Sitename = '%s';
        """
    response = _cursor.execute(query % (name, address, zip, everyday, manager, oldname));
    _database.commit();

def getUnassignedManagers():
    query = """
        SELECT Username
        FROM employee
        WHERE EmployeeType = 'Manager'
        AND Username NOT IN (
            SELECT ManagerUsername
            FROM site
        )
        """
    response = _cursor.execute(query)
    return _cursor.fetchall();

def add_site(name, address, zip, everyday, manager):
    query = """
        INSERT INTO site
        VALUES ('%s', '%s', '%s', '%s', '%s')
        """
    response = _cursor.execute(query % (name, address, zip, everyday, manager))
    _database.commit();

def removesite(name):
    query = """
        DELETE FROM site
        WHERE SiteName = '%s'
        """
    response = _cursor.execute(query % (name))
    _database.commit();










    #bottom
