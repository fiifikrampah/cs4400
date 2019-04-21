# This app connects the html render templates to the flask app
from api import *
from database import *
from flask import Flask, render_template, json, request, Response
from decimal import Decimal

app = Flask(__name__)
# _logged_user = "david.smith"
# _logged_userType = "Manager"
_logged_user = "michael.smith"
_logged_userType = "Staff, Visitor"

@app.route('/')
def main():
    """
    Starts app at login screen
    """
    set_connection()

    #return to_user_take_transit();
    #return to_user_transit_history();
    #return to_manage_profile();
    #return manage_user();
    #return manage_site();
    #return create_site();
    #return manage_transit();
    #return create_transit();
    #return manage_event();
    #return to_manage_event();
    #return create_event()
    #return to_view_site_report()

    #return to_view_schedule()
    # return to_vis_explore_event()

    # return to_view_schedule()

    return render_template('1-login.html', error = "")

@app.route("/to_register_navigation")
def to_register_navigation():
    """
    Takes user to register navigation page
    """
    return render_template('2-registernavigation.html', error="")

@app.route("/to_user_register")
def to_user_register():
    """
    Takes user to user register page
    """
    return render_template('3-reguseronly.html', error="")

@app.route("/register_user", methods = ['POST'])
def register_user():
    print "Starting user register functionality"
    if request.method == 'POST':
        Username = request.form["username"]
        Password = request.form["password"]
        Status = 'Pending'
        Firstname = request.form["firstname"]
        Lastname = request.form["lastname"]
        UserType = 'User'
        confirmed_pass = request.form["confirm_password"]

        # email = request.form["email"]



        # if constraint_email_format(email) == 0:
        #     return render_template("3-reguseronly.html", error="Email does not match format!")
        if constraint_username_format(Username) == 0:
            return render_template("3-reguseronly.html", error="Username does not meet requirement!")

        error = ""
        if Password != confirmed_pass:
            return render_template("3-reguseronly.html", error="Passwords do not match!")
        elif constraint_password_format(Password) == 0:
            return render_template("3-reguseronly.html", error="Passwords do not meet requirement!")
        else:
            result = validate_user_registration(Username, Password, Status, Firstname, Lastname, UserType)
            #successful validation
            if result == 0:
                return render_template("1-login.html", error="")
            elif result == 1:
                return render_template("3-reguseronly.html", error="Username has already been taken")
            elif result == 2:
                return render_template("3-reguseronly.html", error="Cannot register, try again")

@app.route("/to_visitor_register")
def to_visitor_register():
    """
    Takes user to visitor register page
    """
    return render_template('4-regvisit.html', error="")

@app.route("/register_visitor", methods = ['POST'])
def register_visitor():
    print "Starting visitor register functionality"
    if request.method == 'POST':
        Username = request.form["username"]
        Password = request.form["password"]
        Status = 'Pending'
        Firstname = request.form["firstname"]
        Lastname = request.form["lastname"]
        UserType = 'Visitor'
        confirmed_pass = request.form["confirm_password"]
        email = request.form["email"]



        if constraint_email_format(email) == 0:
            return render_template("4-regvisit.html", error="Email does not match format!")
        if constraint_username_format(Username) == 0:
            return render_template("4-regvisit.html", error="Username does not meet requirement!")

        error = ""
        if Password != confirmed_pass:
            return render_template("4-regvisit.html", error="Passwords do not match!")
        elif constraint_password_format(Password) == 0:
            return render_template("4-regvisit.html", error="Passwords do not meet requirement!")
        else:
            result = validate_user_registration(Username, Password, Status, Firstname, Lastname, UserType)
            #successful validation
            if result == 0:
                return render_template("1-login.html", error="")
            elif result == 1:
                return render_template("4-regvisit.html", error="Username has already been taken")
            elif result == 2:
                return render_template("4-regvisit.html", error="Cannot register, try again")

@app.route("/to_employee_register")
def to_employee_register():
    """
    Takes user to employee register page
    """
    return render_template('5-regemp.html', error="")

@app.route("/register_employee", methods = ['POST'])
def register_employee():
    print "Starting employee register functionality"
    if request.method == 'POST':
        Username = request.form["username"]
        Password = request.form["password"]
        EmployeeID = None
        Phone = request.form["phone"]
        EmployeeAddress = request.form["address"]
        EmployeeCity = request.form["city"]
        EmployeeState= request.form.get("state")
        EmployeeZipcode = request.form["zipcode"]
        EmployeeType = request.form.get("usertype")
        Firstname = request.form["firstname"]
        Lastname = request.form["lastname"]
        UserType = 'Employee'
        Status = 'Pending'
        confirmed_pass = request.form["confirm_password"]
        email = request.form["email"]



        if constraint_email_format(email) == 0:
            return render_template("5-regemp.html", error="Email does not match format!")
        if constraint_username_format(Username) == 0:
            return render_template("5-regemp.html", error="Username does not meet requirement!")

        error = ""
        if Password != confirmed_pass:
            return render_template("5-regemp.html", error="Passwords do not match!")
        elif constraint_password_format(Password) == 0:
            return render_template("5-regemp.html", error="Passwords do not meet requirement!")
        else:
            result1 = validate_user_registration(Username, Password, Status, Firstname, Lastname, UserType)
            # result2 = validate_employee_registration(Username, EmployeeID, Phone, EmployeeAddress, EmployeeCity, EmployeeState, EmployeeZipcode, EmployeeType)
            #successful validation
            if result1 == 0:
                result2 = validate_employee_registration(Username, EmployeeID, Phone, EmployeeAddress, EmployeeCity, EmployeeState, EmployeeZipcode, EmployeeType)
                if result2 == 0:
                    return render_template("1-login.html", error="")
                elif result2 == 1:
                    return render_template("5-regemp.html", error="Someone already registered that phone number. Try a different one.")

            elif result1 == 1:
                return render_template("5-regemp.html", error="Username has already been taken")

            else:
                return render_template("5-regemp.html", error="Cannot register, try again")

@app.route("/to_emp_visitor_register")
def to_emp_visitor_register():
    """
    Takes user to employee-visitor register page
    """
    return render_template('6-regempvisit.html', error="")

@app.route("/register_employee_visitor", methods = ['POST'])
def register_employee_visitor():
    print "Starting employee visitor register functionality"
    if request.method == 'POST':
        Username = request.form["username"]
        Password = request.form["password"]
        EmployeeID = None
        Phone = request.form["phone"]
        EmployeeAddress = request.form["address"]
        EmployeeCity = request.form["city"]
        EmployeeState= request.form.get("state")
        EmployeeZipcode = request.form["zipcode"]
        EmployeeType = request.form.get("usertype")
        Firstname = request.form["firstname"]
        Lastname = request.form["lastname"]
        UserType = 'Employee'
        Status = 'Pending'
        confirmed_pass = request.form["confirm_password"]
        email = request.form["email"]



        if constraint_email_format(email) == 0:
            return render_template("6-regempvisit.html", error="Email does not match format!")
        if constraint_username_format(Username) == 0:
            return render_template("6-regempvisit.html", error="Username does not meet requirement!")

        error = ""
        if Password != confirmed_pass:
            return render_template("6-regempvisit.html", error="Passwords do not match!")
        elif constraint_password_format(Password) == 0:
            return render_template("6-regempvisit.html", error="Passwords do not meet requirement!")
        else:
            result1 = validate_user_registration(Username, Password, Status, Firstname, Lastname, UserType)
            # result2 = validate_employee_registration(Username, EmployeeID, Phone, EmployeeAddress, EmployeeCity, EmployeeState, EmployeeZipcode, EmployeeType)
            #successful validation
            if result1 == 0:
                result2 = validate_employee_registration(Username, EmployeeID, Phone, EmployeeAddress, EmployeeCity, EmployeeState, EmployeeZipcode, EmployeeType)
                if result2 == 0:
                    return render_template("1-login.html", error="")
                elif result2 == 1:
                    return render_template("6-regempvisit.html", error="Someone already registered that phone number. Try a different one.")

            elif result1 == 1:
                return render_template("6-regempvisit.html", error="Username has already been taken")

            else:
                return render_template("6-regempvisit.html", error="Cannot register, try again")

@app.route("/to_login")
def to_login():
    """
    Takes user to login page after they click on sign out
    """
    global _logged_user
    _logged_user = ""
    return render_template("1-login.html", error = "")

