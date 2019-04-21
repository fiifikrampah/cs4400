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
    return _cursor.fetchall();

def getTransit15(site, type, minPrice, maxPrice, sort):
    if(site is None):
        site = "-ALL-"
    if(type is None):
        type = "-ALL-"
    if(sort is None):
        sort = "TransitType ASC"
    if(minPrice == "" or minPrice is None):
        minPrice = -1
    if(maxPrice == "" or maxPrice is None):
        maxPrice = -1
    minPrice = float(minPrice)
    maxPrice = float(maxPrice)

    queryTransit = """
        SELECT *
        FROM (
            SELECT DISTINCT TransitRoute, TransitType, TransitPrice, D.Count AS ConnectedSites
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
            AND (D.TransitType = '%s' OR '%s' = '-ALL-')
        ) AS Z
        ORDER BY %s
        """
    response = _cursor.execute(queryTransit % (site, site, minPrice, minPrice, maxPrice, maxPrice, type, type, sort));
    return _cursor.fetchall()

def getTransit16(user, site, type, route, startDate, endDate, sort):
    if(site is None):
        site = "-ALL-"
    if(type is None):
        type = "-ALL-"
    if(sort is None):
        sort = "TransitType ASC"
    if(startDate  == "" or startDate is None):
        startDate = "-ALL-"
    if(endDate == "" or endDate is None):
        endDate = "-ALL-"
    if(route == "" or route is None):
        route = "-ALL-"

    query = """
        SELECT *
        FROM (
            SELECT DISTINCT A.TransitDate, A.TransitRoute, A.TransitType, A.TransitPrice
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
            AND ('%s' = '-ALL-' OR DATEDIFF(A.TransitDate, '%s') >= 0)
            AND ('%s' = '-ALL-' OR DATEDIFF('%s', A.TransitDate) >= 0)
        ) AS B
        ORDER BY %s
        """
    response = _cursor.execute(query % (user, site, site, type, type, route, route, startDate, startDate, endDate, endDate, sort))
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
    return _cursor.fetchone();

def get_employee_emails(user):
    query = """
        SELECT Email
        FROM useremail
        WHERE Username = '%s';
        """

    response = _cursor.execute(query % (user));
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


def getSites19(site, manager, openeveryday, sort):
    if(site is None):
        site = "-ALL-"
    if(manager is None):
        manager = "-ALL-"
    if(openeveryday is None):
        openeveryday = "-ALL-"
    if(sort is None):
        sort = "SiteName ASC"
    query = """
        SELECT SiteName, ManagerUsername, OpenEveryday
        FROM site
        WHERE (SiteName = '%s' OR '%s' = '-ALL-')
        AND (ManagerUsername = '%s' OR '%s' = '-ALL-')
        AND (OpenEveryday = '%s' OR '%s' = '-ALL-')
        ORDER BY %s
        """
    response = _cursor.execute(query % (site, site, manager, manager, openeveryday, openeveryday, sort))
    return _cursor.fetchall()

