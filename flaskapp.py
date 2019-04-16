# This app connects the html render templates to the flask app
from api import *
from database import *
from flask import Flask, render_template, json, request, Response
from decimal import Decimal

app = Flask(__name__)
_logged_user = ""
_logged_userType = ""


@app.route('/')
def main():
    """
    Starts app at login screen
    """
    set_connection()

    #return user_take_transit();
    #return user_transit_history();
    return manage_profile();
    #return manage_user();
    #return manage_site();
    #return create_site();
    #return manage_transit();
    #return create_transit();
    #return manage_event();
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
            elif login_response in ['Employee', 'Employee, Visitor', 'Admin', 'Admin, Visitor', 'Manager', 'Manager, Visitor', 'Staff', 'Staff, Visitor']:
                emp_type = emptype_checker(_name)
                _logged_userType = emp_type
                if _logged_userType in ['Employee', 'Employee, Visitor']:
                    _logged_user = _name
                    print "The username of the logged user is: %s and his type is: %s" % (_logged_user,_logged_userType)
                    return render_template("7-userfunc.html", error = "")
                elif _logged_userType in ['Admin']:
                    _logged_user = _name
                    print "The username of the logged user is: %s and his type is: %s" % (_logged_user,_logged_userType)
                    return render_template("8-adminfunc.html", error = "")
                elif _logged_userType in ['Admin, Visitor']:
                    _logged_user = _name
                    print "The username of the logged user is: %s and his type is: %s" % (_logged_user,_logged_userType)
                    return render_template("9-adminvisitfunc.html", error = "")
                elif _logged_userType in ['Manager']:
                    _logged_user = _name
                    print "The username of the logged user is: %s and his type is: %s" % (_logged_user,_logged_userType)
                    return render_template("10-manfunc.html", error = "")
                elif _logged_userType in ['Manager, Visitor']:
                    _logged_user = _name
                    print "The username of the logged user is: %s and his type is: %s" % (_logged_user,_logged_userType)
                    return render_template("11-manvisitfunc.html", error = "")
                elif _logged_userType in ['Staff']:
                    _logged_user = _name
                    print "logged person is: %s" % _logged_user
                    print "The username of the logged user is: %s and his type is: %s" % (_logged_user,_logged_userType)
                    return render_template("12-stafffunc.html", error = "")
                elif _logged_userType in ['Staff, Visitor']:
                    _logged_user = _name
                    print "The username of the logged user is: %s and his type is: %s" % (_logged_user,_logged_userType)
                    return render_template("13-staffvisitfunc.html", error = "")
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

        person = _logged_user
        p_type = usertype_checker(_logged_user)

        if p_type in ['Employee']:
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


@app.route("/to_user_take_transit", methods=['POST', 'GET'])
def user_take_transit():
    # getting the sites for the dropdown
    response = getSiteNames()
    siteList = []
    for item in response:
        site={}
        site['SiteName'] = item[0]
        siteList.append(site)

        # else:
        #     print "Sorry an error occured."
        #     return 1


    # getting the transit types for the dropdown
    response = getTransitTypes()
    transitTypeList = []
    for item in response:
        tType={}
        tType['TransitType'] = item[0]
        transitTypeList.append(tType)

    if request.method == 'GET':
        # getting unfiltered transit when the page is first loaded
        response = getAllTransit()

        transitList = []
        for item in response:
            transit={}
            transit['TransitRoute'] = item[0]
            transit['TransitType'] = item[1]
            transit['Price'] = item[2];
            transit['ConnectedSites'] = item[3]
            transitList.append(transit);

        return render_template('15-usertaketransit.html', sites=siteList, types=transitTypeList, transits=transitList)

    if request.method == 'POST':
        #getting filtered transit when some of the options have been played with
        site = request.form["site"]
        transitType = request.form["transittype"]
        minPrice = request.form["minPrice"]
        maxPrice = request.form["maxPrice"]

        response = getFilteredTransit(site, transitType, minPrice, maxPrice)

        transitList = []
        for item in response:
            transit={}
            transit['TransitRoute'] = item[0]
            transit['TransitType'] = item[1]
            transit['Price'] = item[2];
            transit['ConnectedSites'] = item[3]
            transitList.append(transit);

        return render_template('15-usertaketransit.html', sites=siteList, types=transitTypeList, transits=transitList)