# This function signs the user in with given credentials
# to the correct page based on their account type.
# Makes call to python wrapper, and logs user in
# or displays appropriate error message

#read the posted values from the UI:
@app.route("/sign_in", methods =['POST', 'GET'])
def sign_in():
    if request.method == 'POST':
        _name = request.form["username"]
        _password = request.form["password"]
        # hash_password() --deprecated function
    	login_response = login(_name, _password)

    	if login_response == 0:
            global _logged_user
            _logged_user = ""
            return render_template("1-login.html", error = "Cannot login, try again.")
        else:
            if login_response in ['User']:
                _logged_user = _name
                _logged_userType = login_response
                print "The username of the logged user is: %s and his type is: %s" % (_logged_user,_logged_userType)
                return render_template("7-userfunc.html", error = "")
            elif login_response in ['Visitor']:
                _logged_user = _name
                _logged_userType = login_response
                print "The username of the logged user is: %s and his type is: %s" % (_logged_user,_logged_userType)
                return render_template("14-visitorfunc.html", error = "")

            elif login_response in ['Employee, Visitor']:
                emp_type = emptype_checker(_name)
                _logged_userType = emp_type

                if _logged_userType in ['Admin']:
                    _logged_user = _name
                    print "The username of the logged user is: %s and his type is: %s" % (_logged_user,_logged_userType)
                    return render_template("9-adminvisitfunc.html", error = "")

                elif _logged_userType in ['Manager']:
                    _logged_user = _name
                    print "The username of the logged user is: %s and his type is: %s" % (_logged_user,_logged_userType)
                    return render_template("11-manvisitfunc.html", error = "")

                elif _logged_userType in ['Staff']:
                    _logged_user = _name
                    print "The username of the logged user is: %s and his type is: %s" % (_logged_user,_logged_userType)
                    return render_template("13-staffvisitfunc.html", error = "")


            elif login_response in ['Employee']:
                emp_type = emptype_checker(_name)
                _logged_userType = emp_type

                if _logged_userType in ['Admin']:
                    _logged_user = _name
                    print "The username of the logged user is: %s and his type is: %s" % (_logged_user,_logged_userType)
                    return render_template("8-adminfunc.html", error = "")
               
                elif _logged_userType in ['Manager']:
                    _logged_user = _name
                    print "The username of the logged user is: %s and his type is: %s" % (_logged_user,_logged_userType)
                    return render_template("10-manfunc.html", error = "")
               
                elif _logged_userType in ['Staff']:
                    _logged_user = _name
                    print "logged person is: %s" % _logged_user
                    print "The username of the logged user is: %s and his type is: %s" % (_logged_user,_logged_userType)
                    return render_template("12-stafffunc.html", error = "")
                
                else:
                    _logged_user = ""
                    return render_template("1-login.html", error = "Username or password is incorrect, please try again.")

            else:
                _logged_user = ""
                _logged_userType = ""
                return render_template("1-login.html", error = "Cannot login, try again.")


@app.route("/back-button", methods = ['GET'])
def go_to_functionality_screen():
    if request.method == 'GET':

        global _logged_user
        person = _logged_user
        print(person)
        p_type = usertype_checker(_logged_user)
        print(p_type)

        if p_type in ['Employee', 'Employee, Visitor']:
            emp_type = emptype_checker(_logged_user)
            if emp_type in ['Admin']:
                return render_template("8-adminfunc.html", error = "")
            elif emp_type in ['Admin, Visitor']:
                return render_template("9-adminvisitfunc.html", error = "")
            elif emp_type in ['Manager']:
                return render_template("10-manfunc.html", error = "")
            elif emp_type in ['Manager, Visitor']:
                return render_template("11-manvisitfunc.html", error = "")
            elif emp_type in ['Staff']:
                return render_template("12-stafffunc.html", error = "")
            elif emp_type in ['Staff, Visitor']:
                return render_template("13-staffvisitfunc.html", error = "")

        elif p_type in ['User']:

            return render_template("7-userfunc.html", error = "")
        elif p_type in ['Visitor']:
            return render_template("14-visitorfunc.html", error = "")

@app.route("/to_visitor_explore_event")
def to_visitor_explore_event():
    """
    Takes user to explore event page
    """
    return render_template('33-visitorexploreevent.html', error="")

@app.route("/to_visitor_explore_site")
def to_visitor_explore_site():
    """
    Takes user to explore site page
    """
    return render_template('35-visitorexploresite.html', error="")

@app.route("/to_visitor_view_visit_history")
def to_visitor_view_visit_history():
    """
    Takes user to view visit history page
    """
    return render_template('38-visitorexploresite.html', error="")



#SCREEN 15
@app.route("/to_user_take_transit", methods=['POST', 'GET'])
def to_user_take_transit():
    # getting the sites for the dropdown
    response = getSiteNames()
    siteList = []
    for item in response:
        site={}
        site['SiteName'] = item[0]
        siteList.append(site)

    # getting the transit types for the dropdown
    response = getTransitTypes()
    transitTypeList = []
    for item in response:
        tType={}
        tType['TransitType'] = item[0]
        transitTypeList.append(tType)

    if request.method == 'GET':
        # getting unfiltered transit when the page is first loaded, with default sort
        response = getTransit15(None, None, None, None, None)
        transitList = []
        for item in response:
            transit={}
            transit['TransitRoute'] = item[0]
            transit['TransitType'] = item[1]
            transit['Price'] = item[2];
            transit['ConnectedSites'] = item[3]
            transitList.append(transit);

        return render_template('15-usertaketransit.html', sites=siteList, types=transitTypeList,
                transits=transitList, filSite="-ALL-", filType="-ALL-", filMinPr=-1, filMaxPr=-1)

    if request.method == 'POST':
        #getting filtered transit when some of the options have been played with
        site = request.form["site"]
        transitType = request.form["transittype"]
        minPrice = request.form["minPrice"]
        maxPrice = request.form["maxPrice"]
        sort = ""
        try:
            sort = request.form["sort"]
        except:
            sort = None

        if(minPrice == ""):
            minPrice = -1
        if(maxPrice == ""):
            maxPrice = -1
        minPrice = float(minPrice)
        maxPrice = float(maxPrice)

        response = getTransit15(site, transitType, minPrice, maxPrice, sort)
        transitList = []
        for item in response:
            transit={}
            transit['TransitRoute'] = item[0]
            transit['TransitType'] = item[1]
            transit['Price'] = item[2];
            transit['ConnectedSites'] = item[3]
            transitList.append(transit);

        return render_template('15-usertaketransit.html', sites=siteList, types=transitTypeList,
                transits=transitList, filSite=site, filType=transitType, filMinPr=minPrice, filMaxPr=maxPrice)

@app.route("/user_log_transit", methods=['POST'])
def log_transit():
    transit = request.form["chosen_transit"]
    date = request.form["dateLogged"]

    global _logged_user
    logTransit(_logged_user, transit, date)

    # getting the sites for the dropdown
    response = getSiteNames()
    siteList = []
    for item in response:
        site={}
        site['SiteName'] = item[0]
        siteList.append(site)

    # getting the transit types for the dropdown
    response = getTransitTypes()
    transitTypeList = []
    for item in response:
        tType={}
        tType['TransitType'] = item[0]
        transitTypeList.append(tType)

    # getting unfiltered transit when the page is first loaded, with default sort
    response = getTransit15(None, None, None, None, None)
    transitList = []
    for item in response:
        transit={}
        transit['TransitRoute'] = item[0]
        transit['TransitType'] = item[1]
        transit['Price'] = item[2];
        transit['ConnectedSites'] = item[3]
        transitList.append(transit);

    return render_template('15-usertaketransit.html', sites=siteList, types=transitTypeList,
            transits=transitList, filSite="-ALL-", filType="-ALL-", filMinPr=-1, filMaxPr=-1)



