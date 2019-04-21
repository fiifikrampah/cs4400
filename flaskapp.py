# This app connects the html render templates to the flask app
from api import *
from database import *
from flask import Flask, render_template, json, request, Response, redirect, url_for
from decimal import Decimal
from datetime import datetime

app = Flask(__name__)
_logged_user = ""
_logged_userType = ""
# _logged_user = "manager2"
# _logged_userType = "Manager, Visitor"

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
    # return to_manage_event();
    # return eventDetails()
    # return visitor_eventDetails()
    return visitor_siteDetails()

    # return render_template('1-login.html', error = "")

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

@app.route("/add-email-reg-user", methods=['GET','POST'])
def addEmail_register_1():
    if request.method == 'POST':
    # Username = request.form["username"]
        email = request.form["addemail"]

        if constraint_email_format(email) == 0:
            # previous = request.referrer
            # return (request.referrer)
            return render_template('3-reguseronly.html', error="Please enter a valid email!")

        tempmail_insert(email) 

        response = get_tempmails()
        if response == []:
            return render_template('3-reguseronly.html', error="Please enter at least one email address!")

        emails = []
        for item in response:
            email = {}
            email['Email'] = item[0]
            emails.append(email)
        return render_template('3-reguseronly.html', emails=emails)

@app.route("/remove_tempmail-user", methods=['POST'])
def delete_tempmails_1():
    email = request.form["rememail"]
    delete_tempmail(email)
    response = get_tempmails()
    if response == []:
        return render_template('3-reguseronly.html', error="Please enter at least one email address!")

    emails = []
    for item in response:
        email = {}
        email['Email'] = item[0]
        emails.append(email)
    return render_template('3-reguseronly.html', emails=emails)


@app.route("/add_email_reg_visitor", methods=['GET','POST'])
def addEmail_register_2():
    if request.method == 'POST':
    # Username = request.form["username"]
        email = request.form["addemail"]

        if constraint_email_format(email) == 0:
            # previous = request.referrer
            # return (request.referrer)
            return render_template('4-regvisit.html', error="Please enter a valid email!")

        tempmail_insert(email) 

        response = get_tempmails()
        if response == []:
            return render_template('4-regvisit.html', error="Please enter at least one email address!")

        emails = []
        for item in response:
            email = {}
            email['Email'] = item[0]
            emails.append(email)
        return render_template('4-regvisit.html', emails=emails)

@app.route("/remove_tempmail_visitor", methods=['POST'])
def delete_tempmails_2():
    email = request.form["rememail"]
    delete_tempmail(email)
    response = get_tempmails()
    if response == []:
        return render_template('4-regvisit.html', error="Please enter at least one email address!")

    emails = []
    for item in response:
        email = {}
        email['Email'] = item[0]
        emails.append(email)
    return render_template('4-regvisit.html', emails=emails)


@app.route("/add_email_reg_emp", methods=['GET','POST'])
def addEmail_register_3():
    if request.method == 'POST':
    # Username = request.form["username"]
        email = request.form["addemail"]

        if constraint_email_format(email) == 0:
            # previous = request.referrer
            # return (request.referrer)
            return render_template('5-regemp.html', error="Please enter a valid email!")

        tempmail_insert(email) 

        response = get_tempmails()
        if response == []:
            return render_template('5-regemp.html', error="Please enter at least one email address!")

        emails = []
        for item in response:
            email = {}
            email['Email'] = item[0]
            emails.append(email)
        return render_template('5-regemp.html', emails=emails)

@app.route("/remove_tempmail_emp", methods=['POST'])
def delete_tempmails_3():
    email = request.form["rememail"]
    delete_tempmail(email)
    response = get_tempmails()
    if response == []:
        return render_template('5-regemp.html', error="Please enter at least one email address!")

    emails = []
    for item in response:
        email = {}
        email['Email'] = item[0]
        emails.append(email)
    return render_template('5-regemp.html', emails=emails)