def getTransit22(site, type, route, minPrice, maxPrice, sort):
    if(site is None):
        site="-ALL-"
    if(type is None):
        type="-ALL-"
    if(minPrice == "" or minPrice is None):
        minPrice = -1
    if(maxPrice == "" or maxPrice is None):
        maxPrice = -1
    if(route == "" or route is None):
        route = "-ALL-"
    if(sort is None):
        sort = "TransitRoute ASC"
    minPrice = float(minPrice)
    maxPrice = float(maxPrice)
    query = """
        SELECT DISTINCT Z.Transitroute, Z.TransitType, Z.TransitPrice, Z.ConnectedSites, Z.TransitsLogged
        FROM (
            SELECT D.TransitRoute, D.TransitType, D.TransitPrice, D.ConnectedCount AS ConnectedSites, D.LoggedCount AS TransitsLogged, D.SiteName
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

            UNION

            SELECT K.TransitRoute, K.TransitType, K.TransitPrice, K.ConnectedSites, K.TransitsLogged, J.SiteName
            FROM (
                SELECT I.TransitRoute, I.TransitType, I.TransitPrice, I.ConnectedCount AS ConnectedSites, 0 AS TransitsLogged
                FROM (
                    SELECT G.TransitRoute, G.TransitType, G.TransitPrice, H.ConnectedCount
                    FROM transit AS G
                    INNER JOIN (
                        SELECT TransitRoute, TransitType, Count(*) AS ConnectedCount
                        FROM connect
                        GROUP BY TransitRoute, TransitType
                    ) AS H
                    ON G.TransitRoute = H.TransitRoute
                    WHERE G.TransitType = H.TransitType
                    AND NOT EXISTS (
                        SELECT TransitRoute, TransitType
                        FROM taketransit AS J
                        WHERE J.TransitRoute = G.TransitRoute
                        AND J.TransitType = G.TransitType
                    )
                ) AS I
            ) AS K
            INNER JOIN (
                SELECT TransitRoute, TransitType, SiteName
                FROM connect
            ) AS J
            ON K.TransitRoute = J.TransitRoute
            WHERE K.TransitType = J.TransitType
        )AS Z
        WHERE (Z.SiteName = '%s' OR '%s' = '-ALL-')
        AND (Z.TransitType = '%s' OR '%s' = '-ALL-')
        AND (Z.TransitRoute = '%s' OR '%s' = '-ALL-')
        AND (Z.TransitPrice >= %.1f OR %.1f = -1.0)
        AND (Z.TransitPrice <= %.1f OR %.1f = -1.0)
        ORDER BY %s
        """
    response = _cursor.execute(query % (site, site, type, type, route, route, minPrice, minPrice, maxPrice, maxPrice, sort))
    return _cursor.fetchall();

def update_employee(user, fname, lname, phone, visitor):
    query0 = """
        UPDATE allusers
        SET Firstname = %s, Lastname = %s
        WHERE Username = %s;
        """
    response = _cursor.execute(query0, (fname, lname, user))
    _database.commit();

    query1 = """
        UPDATE employee
        SET Phone = %s
        WHERE Username = %s;
        """
    response = _cursor.execute(query1, (phone, user))
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
        SET SiteName = %s, SiteAddress = %s, SiteZipcode = %s, OpenEveryday = %s, ManagerUsername = %s
        WHERE Sitename = %s;
        """
    response = _cursor.execute(query, (name, address, zip, everyday, manager, oldname));
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
        VALUES (%s, %s, %s, %s, %s)
        """
    response = _cursor.execute(query, (name, address, zip, everyday, manager))
    _database.commit();

def removesite(name):
    query = """
        DELETE FROM site
        WHERE SiteName = '%s'
        """
    response = _cursor.execute(query % (name))
    _database.commit();

def set_transit(type, oldroute, route, price):
    query = """
        UPDATE transit
        SET TransitRoute = %s, TransitPrice = %s
        WHERE (TransitType = %s AND TransitRoute = %s)
        """
    response = _cursor.execute(query, (route, price, type, oldroute));
    _database.commit();

def change_transit_connections(type, oldroute, route, sites):
    query = """
        DELETE FROM connect
        WHERE TransitType = '%s'
        AND TransitRoute = '%s'
        """
    response = _cursor.execute(query % (type, oldroute));
    _database.commit();

    queryAdd = """
        INSERT INTO connect
        VALUES (%s, %s, %s)
        """
    for site in sites:
        responseAdd = _cursor.execute(queryAdd, (site, type, route))
        _database.commit()

def createtransit(type, route, price, sites):
    query0 = """
        INSERT INTO transit
        VALUES (%s, %s, %s)
        """
    response0 = _cursor.execute(query0, (type, route, price))
    _database.commit();

    query2 = """
        DELETE FROM connect
        WHERE TransitType = '%s'
        AND TransitRoute = '%s'
        """
    response2 = _cursor.execute(query2 % (type, route))
    _database.commit()

    query1 = """
        INSERT INTO connect
        VALUES (%s, %s, %s)
        """
    for site in sites:
        response1 = _cursor.execute(query1, (site['SiteName'], type, route))
        _database.commit();