#SCREEN 16
@app.route("/to_user_transit_history", methods=['POST', 'GET'])
def to_user_transit_history():
    # getting the sites for the dropdown
    response = getSiteNames()
    siteList = []
    for item in response:
        site={}
        site['SiteName'] = item[0]
        siteList.append(site)

    # getting the transit types for the dropdown
    response = getTransitTypes()
    transitTypeList = []
    for item in response:
        tType={}
        tType['TransitType'] = item[0]
        transitTypeList.append(tType)

    if request.method == 'GET':
        # getting unfiltered transit when the page is first loaded
        global _logged_user
        response = getTransit16(_logged_user, None, None, None, None, None, None)

        transitList = []
        for item in response:
            transit={}
            transit['Date'] = item[0]
            transit['TransitRoute'] = item[1]
            transit['TransitType'] = item[2];
            transit['TransitPrice'] = item[3]
            transitList.append(transit);

        return render_template('16-usertranshistory.html', sites=siteList, types=transitTypeList,
                transits=transitList, filSite="-ALL-", filType="-ALL-", filRoute="", filStDate="", filEndDate="")

    if request.method == 'POST':
        #getting filtered transit when some of the options have been played with
        site = request.form["site"]
        transitType = request.form["transittype"]
        route = request.form["route"]
        startDate = request.form["startdate"]
        endDate = request.form["enddate"]
        sort = ""
        try:
            sort = request.form["sort"]
        except:
            sort = None

        # global _logged_user
        response = getTransit16(_logged_user, site, transitType, route, startDate, endDate, sort)

        transitList = []
        for item in response:
            transit={}
            transit['Date'] = item[0]
            transit['TransitRoute'] = item[1]
            transit['TransitType'] = item[2];
            transit['TransitPrice'] = item[3]
            transitList.append(transit);

        return render_template('16-usertranshistory.html', sites=siteList, types=transitTypeList,
                transits=transitList, filSite=site, filType=transitType, filRoute="", filStDate=startDate,
                filEndDate=endDate)



#SCREEN 17
@app.route("/to_manage_profile", methods=['POST', 'GET'])
def to_manage_profile():
    if request.method == 'GET':
        #getting info to populate the screen with
        global _logged_user

        global _logged_userType

        _logged_userType = get_usertype(_logged_user)
        print "FIIFI THE GUY IS: %s AND HIS USER IS: %s" % (_logged_userType, _logged_user)

        info = get_employee_info(_logged_user)
        fname = info[0]
        lname = info[1]
        uname = info[2]
        sname = info[3]
        eid = info[4]
        phone = info[5]
        address = info[6] + ", " + info[7] + ", " + info[8] + " " + str(info[9])

        visitor = "0"
        if('Visitor' in _logged_userType):
            visitor = "1"

        response = get_employee_emails(_logged_user)
        emails = []
        for item in response:
            email = {}
            email['Email'] = item[0]
            emails.append(email)

        return render_template('17-empmanageprofile.html', fname=fname, lname=lname, uname=uname,
                sname=sname, eid=eid, phone=phone, newemail="", address=address, visitor=visitor, emails=emails)

    if request.method == 'POST':
        # updating info
        fname = request.form["firstname"];
        lname = request.form["lastname"];
        phone = request.form["phonenum"];
        visitor = request.form["isvisitor"];
        newemail = request.form["addemail"]

        update_employee(_logged_user, fname, lname, phone, visitor)

        # rendering screen again
        global _logged_user
        info = get_employee_info(_logged_user)
        uname = info[2]
        sname = info[3]
        eid = info[4]
        address = info[6] + ", " + info[7] + ", " + info[8] + " " + str(info[9])

        response = get_employee_emails(_logged_user)
        emails = []
        for item in response:
            email = {}
            email['Email'] = item[0]
            emails.append(email)

        return render_template('17-empmanageprofile.html', fname=fname, lname=lname, uname=uname,
                sname=sname, eid=eid, phone=phone, address=address, visitor=visitor, emails=emails,
                newemail=newemail)

@app.route("/remove_email", methods=['POST'])
def delete_email():
    email = request.form["rememail"];
    deleteEmail(email);

    # rendering fresh screen
    # updating info
    fname = request.form["firstname"];
    lname = request.form["lastname"];
    phone = request.form["phonenum"];
    visitor = request.form["isvisitor"];
    newemail = request.form["addemail"]


    # rendering screen again
    global _logged_user
    info = get_employee_info(_logged_user)
    uname = info[2]
    sname = info[3]
    eid = info[4]
    address = info[6] + ", " + info[7] + ", " + info[8] + " " + str(info[9])

    response = get_employee_emails(_logged_user)
    emails = []
    for item in response:
        email = {}
        email['Email'] = item[0]
        emails.append(email)

    return render_template('17-empmanageprofile.html', fname=fname, lname=lname, uname=uname,
            sname=sname, eid=eid, phone=phone, address=address, visitor=visitor, emails=emails,
            newemail=newemail)

@app.route("/add-email", methods=['POST'])
def addEmail():
    email = request.form["addemail"];

    global _logged_user
    email_insert(_logged_user, email)

    # getting screen back
    # updating info
    fname = request.form["firstname"];
    lname = request.form["lastname"];
    phone = request.form["phonenum"];
    visitor = request.form["isvisitor"];

    # rendering screen again
    global _logged_user
    info = get_employee_info(_logged_user)
    uname = info[2]
    sname = info[3]
    eid = info[4]
    address = info[6] + ", " + info[7] + ", " + info[8] + " " + str(info[9])

    response = get_employee_emails(_logged_user)
    emails = []
    for item in response:
        email = {}
        email['Email'] = item[0]
        emails.append(email)

    return render_template('17-empmanageprofile.html', fname=fname, lname=lname, uname=uname,
            sname=sname, eid=eid, phone=phone, newemail="", address=address, visitor=visitor, emails=emails)



#SCREEN 18
@app.route("/to_manage_user", methods=['POST', 'GET'])
def manage_user():
    if request.method == 'GET':
        response = getAllUsersList();

        userList=[]
        for item in response:
            user={}
            user['Username']=item[0]
            user['EmailCount']=item[1]
            user['Type']=item[2]
            user['Status']=item[3]
            userList.append(user)

        return render_template('18-adminmanuser.html', users=userList)

    if request.method == 'POST':
        username = request.form["username"]
        type = request.form["type"]
        status = request.form["status"]

        response = getFilteredUsersList(username, type, status)



#SCREENS 19-21
@app.route("/to_manage_site", methods=['POST', 'GET'])
def manage_site():
    response = getSiteNames();
    siteNameList = []
    for item in response:
        site={}
        site['SiteName'] = item[0]
        siteNameList.append(site)

    response = getManagerNames();
    managerList = []
    for item in response:
        manager={}
        manager['Username']=item[0]
        managerList.append(manager)

    if request.method == 'GET':
        response = getSites19(None, None, None, None);
        siteList = []
        for item in response:
            site={}
            site['Name']=item[0]
            site['Manager']=item[1]
            site['OpenEveryday']=item[2]
            siteList.append(site)

        return render_template('19-adminmansite.html', siteNames=siteNameList, managers=managerList,
                sites=siteList, filSite="-ALL-", filMan="-ALL-", filEvery="-ALL-")

    if request.method == 'POST':
        filsite = request.form["site"]
        manager = request.form["manager"]
        everyday = request.form["everyday"]
        sort = ""
        try:
            sort = request.form["sort"]
        except:
            sort = None

        response = getSites19(filsite, manager, everyday, sort)
        siteList = []
        for item in response:
            site={}
            site['Name']=item[0]
            site['Manager']=item[1]
            site['OpenEveryday']=item[2]
            siteList.append(site)

        return render_template('19-adminmansite.html', siteNames=siteNameList, managers=managerList,
                    sites=siteList, filSite=filsite, filMan=manager, filEvery=everyday)

@app.route("/to_edit_site", methods=['POST'])
def to_edit_site():
    sitename = request.form["chosen_site"]
    response = get_site_info(sitename);
    item = response[0]

    site = {}
    site['SiteName'] = item[0]
    site['SiteAddress'] = item[1]
    site['SiteZipcode'] = item[2]
    openeveryday = item[3]
    currentManager = item[4]

    managerList = []
    curmanager={}
    curmanager['Username'] = currentManager
    managerList.append(curmanager);

    response = getUnassignedManagers();
    for item in response:
        manager={}
        manager['Username']=item[0]
        managerList.append(manager)

    return render_template("20-admineditsite.html", site=site, managers=managerList, openeveryday=openeveryday,
            currentManager=currentManager, oldName=site['SiteName'])

@app.route("/edit_site", methods=['POST'])
def edit_site():
    oldname = request.form["oldname"]
    name = request.form["name"]
    zip = request.form["zipcode"]
    address = request.form["address"]
    manager = request.form["manager"]
    everyday = request.form["everyday"]

    update_site(oldname, name, zip, address, manager, everyday)

    # TODO handle errors
    # site={}
    # site['SiteName'] = name
    # site['SiteAddress'] = address
    # site['SiteZipcode'] = zip
    # return render_template("20-admineditsite.html", site=site, managers=managerList, openeveryday=everyday,
    #         currentManager=manager, oldName=oldname)

    return render_manage_sites()