@app.route("/add_email_reg_empvis", methods=['GET','POST'])
def addEmail_register_4():
    if request.method == 'POST':
    # Username = request.form["username"]
        email = request.form["addemail"]

        if constraint_email_format(email) == 0:
            # previous = request.referrer
            # return (request.referrer)
            return render_template('6-regempvisit.html', error="Please enter a valid email!")

        tempmail_insert(email) 

        response = get_tempmails()
        if response == []:
            return render_template('6-regempvisit.html', error="Please enter at least one email address!")

        emails = []
        for item in response:
            email = {}
            email['Email'] = item[0]
            emails.append(email)
        return render_template('6-regempvisit.html', emails=emails)

@app.route("/remove_tempmail_empvis", methods=['POST'])
def delete_tempmails_4():
    email = request.form["rememail"]
    delete_tempmail(email)
    response = get_tempmails()
    if response == []:
        return render_template('6-regempvisit.html', error="Please enter at least one email address!")

    emails = []
    for item in response:
        email = {}
        email['Email'] = item[0]
        emails.append(email)
    return render_template('6-regempvisit.html', emails=emails)


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
        # email = request.form["addemail"]



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
                response = get_tempmails()

                for item in response:
                    email = item[0]
                    final = email_insert(Username, email)
                    if final == 1:
                        delete_mailrecs(Username)
                        user_delete(Username)
                        clear_tempmails()
                        return(render_template("3-reguseronly.html", error="One or more emails you entered, has already been registered!"))
                    else:
                        clear_tempmails()
                

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
        # email = request.form["email"]



        # if constraint_email_format(email) == 0:
        #     return render_template("4-regvisit.html", error="Email does not match format!")
        if constraint_username_format(Username) == 0:
            return render_template("4-regvisit.html", error="Username does not meet requirement!")

        error = ""
        if Password != confirmed_pass:
            return render_template("4-regvisit.html", error="Passwords do not match!")
        elif constraint_password_format(Password) == 0:
            return render_template("4-regvisit.html", eremove_tempmail_visitorrror="Passwords do not meet requirement!")
        else:
            result = validate_user_registration(Username, Password, Status, Firstname, Lastname, UserType)
            #successful validation
            if result == 0:
                response = get_tempmails()

                for item in response:
                    email = item[0]
                    final = email_insert(Username, email)
                    if final == 1:
                        delete_mailrecs(Username)
                        user_delete(Username)
                        clear_tempmails()
                        return(render_template("4-regvisit.html", error="One or more emails you entered, has already been registered!"))
                    else:
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
        # email = request.form["email"]



        # if constraint_email_format(email) == 0:
        #     return render_template("5-regemp.html", error="Email does not match format!")
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
                    response = get_tempmails()

                    for item in response:
                        email = item[0]
                        final = email_insert(Username, email)
                        if final == 1:
                            delete_mailrecs(Username)
                            user_delete(Username)
                            clear_tempmails()
                            return(render_template("5-regemp.html", error="One or more emails you entered, has already been registered!"))
                    else:
                        clear_tempmails()
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
        # email = request.form["email"]



        # if constraint_email_format(email) == 0:
        #     return render_template("6-regempvisit.html", error="Email does not match format!")
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
                    response = get_tempmails()

                    for item in response:
                        email = item[0]
                        final = email_insert(Username, email)
                        if final == 1:
                            delete_mailrecs(Username)
                            user_delete(Username)
                            clear_tempmails()
                            return(render_template("6-regempvisit.html", error="One or more emails you entered, has already been registered!"))
                    else:
                        clear_tempmails()
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
                # global _logged_user
                global _logged_userType
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
    try:
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
            
    except Exception as e:
        print("---> run into Exception:")
        print("---> " + str(e) + '\n')  # print exception message
        if str(e)[1:5] == "1062":

            # violates primary key constraint username
             return render_template('15-usertaketransit.html', error="Transit already exists! Please click the back button and enter a different Transit")





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
        _logged_user
        _logged_userType = get_usertype(_logged_user)
        print "FIIFI THE GUY IS: %s AND HIS USER IS: %s" % (_logged_userType, _logged_user)
        info = get_employee_info(_logged_user)
        info2 = get_site_info17(_logged_user)
        fname = info[0]
        lname = info[1]
        uname = info[2]
        sname = info2
        eid = info[3]
        phone = info[4]
        address = info[5] + ", " + info[6] + ", " + info[7] + " " + str(info[8])

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
        try:
                # updating info
            fname = request.form["firstname"];
            lname = request.form["lastname"];
            phone = request.form["phonenum"];
            visitor = request.form["isvisitor"];
            newemail = request.form["addemail"]

            print "visitor is: %s" % visitor
            update_employee(_logged_user, fname, lname, phone, visitor)

            # rendering screen again
            global _logged_user
            info = get_employee_info(_logged_user)
            info2 = get_site_info17(_logged_user)
            uname = info[2]
            sname = info2
            eid = info[3]
            address = info[5] + ", " + info[6] + ", " + info[7] + " " + str(info[8])

            response = get_employee_emails(_logged_user)
            emails = []
            for item in response:
                email = {}
                email['Email'] = item[0]
                emails.append(email)

            return render_template('17-empmanageprofile.html', fname=fname, lname=lname, uname=uname,
                    sname=sname, eid=eid, phone=phone, address=address, visitor=visitor, emails=emails,
                    newemail=newemail)
        except Exception as e:
            print("---> run into Exception:")
            print("---> " + str(e) + '\n')  # print exception message
            _logged_user
            _logged_userType = get_usertype(_logged_user)
            if str(e)[1:5] == "1062":
                # violates primary key constraint
                info = get_employee_info(_logged_user)
                info2 = get_site_info17(_logged_user)
                fname = info[0]
                lname = info[1]
                uname = info[2]
                sname = info2
                eid = info[3]
                phone = info[4]
                address = info[5] + ", " + info[6] + ", " + info[7] + " " + str(info[8])

                visitor = "0"
                if('Visitor' in _logged_userType):
                    visitor = "1"

                response = get_employee_emails(_logged_user)
                emails = []
                for item in response:
                    email = {}
                    email['Email'] = item[0]
                    emails.append(email)

                return render_template('17-empmanageprofile.html',fname=fname, lname=lname, uname=uname,
                    sname=sname, eid=eid, phone=phone, address=address, visitor=visitor, emails=emails,
                    newemail=newemail, error="Phone number already exists!")
            else:
                # other violation
                return 2
        

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
    info2 = get_site_info17(_logged_user)
    uname = info[2]
    sname = info2
    eid = info[3]
    address = info[5] + ", " + info[6] + ", " + info[7] + " " + str(info[8])

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
    info2 = get_site_info17(_logged_user)
    uname = info[2]
    sname = info2
    eid = info[3]
    address = info[5] + ", " + info[6] + ", " + info[7] + " " + str(info[8])

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