@app.route("/to_user_transit_history", methods=['POST', 'GET'])
def user_transit_history():
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
        response = getAllTransit2(_logged_user)

        transitList = []
        for item in response:
            transit={}
            transit['Date'] = item[0]
            transit['TransitRoute'] = item[1]
            transit['TransitType'] = item[2];
            transit['TransitPrice'] = item[3]
            transitList.append(transit);

        return render_template('16-usertranshistory.html', sites=siteList, types=transitTypeList, transits=transitList)

    if request.method == 'POST':
        #getting filtered transit when some of the options have been played with
        site = request.form["site"]
        transitType = request.form["transittype"]
        route = request.form["route"]
        startDate = request.form["startdate"]
        endDate = request.form["enddate"]

        # global _logged_user
        response = getFilteredTransit2(_logged_user, site, transitType, route, startDate, endDate)

        transitList = []
        for item in response:
            transit={}
            transit['Date'] = item[0]
            transit['TransitRoute'] = item[1]
            transit['TransitType'] = item[2];
            transit['TransitPrice'] = item[3]
            transitList.append(transit);

        return render_template('16-usertranshistory.html', sites=siteList, types=transitTypeList, transits=transitList)

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

@app.route("/to_manage_profile", methods=['POST', 'GET'])
def manage_profile():


    if request.method == 'POST':
        fname = request.form["firstname"];
        lname = request.form["lastname"];
        phone = request.form["phonenum"];
        visitor = request.form["isvisitor"];

        global _logged_user
        update_employee(_logged_user, fname, lname, phone, visitor)

    """
    Takes user to manage profile page
    """
    return render_template('17-empmanageprofile.html', error="")


# @app.route("/to_manage_user")
# def manage_user():
#     """
#     Takes user to manage user page
#     """
#     return render_template('18-adminmanuser.html', error="")


# @app.route("/to_manage_transit")
# def manage_transit():
#     """
#     Takes user to manage transit page
#     """
#     return render_template('22-adminmantransit.html', error="")


# @app.route("/to_manage_site")
# def manage_site():
#     """
#     Takes user to manage site page
#     """
#     return render_template('19-adminmansite.html', error="")

# FIIFI FIX THIS:
# @app.route("/add_email", methods =['POST'])
# def add_email():
#     emails = request.get_json()
#     # emails = request.get_json()
#     print emails


#     return manageProfileTemplate();


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
        response = getAllTransitsM();

        transitList=[]
        for item in response:
            transit = {}
            transit['TransitRoute'] = item[0]
            transit['TransitType'] = item[1]

            transit['TransitPrice'] = item[2]

            transit['ConnectedSites'] = item[3]
            transit['TransitLogged'] = item[4]
            transitList.append(transit)

        return render_template('22-adminmantransit.html', sites=siteList, types=transitTypeList, transits=transitList)

    if request.method == 'POST':
        site = request.form["site"]
        type = request.form["type"]
        route = request.form["route"]
        minPrice = request.form["minPrice"]
        maxPrice = request.form["maxPrice"]

        response = getFilteredTransitsM(site, type, route, minPrice, maxPrice);

        transitList=[]
        for item in response:
            transit = {}
            transit['TransitRoute'] = item[0]
            transit['TransitType'] = item[1]

            transit['TransitPrice'] = item[2]

            transit['ConnectedSites'] = item[3]
            transit['TransitLogged'] = item[4]
            transitList.append(transit)

        return render_template('22-adminmantransit.html', sites=siteList, types=transitTypeList, transits=transitList)

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

    response = None

    if request.method == 'GET':
        response = getAllSites();

    if request.method == 'POST':
        site = request.form["site"]
        manager = request.form["manager"]
        everyday = request.form["everyday"]

        response = getFilteredSites(site, manager, everyday)

    siteList = []
    for item in response:
        site={}
        site['Name']=item[0]
        site['Manager']=item[1]
        site['OpenEveryday']=item[2]
        siteList.append(site)

    return render_template('19-adminmansite.html', siteNames=siteNameList, managers=managerList, sites=siteList)