def render_manage_sites():
    # sends back to the manage sites page
    response = getSiteNames();
    siteNameList = []
    for item in response:
        site={}
        site['SiteName'] = item[0]
        siteNameList.append(site)

    response = getManagerNames();
    managerList = []
    for item in response:
        manager={}
        manager['Username']=item[0]
        managerList.append(manager)

    response = getSites19(None, None, None, None)
    siteList = []
    for item in response:
        site={}
        site['Name']=item[0]
        site['Manager']=item[1]
        site['OpenEveryday']=item[2]
        siteList.append(site)

    return render_template('19-adminmansite.html', siteNames=siteNameList, managers=managerList,
            sites=siteList, filSite="-ALL-", filMan="-ALL-", filEvery="-ALL-")

@app.route("/to_create_site", methods=['POST', 'GET'])
def create_site():
    if request.method == 'GET':
        #gets managers who do not manage a site to populate managers list
        response = getUnassignedManagers();
        unassignedManagers = []
        for item in response:
            manager={}
            manager['Username']=item[0]
            unassignedManagers.append(manager);

        return render_template('21-admincreatesite.html', managers=unassignedManagers, filName="", filZip="",
                filAdd="", filMan="", filEvery="")

    if request.method == 'POST':
        #pulls the necessary information form the html form and adds to the database
        name = request.form["name"]
        zip = request.form["zipcode"]
        address = request.form["address"]
        mmanager = request.form["manager"]
        everyday = request.form["everyday"]

        add_site(name, address, zip, everyday, mmanager);

        # TODO implement error
        # #gets managers who do not manage a site to populate managers list
        # response = getUnassignedManagers();
        # unassignedManagers = []
        # for item in response:
        #     manager={}
        #     manager['Username']=item[0]
        #     unassignedManagers.append(manager);
        # return render_template('21-admincreatesite.html', managers=unassignedManagers, filName=name, filZip=zip
        #         filAdd=address, filMan=mmanager, filEvery=everyday)

        return render_manage_sites();

@app.route("/delete_site", methods=['POST'])
def delete_site():
    name = request.form["chosen_site"]

    removesite(name);

    return render_manage_sites();



#SCREENS 22-24
@app.route("/to_manage_transit", methods=['POST', 'GET'])
def manage_transit():
    # getting the sites for the dropdown
    response = getSiteNames()
    siteList = []
    for item in response:
        site={}
        site['SiteName'] = item[0]
        siteList.append(site)

    # getting the transit types for the dropdown
    response = getTransitTypes()
    transitTypeList = []
    for item in response:
        tType={}
        tType['TransitType'] = item[0]
        transitTypeList.append(tType)

    if request.method == 'GET':
        response = getTransit22(None, None, None, None, None, None);
        transitList=[]
        for item in response:
            transit = {}
            transit['TransitRoute'] = item[0]
            transit['TransitType'] = item[1]
            transit['TransitPrice'] = item[2]
            transit['ConnectedSites'] = item[3]
            transit['TransitLogged'] = item[4]
            transitList.append(transit)

        return render_template('22-adminmantransit.html', sites=siteList, types=transitTypeList, transits=transitList,
                filType="-ALL-", filSite="-ALL-", filRoute="", filMinPr=-1, filMaxPr=-1)

    if request.method == 'POST':
        site = request.form["site"]
        type = request.form["type"]
        route = request.form["route"]
        minPrice = request.form["minPrice"]
        maxPrice = request.form["maxPrice"]
        sort = ""
        try:
            sort = request.form["sort"]
        except:
            sort = None

        if(minPrice == ""):
            minPrice = -1
        if(maxPrice == ""):
            maxPrice = -1
        minPrice = float(minPrice)
        maxPrice = float(maxPrice)

        response = getTransit22(site, type, route, minPrice, maxPrice, sort);
        transitList=[]
        for item in response:
            transit = {}
            transit['TransitRoute'] = item[0]
            transit['TransitType'] = item[1]

            transit['TransitPrice'] = item[2]

            transit['ConnectedSites'] = item[3]
            transit['TransitLogged'] = item[4]
            transitList.append(transit)

        return render_template('22-adminmantransit.html', sites=siteList, types=transitTypeList, transits=transitList,
                filType=type, filSite=site, filRoute=route, filMinPr=minPrice, filMaxPr=maxPrice)

@app.route("/to_create_transit", methods=['POST', 'GET'])
def create_transit():
    response = getSiteNames();
    siteNameList = []
    for item in response:
        site={}
        site['SiteName'] = item[0]
        siteNameList.append(site)

    response = getTransitTypes()
    transitTypeList = []
    for item in response:
        tType={}
        tType['TransitType'] = item[0]
        transitTypeList.append(tType)

    if request.method == 'GET':
        return render_template("24-admincreatetransit.html", sites=siteNameList, types=transitTypeList,
                filType="", filRoute="", filPrice=-1, filSite=[])

    if request.method == 'POST':
        # TODO actually create the site
        type = request.form["type"]
        route = request.form["route"]
        price = request.form["price"]

        if(price == ""):
            price = -1
        price = float(price)

        # getting the sites for the dropdown
        response = getSiteNames()
        selectedSites = []
        siteList = []
        for item in response:
            site={}
            site['SiteName'] = item[0]
            siteList.append(site)

            #gets which sites were selected
            included = request.form[item[0]]
            if(included == "Yes"):
                selectedSites.append(site)

        createtransit(type, route, price, selectedSites)

        # TODO if it errors
        # return render_template("24-admincreatetransit.html", sites=siteNameList, types=transitTypeList,
        #         filType=type, filRoute=route, filPrice=price, filSite=selectedSites)

        # getting the transit types for the dropdown
        response = getTransitTypes()
        transitTypeList = []
        for item in response:
            tType={}
            tType['TransitType'] = item[0]
            transitTypeList.append(tType)

        response = getTransit22(None, None, None, None, None, None);
        transitList=[]
        for item in response:
            transit = {}
            transit['TransitRoute'] = item[0]
            transit['TransitType'] = item[1]
            transit['TransitPrice'] = item[2]
            transit['ConnectedSites'] = item[3]
            transit['TransitLogged'] = item[4]
            transitList.append(transit)

        return render_template('22-adminmantransit.html', sites=siteList, types=transitTypeList, transits=transitList,
                filType="-ALL-", filSite="-ALL-", filRoute="", filMinPr=-1, filMaxPr=-1)

@app.route("/to_edit_transit", methods=['POST'])
def to_edit_transit():
    transit = request.form["chosen_transit"]
    transit = transit.replace("{", "").replace("}", "")
    fields = transit.split(", ")

    route = ""
    ttype = ""
    price = -1.0

    for field in fields:
        if(len(field) >= 14 and field[0:14]=="'TransitRoute'"):
            strings = field.split(": ")
            route = strings[1][1:len(strings[1])-1]
        if(len(field) >= 13 and field[0:13]=="'TransitType'"):
            strings = field.split(": ")
            ttype = strings[1][1:len(strings[1])-1]
        if(len(field) >= 14 and field[0:14]=="'TransitPrice'"):
            strings = field.split(": ")
            price = float(strings[1][0:len(strings[1])])

    response = get_connected_sites(route, ttype)
    connectedSites = []
    for item in response:
        site = {}
        site['SiteName'] = item[0]
        connectedSites.append(site)

    response = getSiteNames()
    siteNameList = []
    for item in response:
        site={}
        site['SiteName'] = item[0]
        siteNameList.append(site)

    return render_template("23-adminedittransit.html", route=route, ttype=ttype, tprice=price,
            connectedSites=connectedSites, sites=siteNameList)