@app.route("/to_viewsitereport.html", methods=['POST', 'GET'])
def to_view_site_report():
    if request.method == 'GET':
        sites=[]
        render_template("29-viewsitereport.html", sites=sites, stDate="", endDate="", eCountMin=-1, eCountMax=-1,
                stCountMin=-1, stCountMax=-1, toVisMin=-1, toVisMax=-1, toRevMin=-1, toRevMax=-1)
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
        toVisMax = float(tovisMax)
        toRevMin = float(toRevMin)
        toRevMax = float(toRevMax)



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
            eventList.append(event)

        return render_template("25-managermanevent.html", events=eventList, filName=name,
                filKey=descr, filStDate=startDate, filEndDate=endDate, filDurMin=mindur,
                filDurMax=maxdur, filVisMin=minvis, filVisMax=maxvis,
                filRevMin=minrev, filRevMax=maxrev)




#Screen32
@app.route("/to_staff_event_detail", methods=['GET'])
def eventDetails():
    if request.method == 'GET':

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

    return render_template("32-eventdetail.html", EventName=EventName, StartDate=StartDate,SiteName=SiteName,EndDate=EndDate,
        EventPrice=EventPrice, Capacity=Capacity,Description=Description,StaffUsername=StaffUsername,Duration=Duration)




# Screen 34
@app.route("/to_visitor_event_detail", methods=['GET'])
def visitor_eventDetails():
    if request.method == 'GET':
        # info1 = getEventDetail32("Bus Tour", "2019-02-01 00:00:00", "Inman Park")

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
        info1 = get_site_info('Atlanta Beltline Center')

        # info1 = get_site_info(sitename)
               
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
        print("hey")
    if request.method == 'POST':
        print("hey")










if __name__ == '__main__':
    app.run()