def deletetransit(type, route):
    query = """
        DELETE FROM transit
        WHERE TransitType = '%s'
        AND TransitRoute = '%s'
        """
    response = _cursor.execute(query % (type, route))
    _database.commit()

    query = """
        DELETE FROM connect
        WHERE TransitType = '%s'
        AND TransitRoute = '%s'
        """
    response = _cursor.execute(query % (type, route))
    _database.commit()

    query = """
        DELETE FROM taketransit
        WHERE TransitType = '%s'
        AND TransitRoute = '%s'
        """
    response = _cursor.execute(query % (type, route))
    _database.commit()

def get_connected_sites(route, type):
    query = """
        SELECT SiteName
        FROM connect
        WHERE TransitType = '%s'
        AND TransitRoute = '%s'
        """
    response = _cursor.execute(query % (type, route));
    return _cursor.fetchall();

def change_transit_history(type, oldroute, route):
    query = """
        UPDATE taketransit
        SET TransitRoute = %s
        WHERE TransitType = %s
        AND TransitRoute = %s
        """
    response = _cursor.execute(query, (route, type, oldroute))
    _database.commit();

def get_site_report(stDate, endDate, eCountMin, eCountMax, stCountMin, stCountMax, toVisMin, toVisMax, toRevMin, toRevMax, sort):
    if(eCountMin == "" or eCountMin is None):
        eCountMin = -1
    if(eCountMax == "" or eCountMax is None):
        eCountMax = -1
    if(stCountMin == "" or stCountMin is None):
        stCountMin = -1
    if(stCountMax == "" or stCountMax is None):
        stCountMax = -1
    if(toVisMin == "" or toVisMin is None):
        toVisMin = -1
    if(toVisMax == "" or toVisMax is None):
        toVisMax = -1
    if(toRevMin == "" or toRevMin is None):
        toRevMin = -1;
    if(toRevMax == "" or toRevMax is None):
        toRevMax = -1;
    eCountMin = float(eCountMin)
    eCountMax = float(eCountMax)
    stCountMin = float(stCountMin)
    stCountMax = float(stCountMax)
    toVisMin = float(toVisMin)
    toVisMax = float(tovisMax)
    toRevMin = float(toRevMin)
    toRevMax = float(toRevMax)

    query = """
        SELECT B.ReportDate, B.TotalVisits
        FROM (
            SELECT ReportDate, SUM(Visits) AS TotalVisits
            FROM (
                SELECT VisitSiteDate AS ReportDate, COUNT(*) AS Visits
                FROM visitsite
                WHERE SiteName = '%s'
                GROUP BY VisitSiteDate

                UNION

                SELECT VisitEventDate AS ReportDate, COUNT(*) AS Visits
                FROM visitevent
                WHERE SiteName = '%s'
                GROUP BY VisitEventDate
            ) AS A
            GROUP BY ReportDate
        ) AS B
        ON B.VisitEventDate = A.VisitSiteDate
        INNER JOIN (
            SELECT EventName, StartDate, EndDate, COUNT()
            FROM event
            WHERE SiteName = '%s'
        )
        """

def getManagersSite(manager):
    query = """
        SELECT SiteName
        FROM site
        WHERE ManagerUsername = '%s'
        """
    response = _cursor.execute(query % (manager))
    return (_cursor.fetchone())[0]