@app.route("/edit_transit", methods=['POST'])
def edit_transit():
    type = request.form["type"]
    oldroute = request.form["oldroute"]
    route = request.form["route"]
    price = request.form["price"]
    price = float(price)

    response = getSiteNames()
    siteList = []
    for item in response:
        site={}
        site['SiteName'] = item[0]
        siteList.append(site)

    connectedSites = []
    for site in siteList:
        selected = request.form[site['SiteName']]
        if(selected == "1"):
            connectedSites.append(site['SiteName'])

    change_transit_connections(type, oldroute, route, connectedSites)
    set_transit(type, oldroute, route, price)
    change_transit_history(type, oldroute, route)

    # TODO error handling
    # response = get_connected_sites(route, ttype)
    # connectedSites = []
    # for item in response:
    #     site = {}
    #     site['SiteName'] = item[0]
    #     connectedSites.append(site)
    #
    # response = getSiteNames()
    # siteNameList = []
    # for item in response:
    #     site={}
    #     site['SiteName'] = item[0]
    #     siteNameList.append(site)
    #
    # return render_template("23-adminedittransit.html", route=route, ttype=type, tprice=price,
    #         connectedSites=connectedSites, sites=siteNameList)

    return render_manage_transit();

@app.route("/delete_transit", methods=['POST'])
def delete_transit():
    transit = request.form["chosen_transit"]
    transit = transit.replace("{", "").replace("}", "")
    fields = transit.split(", ")

    route = ""
    ttype = ""

    for field in fields:
        if(len(field) >= 14 and field[0:14]=="'TransitRoute'"):
            strings = field.split(": ")
            route = strings[1][1:len(strings[1])-1]
        if(len(field) >= 13 and field[0:13]=="'TransitType'"):
            strings = field.split(": ")
            ttype = strings[1][1:len(strings[1])-1]

    deletetransit(ttype, route)

    return render_manage_transit()

def render_manage_transit():
    # getting the sites for the dropdown
    response = getSiteNames()
    siteList = []
    for item in response:
        site={}
        site['SiteName'] = item[0]
        siteList.append(site)

    # getting the transit types for the dropdown
    response = getTransitTypes()
    transitTypeList = []
    for item in response:
        tType={}
        tType['TransitType'] = item[0]
        transitTypeList.append(tType)

    response = getTransit22(None, None, None, None, None, None);
    transitList=[]
    for item in response:
        transit = {}
        transit['TransitRoute'] = item[0]
        transit['TransitType'] = item[1]
        transit['TransitPrice'] = item[2]
        transit['ConnectedSites'] = item[3]
        transit['TransitLogged'] = item[4]
        transitList.append(transit)

    return render_template('22-adminmantransit.html', sites=siteList, types=transitTypeList, transits=transitList,
            filType="-ALL-", filSite="-ALL-", filRoute="", filMinPr=-1, filMaxPr=-1)



#SCREENS 25-27
@app.route("/to_manage_event", methods=['POST', 'GET'])
def to_manage_event():
    if request.method == 'GET':
        global _logged_user
        site = getManagersSite(_logged_user)
        response = getEvents25(site, None, None, None, None, None, None, None, None, None, None, None)
        eventList = []
        for item in response:
            event={}
            event['EventName'] = item[0]
            event['StaffCount'] = item[1]
            event['Duration'] = item[2]
            event['TotalVisits'] = item[3]
            event['TotalRevenue'] = item[4]
            event['StartDate'] = item[5]
            eventList.append(event)

        return render_template("25-managermanevent.html", events=eventList, filName="", filKey="", filStDate="",
                filEndDate="", filDurMin=-1, filDurMax=-1, filVisMin=-1, filVisMax=-1,
                filRevMin=-1, filRevMax=-1)

    if request.method == 'POST':
        name = request.form["name"]
        descr = request.form["keyword"]
        startDate = request.form["startDate"]
        endDate = request.form["endDate"]
        mindur = request.form["durMin"]
        maxdur = request.form["durMax"]
        minvis = request.form["visMin"]
        maxvis = request.form["visMax"]
        minrev = request.form["revMin"]
        maxrev = request.form["revMax"]
        sort = ""
        try:
            sort = request.form["sort"]
        except:
            sort = None

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
        mindur = int(mindur)
        maxdur = int(maxdur)
        minvis = int(minvis)
        maxvis = int(maxvis)
        minrev = int(minrev)
        maxrev = int(maxrev)

        global _logged_user
        site = getManagersSite(_logged_user)
        response = getEvents25(site, name, descr, startDate, endDate, mindur, maxdur,
                minvis, maxvis, minrev, maxrev, sort)
        eventList = []
        for item in response:
            event={}
            event['EventName'] = item[0]
            event['StaffCount'] = item[1]
            event['Duration'] = item[2]
            event['TotalVisits'] = item[3]
            event['TotalRevenue'] = item[4]
            event['StartDate'] = item[5]
            eventList.append(event)

        return render_template("25-managermanevent.html", events=eventList, filName=name,
                filKey=descr, filStDate=startDate, filEndDate=endDate, filDurMin=mindur,
                filDurMax=maxdur, filVisMin=minvis, filVisMax=maxvis,
                filRevMin=minrev, filRevMax=maxrev)





# Screen 28
@app.route("/to_view_staff", methods=['POST', 'GET'])
def manageStaff():
    
     # getting the sites for the dropdown
    response = getSiteNames()
    siteList = []
    for item in response:
        site={}
        site['SiteName'] = item[0]
        siteList.append(site)

        site_name = []
    for val in siteList:
        site_name.append(val['SiteName'])

    firstSite = site_name[0]

    if request.method == 'GET':
        # getting unfiltered table when the page is first loaded
        # global _logged_user
        response =manageStaffers(firstSite, None, None, None, None, None)
        stafflist = []
        for item in response:
            staff={}
            staff['staffName'] = item[0]
            staff['EventShift'] = item[1]
            stafflist.append(staff);       
        return render_template("28-managermanstaff.html", sites=siteList, Firstname="",Lastname="",
            Startdate="", Enddate="", staffs=stafflist, filSite= "")
    if request.method =='POST':


        #getting filtered transit when some of the options have been played with
        site = request.form["site"]
        # print site
        Startdate = request.form["sdate"]
        Enddate = request.form["endate"]
        Firstname = request.form["fname"]
        Lastname = request.form["lname"]
        sort = ""
        try:
            sort = request.form["sort"]
        except:
            sort = None

        # global _logged_user
        response =manageStaffers(site,Firstname,Lastname, Startdate, Enddate, sort) 
        stafflist = []
        for item in response:
            staff={}
            staff['staffName'] = item[0]
            staff['EventShift'] = item[1]
            stafflist.append(staff)
        return render_template("28-managermanstaff.html", sites=siteList, Firstname=Firstname,Lastname=Lastname,
            Startdate=Startdate, Enddate=Enddate, filSite=site,staffs=stafflist)



#Screen32
@app.route("/to_staff_event_detail", methods=['GET'])
def eventDetails():
    if request.method == 'GET':

        # info1 = getEventDetail32("Bus Tour", "2019-02-01 00:00:00", "Inman Park")
        # info2 = getstaffDetail32("Bus Tour", "2019-02-01 00:00:00", "Inman Park")
        # info3 = getEventDate32("Bus Tour", "2019-02-01 00:00:00", "Inman Park")


        info1 = getEventDetail32(eventName, startDate, siteName)
        info2 = getstaffDetail32(eventName, startDate, siteName)
        info3 = getEventDate32(eventName, startDate, siteName)

       
        EventName = info1[0]
        StartDate = str(info1[1])[0:10]
        SiteName = info1[2]
        EndDate = str(info1[3])[0:10]
        EventPrice = info1[4]
        Capacity = info1[5]
        # MinStaffRequired = info1[6]
        Description = info1[7]

        staff = info2
        stafflist = []
        
        for list in staff:
            for item in list:
                stafflist.append(item)

        StaffUsername = ",\n".join(stafflist)
        Duration = info3

    return render_template("32-eventdetail.html", EventName=EventName, StartDate=StartDate,SiteName=SiteName, EndDate=EndDate,
        EventPrice=EventPrice, Capacity=Capacity,Description=Description,StaffUsername=StaffUsername,Duration=Duration)




# Screen 34
@app.route("/to_visitor_event_detail", methods=['GET'])
def visitor_eventDetails():
    if request.method == 'GET':
        # info1 = getEventDetail32("Bus Tour", "2019-02-01 00:00:00", "Inman Park")
        # info2 = getEventDetail32("Bus Tour", "2019-02-01 00:00:00", "Inman Park")
        # info3 = getEventDetail32("Bus Tour", "2019-02-01 00:00:00", "Inman Park")


        info1 = getEventDetail32(eventName, startDate, siteName)
        info2 = getstaffDetail32(eventName, startDate, siteName)
        info3 = getEventDate32(eventName, startDate, siteName)

       
        EventName = info1[0]
        StartDate = str(info1[1])[0:10]
        SiteName = info1[2]
        EndDate = str(info1[3])[0:10]
        price = info1[4]
        Description = info1[7]
        #FIX THIS USING PREVIOUS SCREEN:
        TicketRemaining = 0
                
    

    return render_template("34-viseventdetail.html", EventName=EventName, StartDate=StartDate,SiteName=SiteName,EndDate=EndDate,
        price=price,Description=Description,TicketRemaining=TicketRemaining)