@app.route("/to_manage_site/edit", methods=['POST'])
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

    print(openeveryday)
    managerList = []
    curmanager={}
    curmanager['Username'] = currentManager
    managerList.append(curmanager);

    response = getUnassignedManagers();
    for item in response:
        manager={}
        manager['Username']=item[0]
        managerList.append(manager)

    return render_template("20-admineditsite.html", site=site, managers=managerList, openeveryday=openeveryday, currentManager=currentManager)

@app.route("/edit_site", methods=['POST'])
def edit_site():
    oldname = request.form["oldname"]
    name = request.form["name"]
    zip = request.form["zipcode"]
    address = request.form["address"]
    manager = request.form["manager"]
    everyday = request.form["everyday"]

    update_site(oldname, name, zip, address, manager, everyday)

    return render_manage_sites();

@app.route("/add_email", methods =['POST'])
def add_email():
    emails = request.get_json()
    # emails = request.get_json()
    print emails

@app.route("/to_user_take_transit/log_transit", methods=['POST'])
def log_transit():
    if request.method == 'POST':
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

        # getting unfiltered transit when the page is first loaded
        response = getAllTransit()

        transitList = []
        for item in response:
            transit={}
            transit['TransitRoute'] = item[0]
            transit['TransitType'] = item[1]
            transit['Price'] = item[2];
            transit['ConnectedSites'] = item[3]
            transitList.append(transit);

        return render_template('15-usertaketransit.html', sites=siteList, types=transitTypeList, transits=transitList)

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

        return render_template('21-admincreatesite.html', managers=unassignedManagers)

    if request.method == 'POST':
        #pulls the necessary information form the html form and adds to the database
        name = request.form["name"]
        zip = request.form["zipcode"]
        address = request.form["address"]
        manager = request.form["manager"]
        everyday = request.form["everyday"]

        add_site(name, address, zip, everyday, manager);

        return render_manage_sites();

@app.route("/delete_site", methods=['POST'])
def delete_site():
    name = request.form["chosen_site"]

    removesite(name);

    return render_manage_sites();

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
        return render_template("24-admincreatetransit.html", sites=siteNameList, types=transitTypeList)

    if request.method == 'POST':
        # TODO actually create the site

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

        response = getAllTransitsM();

        transitList=[]
        for item in response:
            transit = {}
            transit['TransitRoute'] = item[0]
            transit['TransitType'] = item[1]
            transit['TransitPrice'] = item[2]
            transit['ConnectedSites'] = item[3]
            transit['TransitLogged'] = item[4]
            transitList.append(transit)

        return render_template('22-adminmantransit.html', sites=siteList, types=transitTypeList, transits=transitList)

@app.route("/remove_email", methods=['POST'])
def delete_email():
    email = request.form["email"];
    deleteEmail(email);

    return manageProfileTemplate();

@app.route("/add-email", methods=['POST'])
def addEmail():
    email = request.form["email"];

    global _logged_user
    email_insert(_logged_user, email);

    return manageProfileTemplate();

def manageProfileTemplate():
    #getting all employee information for this page except emails
    global _logged_user;
    response = get_employee_info(_logged_user);
    info = response[0]
    fname=info[0]
    lname=info[1]
    uname=info[2]
    sname=info[3]
    eid=info[4]
    phone=info[5]
    address=info[6] + ", " + info[7] + ", " + info[8] + " " + str(info[9])

    response = get_employee_emails(_logged_user);

    emailList = []
    for item in response:
        email={}
        email['Email']=item[0];
        emailList.append(email);

    return render_template('17-empmanageprofile.html', fname=fname, lname=lname, uname=uname, sname=sname, eid=eid, phone=phone, address=address, emails=emailList)

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

    response = getAllSites();
    siteList = []
    for item in response:
        site={}
        site['Name']=item[0]
        site['Manager']=item[1]
        site['OpenEveryday']=item[2]
        siteList.append(site)

    return render_template('19-adminmansite.html', siteNames=siteNameList, managers=managerList, sites=siteList)








if __name__ == '__main__':
    app.run()