def getEvents25(site, ename, descr, sdate, edate, mindur, maxdur, minvis, maxvis, minrev, maxrev, sort):
    if(ename == "" or ename is None):
        ename = "-ALL-"
    if(descr == "" or descr is None):
        descr = "-ALL-"
    if(sdate == "" or sdate is None):
        sdate = "-ALL-"
    if(edate == "" or edate is None):
        edate = "-ALL-"
    if(mindur == "" or mindur is None):
        mindur = -1;
    if(maxdur == "" or maxdur is None):
        maxdur = -1;
    if(minvis == "" or minvis is None):
        minvis = -1;
    if(maxvis == "" or maxvis is None):
        maxvis = -1;
    if(minrev == "" or minrev is None):
        minrev = -1;
    if(maxrev == "" or maxrev is None):
        maxrev = -1;
    if(sort == "" or sort is None):
        sort = "EventName ASC"
    mindur = int(mindur)
    maxdur = int(maxdur)
    minvis = int(minvis)
    maxvis = int(maxvis)
    minrev = int(minrev)
    maxrev = int(maxrev)
    query = """
        SELECT EventName, StaffCount, Duration, TotalVisits, TotalRevenue, StartDate
        FROM (
            SELECT E.EventName, E.StaffCount, E.StartDate, E.Duration, E.TotalVisits, (E.EventPrice*E.TotalVisits) AS TotalRevenue
            FROM (
                SELECT A.EventName, A.StartDate, A.SiteName, A.Duration, A.EventPrice, A.StaffCount, D.TotalVisits, A.Description, A.EndDate
                FROM (
                    SELECT C.EventName, C.StartDate, C.EndDate, C.SiteName, (DATEDIFF(C.EndDate, C.StartDate) + 1) AS Duration, C.EventPrice, B.StaffCount, C.Description
                    FROM event AS C
                    INNER JOIN (
                        SELECT EventName, StartDate, SiteName, COUNT(*) As StaffCount
                        FROM assignto
                        GROUP BY EventName, StartDate, SiteName
                    ) AS B
                    ON C.EventName = B.EventName
                    WHERE C.StartDate = B.StartDate
                    AND C.SiteName = B.SiteName
                    AND C.SiteName = '%s'
                ) AS A
                INNER JOIN (
                    SELECT EventName, StartDate, SiteName, COUNT(*) AS TotalVisits
                    FROM visitevent
                    GROUP BY EventName, StartDate, SiteName

                    UNION

                    SELECT Y.EventName, Y.StartDate, Y.SiteName, 0 AS TotalVisits
                    FROM (
                        SELECT EventName, StartDate, SiteName
                        FROM event AS U
                        WHERE NOT EXISTS (
                            SELECT V.EventName, V.StartDate, V.SiteName
                            FROM visitevent AS V
                            WHERE U.EventName = V.EventName
                            AND U.StartDate = V.StartDate
                            AND U.SiteName = V.SiteName
                        )
                    ) AS Y
                ) AS D
                ON A.EventName = D.EventName
                WHERE A.StartDate = D.StartDate
                AND A.SiteName = D.SiteName
            ) AS E
            WHERE (LOCATE('%s',E.Eventname) > 0 OR '%s' = '-ALL-')
            AND (LOCATE('%s', E.Description) > 0 OR '%s' = '-ALL-')
            AND ('%s' = '-ALL-' OR DATEDIFF(E.EndDate, '%s') >= 0)
            AND ('%s' = '-ALL-' OR DATEDIFF('%s', E.StartDate) >= 0)
            AND (E.Duration >= %d OR %d = -1)
            AND (E.Duration <= %d OR %d = -1)
            AND (E.TotalVisits >= %d OR %d = -1)
            AND (E.TotalVisits <= %d OR %d = -1)
            AND ((E.EventPrice*E.TotalVisits) >= %d OR %d = -1)
            AND ((E.EventPrice*E.TotalVisits) <= %d OR %d = -1)
        ) AS Z
        ORDER BY %s
        """
    response = _cursor.execute(query % (site, ename, ename, descr, descr, sdate,
        sdate, edate, edate, mindur, mindur, maxdur, maxdur, minvis, minvis, maxvis,
        maxvis, minrev, minrev, maxrev, maxrev, sort));
    return _cursor.fetchall();

def getAllStaff():
    query = """
        SELECT Username
        FROM employee
        WHERE EmployeeType = 'Staff'
        """
    response = _cursor.execute(query)
    return _cursor.fetchall();