@app.route("/visitor_logVisit", methods=[ 'POST'])
def visitor_logVisit():
    
    try:
        # info1 = getEventDetail32("Bus Tour", "2019-02-01 00:00:00", "Inman Park")
        info1 = getEventDetail32(eventName, startDate, siteName)
        EventName = info1[0]
        StartDate = str(info1[1])[0:10]
        SiteName = info1[2]
        EndDate = str(info1[3])[0:10]
        price = info1[4]
        Description = info1[7]
        #FIX THIS USING PREVIOUS SCREEN:
        TicketRemaining = 0
        VisitDate = request.form["visitdate"][0:10]

        global _logged_user
        print "THE VISITOR IS: %s" % _logged_user

        newstart = datetime.strptime(StartDate, '%Y-%m-%d').date()
        newend = datetime.strptime(EndDate, '%Y-%m-%d').date()
        newvisitdate = datetime.strptime(VisitDate, '%Y-%m-%d').date()
        # print newvisitdate

        # Visit date must be b/n start and end and Remaining tickets > 0:
        

        if (newstart <= newvisitdate) and  (newvisitdate <= newend) and TicketRemaining > 0 :
            result = logeventVisit(_logged_user, EventName, StartDate,SiteName, VisitDate)
            if result == 1:
                print "YAAAY"
                return render_template("34-viseventdetail.html", EventName=EventName, StartDate=StartDate,SiteName=SiteName,EndDate=EndDate,
                    price=price,Description=Description,TicketRemaining=TicketRemaining, success="Event has been logged!")
            elif result == 0:
                print  "NAAY"
                return render_template("34-viseventdetail.html", EventName=EventName, StartDate=StartDate,SiteName=SiteName,EndDate=EndDate,
                    price=price,Description=Description,TicketRemaining=TicketRemaining, error="An event with the same date has been already logged!")

        elif (newvisitdate < newstart) or  (newvisitdate > newend):
            return render_template("34-viseventdetail.html", EventName=EventName, StartDate=StartDate,SiteName=SiteName,EndDate=EndDate,
                    price=price,Description=Description,TicketRemaining=TicketRemaining, error="Visit Date must be between Start and End Dates")
        elif(TicketRemaining==0):
            return render_template("34-viseventdetail.html", EventName=EventName, StartDate=StartDate,SiteName=SiteName,EndDate=EndDate,price=price,Description=Description,TicketRemaining=TicketRemaining, error="The event is sold out!")
        
    except Exception as e:
        print("---> run into Exception:")
        print("---> " + str(e) + '\n')  # print exception message
        if str(e)[1:5] == "1062":

            # violates primary key constraint username
            return render_template("34-viseventdetail.html", EventName=EventName, StartDate=StartDate,SiteName=SiteName,EndDate=EndDate,
                price=price,Description=Description,TicketRemaining=TicketRemaining, error="An event with the same date has been already logged!")

        return go_to_functionality_screen()




#Screen 37
@app.route("/to_visitor_site_detail", methods=['GET'])
def visitor_siteDetails():
    if request.method == 'GET':
        # info1 = get_site_info('Atlanta Beltline Center')

        info1 = get_site_info(sitename)
               
        SiteName = info1[0][0]
        Address = str(info1[0][1])      
        Zipcode = str(info1[0][2])
        OpenEveryday = info1[0][3]
        fulladdress = Address + " " + Zipcode
    return render_template("37-vissitedetail.html", SiteName=SiteName, OpenEveryday=OpenEveryday,fulladdress=fulladdress)


@app.route("/visitor_logsiteVisit", methods=[ 'POST'])
def visitor_logsiteVisit():
    
    try:
        global _logged_user
        print "THE VISITOR IS: %s" % _logged_user

        # info1 = get_site_info('Atlanta Beltline Center')

        info1 = get_site_info(sitename)
               
        SiteName = info1[0][0]
        Address = str(info1[0][1])      
        Zipcode = str(info1[0][2])
        OpenEveryday = info1[0][3]
        fulladdress = Address + " " + Zipcode
        sitevisitdate = request.form["sitevisitdate"][0:10]

        result = logsiteVisit(_logged_user, SiteName, sitevisitdate)
        if result == 1:
            return render_template("37-vissitedetail.html", SiteName=SiteName, OpenEveryday=OpenEveryday,fulladdress=fulladdress, success="Site Visit logged successfully")

    except Exception as e:
        print("---> run into Exception:")
        print("---> " + str(e) + '\n')  # print exception message
        if str(e)[1:5] == "1062":

            # violates primary key constraint username
            return render_template("37-vissitedetail.html", SiteName=SiteName, OpenEveryday=OpenEveryday,fulladdress=fulladdress, error="Cannot log visit to the same site on same date")


@app.route("/to_create_event", methods=['POST', 'GET'])
def create_event():
    if request.method == 'GET':
        filStaff = []
        staffs = []
        response = getAllStaff();
        for item in response:
            staff={}
            staff['Username'] = item[0]
            staffs.append(staff)

        return render_template("27-managercreateevent.html", filName="", filPrice=-1, filCap=-1,
                filMinStaff=-1, filStDate="", filEndDate="", filDescr="", filStaff=filStaff, staffs=staffs)
    if request.method == 'POST':
        name=request.form["name"]
        price=request.form["price"]
        capacity=request.form["capacity"]
        minstaff=request.form["minstaff"]
        stdate=request.form["startdate"]
        enddate=request.form["enddate"]
        description=request.form["description"]

        if(price == ""):
            price = -1;
        if(capacity == ""):
            capacity = -1;
        if(minstaff == ""):
            minstaff = -1;
        price = float(price)
        capacity = float(capacity)
        minstaff = float(minstaff)

        selectedStaff = []
        allStaff = []
        response = getAllStaff()
        for item in response:
            staff={}
            staff['Username'] = item[0];
            allStaff.append(staff)

            included = ""
            try:
                included = request.form[item[0]]
            except:
                included = "No"
            if(included == "Yes"):
                selectedStaff.append(staff)

        if(stdate != "" and enddate != ""):
            response = getAvailableStaff(stdate, enddate);
            allStaff = []
            for item in response:
                staff={}
                staff['Username'] = item[0]
                print(item)
                allStaff.append(staff)

        if(name == "" or price == -1 or capacity == -1 or minstaff == -1 or stdate == ""
                or enddate == "" or description == "" or len(selectedStaff) == 0):
            error="You must fill in all fields to create the event"
        elif(len(selectedStaff) < minstaff):
            error="You must assign >= the minimum required staff"
        elif(minstaff < 1):
            error="The minimum number of staff must be at least 1"
        else:
            global _logged_users
            site = getManagersSite(_logged_user);
            addEvent(name, price, capacity, minstaff, stdate, enddate, description, selectedStaff, site);
            return render_manage_event();
        return render_template("27-managercreateevent.html", filName=name, filPrice=price,
                filCap=capacity, filMinStaff=minstaff, filStDate=stdate, filEndDate=enddate,
                filDescr=description, filStaff=selectedStaff, staffs=allStaff, error=error)

@app.route("/get_available_staff_to_create", methods=['POST'])
def get_available_staff_to_create():
    error=""
    print("why isn't htis working")
    name=request.form["name"]
    price=request.form["price"]
    capacity=request.form["capacity"]
    minstaff=request.form["minstaff"]
    stdate=request.form["startdate"]
    enddate=request.form["enddate"]
    description=request.form["description"]

    if(price == ""):
        price = -1;
    if(capacity == ""):
        capacity = -1;
    if(minstaff == ""):
        minstaff = -1;
    price = float(price)
    capacity = float(capacity)
    minstaff = float(minstaff)

    response = getAllStaff()
    selectedStaff = []
    allStaff = []
    for item in response:
        staff={}
        staff['Username'] = item[0];
        allStaff.append(staff)

        included = ""
        try:
            included = request.form[item[0]]
        except:
            included = "No"
        if(included == "Yes"):
            selectedStaff.append(staff)
    print(stdate)
    print(enddate)
    if(stdate == "" or enddate == ""):
        error="You must fill in a start and end date to get available staff"
        return render_template("27-managercreateevent.html", filName=name, filPrice=price,
                filCap=capacity, filMinStaff=minstaff, filStDate=stdate, filEndDate=enddate,
                filDescr=description, filStaff=selectedStaff, staffs=allStaff, error=error)
    else:
        response = getAvailableStaff(stdate, enddate);
        availableStaff = []
        for item in response:
            staff={}
            staff['Username'] = item[0]
            print(item)
            availableStaff.append(staff)
        return render_template("27-managercreateevent.html", filName=name, filPrice=price,
                filCap=capacity, filMinStaff=minstaff, filStDate=stdate, filEndDate=enddate,
                filDescr=description, filStaff=selectedStaff, staffs=availableStaff, error=error)

