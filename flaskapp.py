# This app connects the html render templates to the flask app
from api import *
from database import *
from flask import Flask, render_template, json, request, Response
from decimal import Decimal

app = Flask(__name__)
_logged_user = "manager2"
_logged_userType = "Manager, Visitor"


@app.route('/')
def main():
    """
    Starts app at login screen
    """
    set_connection()

    #return transit_history();
    return take_transit();
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
    global logged_user
    logged_user = ""
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
        emp_type = emptype_checker(_name)
    	if login_response == 0:
            return render_template("1-login.html", error = "Cannot login, try again.")
        else:
            _logged_user = name;
            if login_response in ['User', 'Employee', 'Employee, Visitor', 'Admin', 'Admin, Visitor', 'Manager', 'Manager, Visitor', 'Staff', 'Staff, Visitor', 'Visitor']:
                _logged_userType = login_response;
                return go_to_functionality_screen();
            else:
                _logged_user = "";
                _logged_userType = "";
                return render_template("login_test-bootstrapped.html", error = "Cannot login, try again.")

@app.route("/back-button", methods = ['GET'])
def go_to_functionality_screen():
    if request.method == 'GET':
        if _logged_userType in ['User','Employee', 'Employee, Visitor']:
            return render_template("7-userfunc.html", error = "")
        elif _logged_userType in ['Admin']:
            return render_template("8-adminfunc.html", error = "")
        elif _logged_userType in ['Admin, Visitor']:
            return render_template("9-adminvisitfunc.html", error = "")
        elif _logged_userType in ['Manager']:
            return render_template("10-manfunc.html", error = "")
        elif _logged_userType in ['Manager, Visitor']:
            return render_template("11-manvisitfunc.html", error = "")
        elif _logged_userType in ['Staff']:
            return render_template("12-stafffunc.html", error = "")
        elif _logged_userType in ['Staff, Visitor']:
            return render_template("13-staffvisitfunc.html", error = "")
        elif _logged_userType in ['Visitor']:
            return render_template("14-visitorfunc.html", error = "")
        else:
            return render_template("1-login.html", error = "Username or password is incorrect,please try again.")


@app.route("/to_user_take_transit")
def to_user_take_transit():
    """
    Takes user to take transit page
    """
    return render_template('15-usertaketransit.html', error="")

@app.route("/to_user_transit_history")
def to_user_transit_history():
    """
    Takes user to view transit history page
    """
    return render_template('16-usertranshistory.html', error="")

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


@app.route("/to_manage_profile")
def manage_profile():
    """
    Takes user to manage profile page
    """
    return render_template('17-empmanageprofile.html', error="")


@app.route("/to_manage_user")
def manage_user():
    """
    Takes user to manage user page
    """
    return render_template('18-adminmanuser.html', error="")


@app.route("/to_manage_transit")
def manage_transit():
    """
    Takes user to manage transit page
    """
    return render_template('22-adminmantransit.html', error="")


@app.route("/to_manage_site")
def manage_site():
    """
    Takes user to manage site page
    """
    return render_template('19-adminmansite.html', error="")


@app.route("/add_email", methods =['POST'])
def add_email():
    emails = request.get_json()
    # emails = request.get_json()
    print emails  






# IS THIS STILL NEEDED?
@app.route("/back", methods=['GET'])
def backButton():

    #implement logic for sending user back to their corresponding functionality
    return render_template("1-login.html", error="Cannot login, try again.")


@app.route("/15-usertaketransit", methods = ['POST', 'GET'])
def take_transit():
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

"""
@app.route("/15-usertaketransit/filter", methods = ['POST', 'GET'])
def filter_take_transit():
    if request.method == 'POST':
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
"""

@app.route("/15-usertaketransit/log_transit", methods=['POST'])
def log_transit():
    if request.method == 'POST':
        transit = request.form["chosen_transit"]
        date = request.form["dateLogged"]

        response = logTransit(_logged_user, transit, date)
        return take_transit();

@app.route("/16-usertranshistory", methods=['POST','GET'])
def transit_history():
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
        startDate = request.form["startDate"]
        endDate = request.form["endDate"]

        response = getFilteredTransit2(site, transitType, route, startDate, endDate)

        transitList = []
        for item in response:
            transit={}
            transit['Date'] = item[0]
            transit['TransitRoute'] = item[1]
            transit['TransitType'] = item[2];
            transit['TransitPrice'] = item[3]
            transitList.append(transit);

        return render_template('16-usertranshistory.html', sites=siteList, types=transitTypeList, transits=transitList)

if __name__ == '__main__':
    app.run()