def getAvailableStaff(startDate, endDate):
    query = """
        SELECT DISTINCT StaffUsername
        FROM (
            SELECT A.StaffUsername, A.EventName, A.StartDate, A.SiteName, B.EndDate
            FROM assignto AS A
            INNER JOIN (
                SELECT EventName, StartDate, SiteName, EndDate
                FROM event
            ) AS B
            ON A.EventName = B.EventName
            WHERE A.StartDate = B.StartDate
            AND A.SiteName = B.SiteName
            AND (DATEDIFF(B.EndDate, '%s') > 0 OR DATEDIFF('%s', A.StartDate) > 0)
        ) AS C
        """
    response = _cursor.execute(query % (startDate, endDate))
    return _cursor.fetchall();

def addEvent(name, price, capacity, minstaff, stdate, enddate, description, selectedStaff, site):
    query0 = """
        INSERT INTO event
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
    response0 = _cursor.execute(query0, (name, stdate, site, enddate, price, capacity, minstaff, description));
    _database.commit();

    query1 = """
        INSERT INTO assignto
        VALUES (%s, %s, %s, %s)
        """
    for staff in selectedStaff:
        response1 = _cursor.execute(query1, (staff['Username'], name, stdate, site));
        _database.commit();

def deleteEvent(name, startDate, site):
    query0="""
        DELETE FROM event
        WHERE EventName = '%s'
        AND StartDate = '%s'
        AND SiteName = '%s'
        """
    response0 = _cursor.execute(query0 % (name, startDate, site))
    _database.commit();

    query1="""
        DELETE FROM visitevent
        WHERE EventName = '%s'
        AND StartDate = '%s'
        AND SiteName = '%s'
        """
    response1 = _cursor.execute(query1 % (name, startDate, site))
    _database.commit();

    query2="""
        DELETE FROM assignto
        WHERE EventName = '%s'
        AND StartDate = '%s'
        AND SiteName = '%s'
        """
    response2 = _cursor.execute(query2 % (name, startDate, site))
    _database.commit();

def getEventInfo(name, startDate, site):
    query = """
        SELECT EventName, DATE(StartDate), SiteName, DATE(EndDate), EventPrice, Capacity, MinStaffRequired, Description
        FROM event
        WHERE EventName = '%s'
        AND StartDate = '%s'
        AND SiteName = '%s'
        """
    response = _cursor.execute(query % (name, startDate, site))
    return _cursor.fetchone()

def getAssignedStaff(name, startdate, site):
    query = """
        SELECT StaffUsername
        FROM assignto
        WHERE EventName = '%s'
        AND StartDate = '%s'
        AND SiteName = '%s'
        """
    response = _cursor.execute(query % (name, startdate, site))
    return _cursor.fetchall();

def getDayInfo(name, startdate, site, minvis, maxvis, minrev, maxrev):
    if(minvis is None):
        minvis = -1
    if(maxvis is None):
        maxvis = -1
    if(minrev is None):
        minrev = -1
    if(maxrev is None):
        maxrev = -1
    query = """
        SELECT VisitEventDate, DailyVisits, DailyRevenue
        FROM (
            SELECT C.VisitEventDate, C.DailyVisits, (C.DailyVisits*D.EventPrice) AS DailyRevenue
            FROM (
            	SELECT A.VisitEventDate, A.EventName, A.StartDate, A.SiteName, B.DailyVisits
            	FROM (
            		SELECT DISTINCT VisitEventDate, EventName, StartDate, SiteName
            		FROM visitevent
            		WHERE EventName = '%s'
            		AND StartDate = '%s'
            		AND SiteName = '%s'
            	) AS A
            	INNER JOIN (
            		SELECT VisitEventDate, EventName, StartDate, SiteName, COUNT(*) AS DailyVisits
            		FROM visitevent
            		GROUP BY VisitEventDate, EventName, StartDate, SiteName
            	) AS B
            	ON A.EventName = B.EventName
            	WHERE A.StartDate = B.StartDate
            	AND A.SiteName = B.SiteName
                AND A.VisitEventDate = B.VisitEventDate
            ) AS C
            INNER JOIN (
            	SELECT EventName, StartDate, SiteName, EventPrice
            	FROM event
            ) AS D
            ON C.EventName = D.EventName
            WHERE C.StartDate = D.StartDate
            AND C.SiteName = D.SiteName
        ) AS E
        WHERE (DailyVisits >= %d OR %d = -1)
        AND (DailyVisits <= %d OR %d = -1)
        AND (DailyRevenue >= %d OR %d = -1)
        AND (DailyRevenue <= %d OR %d = -1)
        """
    response = _cursor.execute(query % (name, startdate, site, minvis, minvis, maxvis, maxvis,
            minrev, minrev, maxrev, maxrev))
    return _cursor.fetchall()

def updateEvent(eventname, startdate, site, description, assignedStaff):
    query0 = """
        UPDATE event
        SET Description = %s
        WHERE EventName = %s
        AND StartDate = %s
        AND SiteName = %s
        """
    response0 = _cursor.execute(query0, (description, eventname, startdate, site))
    _database.commit()

    query1 = """
        DELETE FROM assignto
        WHERE EventName = '%s'
        AND StartDate = '%s'
        AND SiteName = '%s'
        """
    response1 = _cursor.execute(query1 % (eventname, startdate, site))

    query2 = """
        INSERT INTO assignto
        VALUES (%s, %s, %s, %s)
        """
    for staff in assignedStaff:
        response2 = _cursor.execute(query2, (staff['Username'], eventname, startdate, site))
        _database.commit()

def getSiteReport(stDate, endDate, eCountMin, eCountMax, stCountMin, stCountMax,
        toVisMin, toVisMax, toRevMin, toRevMax, site, sort):
    if(eCountMin == "" or eCountMin is None):
        eCountMin = -1
    if(eCountMax == "" or eCountMax is None):
        eCountMax = -1
    if(stCountMin == "" or stCountMin is None):
        stCountMin = -1
    if(stCountMax == "" or stCountMax is None):
        stCountMax = -1
    if(toVisMin == "" or toVisMin is None):
        toVisMin = -1
    if(toVisMax == "" or toVisMax is None):
        toVisMin = -1
    if(toRevMin == "" or toRevMin is None):
        toRevMin = -1
    if(toRevMax == "" or toRevMax is None):
        toRevMax = -1
    if(sort == "" or sort is None):
        sort = "Day ASC"
    query = """
        SELECT *
        FROM (
            SELECT AE.Day, AE.EventCount, AE.StaffCount, AE.TotalVisits, AE.TotalRevenue
            FROM (
                SELECT D.Day, D.EventCount, M.TotalStaffCount AS StaffCount, AD.TotalVis AS TotalVisits, AD.TotalRev AS TotalRevenue
                FROM (
                	SELECT C.Day, Count(*) AS EventCount
                	FROM (
                		SELECT A.Day, B.EventName, B.StartDate, B.SiteName
                		FROM (
                			SELECT _date AS Day
                			FROM calendar
                			WHERE DATEDIFF(_date, '%s') >= 0
                			AND DATEDIFF(_date, '%s') <= 0
                		) AS A
                		INNER JOIN (
                			SELECT EventName, StartDate, EndDate, SiteName
                			FROM event
                            WHERE SiteName = '%s'
                		) AS B
                		ON DATEDIFF(A.Day, B.StartDate) >= 0
                		WHERE DATEDIFF(A.Day, B.EndDate) <= 0
                	) AS C
                	GROUP BY C.Day
                ) AS D
                INNER JOIN (
                	SELECT L.Day, SUM(StaffCount) AS TotalStaffCount
                    FROM (
                		SELECT J.Day, J.EventName, J.StartDate, J.SiteName, K.StaffCount
                		FROM (
                			SELECT E.Day, F.EventName, F.StartDate, F.SiteName
                			FROM (
                				SELECT _date AS Day
                				FROM calendar
                				WHERE DATEDIFF(_date, '%s') >= 0
                				AND DATEDIFF(_date, '%s') <= 0
                			) AS E
                			INNER JOIN (
                				SELECT EventName, StartDate, EndDate, SiteName
                				FROM event
                                WHERE SiteName = '%s'
                			) AS F
                			ON DATEDIFF(E.Day, F.StartDate) >= 0
                			WHERE DATEDIFF(E.Day, F.EndDate) <= 0
                		) AS J
                		INNER JOIN (
                			SELECT EventName, StartDate, SiteName, COUNT(*) AS StaffCount
                			FROM assignto
                			GROUP BY EventName, StartDate, SiteName
                		) AS K
                		ON J.EventName = K.EventName
                		WHERE J.StartDate = K.StartDate
                		AND J.SiteName = K.SiteName
                	) AS L
                    GROUP BY L.Day
                ) AS M
                ON M.Day = D.Day
                INNER JOIN (
                	SELECT AC.Day, SUM(TotalVisits) AS TotalVis, SUM(TotalRevenue) AS TotalRev
                	FROM (
                		SELECT AB.Day, AB.TotalVisits, AB.TotalRevenue
                		FROM (
                			SELECT P.Day, Q.TotalVisits, Q.TotalRevenue
                			FROM (
                				SELECT _date AS Day
                				FROM calendar
                				WHERE DATEDIFF(_date, '%s') >= 0
                				AND DATEDIFF(_date, '%s') <= 0
                			) AS P
                			INNER JOIN (
                				SELECT T.VisitEventDate, SUM(T.VisitValue) AS TotalVisits, Sum(T.EventPrice) AS TotalRevenue
                				FROM (
                					SELECT R.VisitEventDate, R.EventName, R.StartDate, R.SiteName, S.VisitValue, S.EventPrice
                					FROM visitevent AS R
                					INNER JOIN (
                						SELECT EventName, StartDate, SiteName, EventPrice, 1 AS VisitValue
                						FROM event
                						WHERE SiteName = '%s'
                					) AS S
                					WHERE S.EventName = R.EventName
                					AND S.StartDate = R.StartDate
                					AND S.SiteName = R.SiteName
                				) AS T
                				GROUP BY T.VisitEventDate
                			) AS Q
                			ON P.Day = Q.VisitEventDate
                		) AS AB

                		UNION

                		SELECT AA.Day, 0 AS TotalVisits, 0 AS TotalRevenue
                		FROM (
                			SELECT _date AS Day
                			FROM calendar
                			WHERE DATEDIFF(_date, '%s') >= 0
                			AND DATEDIFF(_date, '%s') <= 0
                		) AS AA
                	) AS AC
                	GROUP BY AC.Day
                ) AS AD
                ON AD.Day = D.Day
            ) AS AE
            WHERE (AE.EventCount >= %d OR %d = -1)
            AND (AE.EventCount <= %d OR %d = -1)
            AND (AE.StaffCount >= %d OR %d = -1)
            AND (AE.StaffCount <= %d OR %d = -1)
            AND (AE.TotalVisits >= %d OR %d = -1)
            AND (AE.TotalVisits <= %d OR %d = -1)
            AND (AE.TotalRevenue >= %d OR %d = -1)
            AND (AE.TotalRevenue <= %d OR %d = -1)
        ) AS AF
        ORDER BY %s
        """
    response = _cursor.execute(query % (stDate, endDate, site, stDate, endDate, site,
            stDate, endDate, site, stDate, endDate, eCountMin, eCountMin, eCountMax,
            eCountMax, stCountMin, stCountMin, stCountMax, stCountMax, toVisMin,
            toVisMin, toVisMax, toVisMax, toRevMin, toRevMin, toRevMax, toRevMax, sort));
    return _cursor.fetchall();

def getDailyDetail(site, date, sort):
    if(sort == "" or sort is None):
        sort = "EventName ASC"
    query = """
        SELECT G.EventName, G.StaffNames, G.Visits, (G.EventPrice*G.Visits) AS Revenue
        FROM (
            SELECT F.EventName, F.StartDate, F.SiteName, F.StaffNames, SUM(F.VisitorValue) AS Visits, F.EventPrice
            FROM (
            	SELECT D.EventName, D.StartDate, D.SiteName, D.StaffNames, E.VisitorValue, D.EventPrice
            	FROM (
            		SELECT C.EventName, C.StartDate, C.SiteName, C.EventPrice, GROUP_CONCAT(C.StaffUsername SEPARATOR '\n') AS StaffNames
            		FROM (
            			SELECT A.EventName, A.StartDate, A.SiteName, B.StaffUsername, A.EventPrice
            			FROM (
            				SELECT EventName, StartDate, SiteName, EventPrice
            				FROM event
            				WHERE DATEDIFF(StartDate, '%s') <= 0
            				AND DATEDIFF(EndDate, '%s') >= 0
            				AND SiteName = '%s'
            			) AS A
            			INNER JOIN (
            				SELECT *
            				FROM assignto
            			) AS B
            			ON A.EventName = B.EventName
            			WHERE A.StartDate = B.StartDate
            			AND A.SiteName = B.SiteName
            		) AS C
            		GROUP BY C.EventName, C.StartDate, C.SiteName
            	) AS D
            	INNER JOIN (
            		SELECT EventName, StartDate, SiteName, 1 AS VisitorValue
            		FROM visitevent
            		WHERE VisitEventDate = '%s'

                    UNION

                    SELECT EventName, StartDate, SiteName, 0 AS VisitorValue
                    FROM event
            	) AS E
            	ON D.EventName = E.EventName
            	WHERE D.StartDate = E.StartDate
            	AND D.SiteName = E.SiteName
            ) AS F
            GROUP BY F.EventName, F.StartDate, F.SiteName
        ) AS G
        ORDER BY %s
        """
    #print(query % (date, date, site, date, sort))
    response = _cursor.execute(query % (date, date, site, date, sort))
    return _cursor.fetchall();







# DEPRECATED FUNCTIONS
# def getAllTransit():
#     queryTransit = """
#         SELECT T.TransitRoute, T.TransitType, T.TransitPrice, C.Count
#         FROM transit AS T
#         INNER JOIN (
#             SELECT TransitRoute, TransitType, Count(*) AS Count
#             FROM connect
#             GROUP BY TransitRoute, TransitType ) AS C
#         ON T.TransitType = C.TransitType
#         WHERE T.TransitRoute = C.TransitRoute
#         """
#     response = _cursor.execute(queryTransit)
#     return _cursor.fetchall()
#
# def getAllTransit2(user):
#     queryTransit = """
#         SELECT TransitDate, TransitRoute, TransitType, TransitPrice
#         FROM (
#             SELECT TT.Username, TT.TransitDate, TT.TransitRoute, TT.TransitType, T.TransitPrice
#             FROM taketransit AS TT
#             INNER JOIN (
#               	SELECT TransitType, TransitRoute, TransitPrice
#                 FROM transit ) AS T
#             ON TT.TransitType = T.TransitType
#             WHERE TT.TransitRoute = T.TransitRoute
#         ) AS A
#         WHERE A.Username = '%s';
#         """
#     response = _cursor.execute(queryTransit % (user))
#     return _cursor.fetchall();

# def getAllSites():
#     query = """
#         SELECT SiteName, ManagerUsername, OpenEveryday
#         FROM site;
#         """
#     response = _cursor.execute(query)
#     return _cursor.fetchall();

# def getAllUsersList():
#     query = """
#         SELECT U.Username, Email.Count, U.UserType, U.Status
#         FROM allusers AS U
#         INNER JOIN (
#           	SELECT DISTINCT Username, COUNT(Username) AS Count
#             FROM useremail
#             GROUP BY Username
#         ) As Email
#         ON U.Username = Email.Username;
#         """
#     response = _cursor.execute(query)
#     return _cursor.fetchall();







    #bottom