def render_manage_event():
    global _logged_user
    site = getManagersSite(_logged_user)
    response = getEvents25(site, None, None, None, None, None, None, None, None, None, None, None)
    eventList = []
    for item in response:
        event={}
        event['EventName'] = item[0]
        event['StaffCount'] = item[1]
        event['Duration'] = item[2]
        event['TotalVisits'] = item[3]
        event['TotalRevenue'] = item[4]
        event['StartDate'] = item[5]
        eventList.append(event)

    return render_template("25-managermanevent.html", events=eventList, filName="", filKey="", filStDate="",
            filEndDate="", filDurMin=-1, filDurMax=-1, filVisMin=-1, filVisMax=-1,
            filRevMin=-1, filRevMax=-1)

@app.route("/delete_event", methods=['POST'])
def delete_event():
    event = request.form["chosen_event"]
    event = event.replace("{'", "").replace("}", "")
    fields = event.split(", '")

    eventname = ""
    startdate = ""

    global _logged_user
    site = getManagersSite(_logged_user)

    for field in fields:
        if(len(field) >= 10 and field[0:10] == "EventName'"):
            strings = field.split(": ")
            eventname = strings[1][1:len(strings[1])-1]
        if(len(field) >= 10 and field[0:10] == "StartDate'"):
            strings = field.split(": ")
            date = strings[1][17:len(strings[1])]
            date = date.replace("(", "").replace(")", "")
            components = date.split(", ")
            year = components[0]
            month = components[1]
            day = components[2]

            if(len(month) < 2):
                month = "0" + month;
            if(len(day) < 2):
                day = "0" + day;
            startdate = year + "-" + month + "-" + day

    deleteEvent(eventname, startdate, site)

    return render_manage_event()

@app.route("/to_edit_event", methods=['POST', 'GET'])
def to_edit_event():
    event = request.form["chosen_event"]
    event = event.replace("{'", "").replace("}", "")
    fields = event.split(", '")

    eventname = ""
    startdate = ""

    global _logged_user
    site = getManagersSite(_logged_user)

    for field in fields:
        if(len(field) >= 10 and field[0:10] == "EventName'"):
            strings = field.split(": ")
            eventname = strings[1][1:len(strings[1])-1]
        if(len(field) >= 10 and field[0:10] == "StartDate'"):
            strings = field.split(": ")
            date = strings[1][17:len(strings[1])]
            date = date.replace("(", "").replace(")", "")
            components = date.split(", ")
            year = components[0]
            month = components[1]
            day = components[2]

            if(len(month) < 2):
                month = "0" + month;
            if(len(day) < 2):
                day = "0" + day;
            startdate = year + "-" + month + "-" + day

    response = getEventInfo(eventname, startdate, site)
    name = response[0]
    stDate = response[1]
    endDate = response[3]
    price = response[4]
    capacity = response[5]
    minstaff = response[6]
    descr = response[7]

    price = float(price)
    capacity = float(capacity)
    minstaff = float(minstaff)

    print(stDate)
    print(endDate)
    response = getAvailableStaff(stDate, endDate);
    availableStaff = []
    for item in response:
        staff={}
        staff['Username'] = item[0]
        availableStaff.append(staff)
    print(availableStaff)


    response = getAssignedStaff(eventname, startdate, site)
    assignedStaff = []
    for item in response:
        staff={}
        staff['Username'] = item[0]
        #availableStaff.append(staff)
        assignedStaff.append(staff)
    print(assignedStaff)

    response = getDayInfo(eventname, startdate, site, None, None, None, None)
    days = []
    for item in response:
        day={}
        day['Date'] = item[0]
        day['DailyVisits'] = item[1]
        day['DailyRevenue'] = item[2]
        days.append(day);

    return render_template("26-managereditevent.html", filName=name, filPrice=price,
            filCap=capacity, filEndDate=endDate, filStDate=stDate, filMinStaff=minstaff,
            filVisMin=-1, filVisMax=-1, filRevMin=-1, filRevMax=-1, filDescr=descr,
            staffs=availableStaff, filStaff=assignedStaff, days=days, error="")

@app.route("/to_edit_event_filtered", methods=['POST'])
def to_edit_event_filtered():
    error=""
    eventname = request.form["eventname"]
    startdate = request.form["startdate"]

    global _logged_user
    site = getManagersSite(_logged_user)

    response = getEventInfo(eventname, startdate, site)
    name = response[0]
    stDate = response[1]
    endDate = response[3]
    price = response[4]
    capacity = response[5]
    minstaff = response[6]
    descr = request.form["description"]

    price = float(price)
    capacity = float(capacity)
    minstaff = float(minstaff)

    response = getAvailableStaff(stDate, endDate);
    availableStaff = []
    assignedStaff = []
    for item in response:
        staff={}
        staff['Username'] = item[0]
        availableStaff.append(staff)

        included = ""
        try:
            included = request.form[item[0]]
        except:
            included = "No"
        if(included == "Yes"):
            assignedStaff.append(staff)

    vismin = request.form["minVisits"]
    vismax = request.form["maxVisits"]
    revmin = request.form["minRevenue"]
    revmax = request.form["maxRevenue"]

    if(vismin == ""):
        vismin = -1
    if(vismax == ""):
        vismax = -1;
    if(revmin == ""):
        revmin = -1;
    if(revmax == ""):
        revmax = -1;
    vismin = float(vismin)
    vismax = float(vismax)
    revmin = float(revmin)
    revmax = float(revmax)

    days=[]
    if(vismax < vismin and vismax != -1):
        error="Max Visits cannot be less than min"
    elif(revmax < revmin and revmin != -1):
        error="Max Revenue cannot be less than min"
    else:
        response = getDayInfo(eventname, startdate, site, vismin, vismax, revmin, revmax)
        for item in response:
            day={}
            day['Date'] = item[0]
            day['DailyVisits'] = item[1]
            day['DailyRevenue'] = item[2]
            days.append(day);

    return render_template("26-managereditevent.html", filName=name, filPrice=price,
            filCap=capacity, filEndDate=endDate, filStDate=stDate, filMinStaff=minstaff,
            filVisMin=vismin, filVisMax=vismax, filRevMin=revmin, filRevMax=revmax, filDescr=descr,
            staffs=availableStaff, filStaff=assignedStaff, days=days, error=error)

@app.route("/edit_event", methods=['POST'])
def edit_event():
    error=""
    eventname = request.form["eventname"]
    startdate = request.form["startdate"]

    global _logged_user
    site = getManagersSite(_logged_user)

    description = request.form["description"]

    response = getAllStaff();
    assignedStaff = []
    for item in response:
        staff={}
        staff['Username'] = item[0]

        included = ""
        try:
            included = request.form[item[0]]
        except:
            included = "No"
        if(included == "Yes"):
            assignedStaff.append(staff)

    updateEvent(eventname, startdate, site, description, assignedStaff)

    return render_manage_event();



#SCREENS 29-30
@app.route("/to_view_site_report", methods=['POST', 'GET'])
def to_view_site_report():
    if request.method == 'GET':
        days=[]
        return render_template("29-viewsitereport.html", stDate="", endDate="", eCountMin=-1,
                eCountMax=-1, stCountMin=-1, stCountMax=-1, toVisMin=-1, toVisMax=-1,
                toRevMin=-1, toRevMax=-1, days=days, error="")

    if request.method == 'POST':
        stDate = request.form["stDate"]
        endDate = request.form["endDate"]
        eCountMin = request.form["eCountMin"]
        eCountMax = request.form["eCountMax"]
        stCountMin = request.form["stCountMin"]
        stCountMax = request.form["stCountMax"]
        toVisMin = request.form["toVisMin"]
        toVisMax = request.form["toVisMax"]
        toRevMin = request.form["toRevMin"]
        toRevMax = request.form["toRevMax"]
        sort = ""
        try:
            sort = request.form["sort"]
        except:
            sort = None

        if(eCountMin == ""):
            eCountMin = -1
        if(eCountMax == ""):
            eCountMax = -1
        if(stCountMin == ""):
            stCountMin = -1
        if(stCountMax == ""):
            stCountMax = -1
        if(toVisMin == ""):
            toVisMin = -1
        if(toVisMax == ""):
            toVisMax = -1
        if(toRevMin == ""):
            toRevMin = -1;
        if(toRevMax == ""):
            toRevMax = -1;
        eCountMin = float(eCountMin)
        eCountMax = float(eCountMax)
        stCountMin = float(stCountMin)
        stCountMax = float(stCountMax)
        toVisMin = float(toVisMin)
        toVisMax = float(toVisMax)
        toRevMin = float(toRevMin)
        toRevMax = float(toRevMax)

        error=""
        days=[]
        if(stDate == "" or endDate == ""):
            error = "You must enter a date range in order for results to be shown"
        elif(eCountMin > eCountMax and eCountMax != -1):
            error = "Your maximum event count cannot be less than the minimum"
            eCountMax = float(-1)
        elif(stCountMin > stCountMax and stCountMax != -1):
            error = "Your maximum staff count cannot be less than the minimum"
            stCountMax = float(-1)
        elif(toVisMin > toVisMax and toVisMax != -1):
            error = "Your maximum total visits cannot be less than the minimum"
            toVisMax = float(-1)
        elif(toRevMin > toRevMax and toRevMax != 1):
            error = "Your maximum total revenue cannot be less than the minimum"
            toRevMax = float(-1)
        else:
            global _logged_user
            site = getManagersSite(_logged_user)
            response = getSiteReport(stDate, endDate, eCountMin, eCountMax, stCountMin, stCountMax,
                    toVisMin, toVisMax, toRevMin, toRevMax, site, sort)
            for item in response:
                day={}
                day['Date'] = item[0]
                day['EventCount'] = item[1]
                day['StaffCount'] = item[2]
                day['TotalVisits'] = item[3]
                day['TotalRevenue'] = item[4]
                days.append(day)

        return render_template("29-viewsitereport.html", stDate=stDate, endDate=endDate,
                eCountMin=eCountMin, eCountMax=eCountMax, stCountMin=stCountMin,
                stCountMax=stCountMax, toVisMin=toVisMin, toVisMax=toVisMax, toRevMin=toRevMin,
                toRevMax=toRevMax, days=days, error=error)

@app.route("/to_daily_detail", methods=['POST'])
def daily_detail():
    date = request.form["chosen_day"]
    global _logged_user
    site = getManagersSite(_logged_user)

    response = getDailyDetail(site, date, None)
    events = []
    for item in response:
        event = {}
        event['EventName'] = item[0]
        event['StaffNames'] = item[1]
        event['Visits'] = item[2]
        event['Revenue'] = item[3]
        events.append(event)

    return render_template("30-dailydetail.html", events=events, date=date)

@app.route("/sort_daily_detail", methods=['POST'])
def sort_daily_detail():
    date = request.form["date"]
    sort = ""
    try:
        sort = request.form["sort"]
    except:
        sort = None

    global _logged_user
    site = getManagersSite(_logged_user)

    response = getDailyDetail(site, date, sort)
    events = []
    for item in response:
        event = {}
        event['EventName'] = item[0]
        event['StaffNames'] = item[1]
        event['Visits'] = item[2]
        event['Revenue'] = item[3]
        events.append(event)

    return render_template("30-dailydetail.html", events=events, date=date)



#SCREENS 31-32
@app.route("/to_view_schedule", methods=['POST', 'GET'])
def to_view_schedule():
    if request.method == 'GET':
        global _logged_user
        events = []
        response = getSchedule(_logged_user, None, None, None, None, None)
        for item in response:
            event = {}
            event['EventName'] = item[0]
            event['SiteName'] = item[1]
            event['StartDate'] = item[2]
            event['EndDate'] = item[3]
            event['StaffCount'] = item[4]
            events.append(event)

        return render_template("31-viewschedule.html", filName="", filDescr="",
                filStDate="", filEndDate="", events=events)

    if request.method == 'POST':
        print("LOL")
        ename = request.form["name"]
        descr = request.form["description"]
        startdate = request.form["startdate"]
        enddate = request.form["enddate"]
        sort = ""
        try:
            sort = request.form["sort"]
        except:
            sort = None

        global _logged_user
        events = []
        response = getSchedule(_logged_user, ename, descr, startdate, enddate, sort)
        for item in response:
            event = {}
            event['EventName'] = item[0]
            event['SiteName'] = item[1]
            event['StartDate'] = item[2]
            event['EndDate'] = item[3]
            event['StaffCount'] = item[4]
            events.append(event)

        return render_template("31-viewschedule.html", filName=ename, filDescr=descr,
                filStDate=startdate, filEndDate=enddate, events=events)




#SCREENS 33-34
@app.route("/to_vis_explore_event", methods=['POST', 'GET'])
def to_vis_explore_event():
    if request.method == 'GET':
        global _logged_user

        response = getEvents33(_logged_user, None, None, None, None, None, None,
                None, None, None, "Yes", "Yes", None)
        events = []
        for item in response:
            event = {}
            event['EventName'] = item[0]
            event['SiteName'] = item[1]
            event['TicketPrice'] = item[2]
            event['TicketsRemaining'] = item[3]
            event['TotalVisits'] = item[4]
            event['MyVisits'] = item[5]
            events.append(event)

        # getting the sites for the dropdown
        response = getSiteNames()
        siteList = []
        for item in response:
            site={}
            site['SiteName'] = item[0]
            siteList.append(site)

        return render_template("33-visexploreevent.html", filName="", filDescr="",
                filSite="", filStDate="", filEndDate="", toVisMin=-1, toVisMax=-1,
                tPriceMin=-1, tPriceMax=-1, filIncVis="Yes", filIncSoldOut="Yes",
                sites=siteList, events=events)

    if request.method == 'POST':
        name = request.form["name"]
        descr = request.form["description"]
        site = request.form["site"]
        startdate = request.form["startdate"]
        enddate = request.form["enddate"]
        toVisMin = request.form["toVisMin"]
        toVisMax = request.form["toVisMax"]
        tPriceMin = request.form["tPriceMin"]
        tPriceMax = request.form["tPriceMax"]
        includeVisit = request.form["includeVisited"]
        includeSoldOut = request.form["includeSoldOut"]
        sort = ""
        try:
            sort = request.form["sort"]
        except:
            sort = None

        if(toVisMin == "" or toVisMin is None):
            toVisMin = -1
        if(toVisMax == "" or toVisMax is None):
            toVisMax = -1
        if(tPriceMin == "" or tPriceMin is None):
            tPriceMin = -1
        if(tPriceMax == "" or tPriceMax is None):
            tPriceMax = -1
        toVisMin = float(toVisMin)
        toVisMax = float(toVisMax)
        tPriceMin = float(tPriceMin)
        tPriceMax = float(tPriceMax)

        global _logged_user
        response = getEvents33(_logged_user, name, descr, site, startdate, enddate,
                toVisMin, toVisMax, tPriceMin, tPriceMax, includeVisit, includeSoldOut, sort)
        events = []
        for item in response:
            event = {}
            event['EventName'] = item[0]
            event['SiteName'] = item[1]
            event['TicketPrice'] = item[2]
            event['TicketsRemaining'] = item[3]
            event['TotalVisits'] = item[4]
            event['MyVisits'] = item[5]
            events.append(event)

        # getting the sites for the dropdown
        response = getSiteNames()
        siteList = []
        for item in response:
            site={}
            site['SiteName'] = item[0]
            siteList.append(site)

        return render_template("33-visexploreevent.html", filName=name, filDescr=descr,
                filSite=site, filStDate=startdate, filEndDate=enddate, toVisMin=toVisMin,
                toVisMax=toVisMax, tPriceMin=tPriceMin, tPriceMax=tPriceMax, filIncVis=includeVisit,
                filIncSoldOut=includeSoldOut, sites=siteList, events=events)






if __name__ == '__main__':
    app.run()
