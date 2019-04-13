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
    # return render_template('1-login.html', error = "")
    # return render_template('login_test-bootstrapped.html', error = "")
    return take_transit();
    #return transit_history();

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

@app.route("/register_user", methods = ["POST"])
def register_user():
    print "Starting user register functionality"
    if request.method == "POST":
        fname = request.form["fname"]
        lname = request.form["lname"]
        username = request.form["username"]
        password = request.form["pword"]
        confirmed_pass = request.form["cpword"]
        email = request.form["email"]
        status = 'Pending'
        UserType = 'User'

        if constraint_email_format(email) == 0:
            return render_template("3-reguseronly.html", error="Email does not match format!")
        if constraint_username_format(username) == 0:
            return render_template("3-reguseronly.html", error="Username does not meet requirement!")

        error = ""
        if password != confirmed_pass:
            return render_template("3-reguseronly.html", error="Passwords do not match!")
        elif constraint_password_format(password) == 0:
            return render_template("3-reguseronly.html", error="Passwords do not meet requirement!")
        else:
            result = validate_user_registration(fname, lname, username, password, status, UserType)
            #successful validation
            if result == 1:
                return render_template("7-userfunc.html", error="")
            else:
                error = "Cannot register, try again"
                return render_template("3-reguseronly.html", error= error)


# Continue with register_vistor...






@app.route("/to_visitor_register")
def to_visitor_register():
    """
    Takes user to visitor register page
    """
    return render_template('4-regvisit.html', error="")

@app.route("/to_employee_register")
def to_employee_register():
    """
    Takes user to employee register page
    """
    return render_template('5-regemp.html', error="")

@app.route("/to_emp_visitor_register")
def to_emp_visitor_register():
    """
    Takes user to employee-visitor register page
    """
    return render_template('6-regempvisit.html', error="")

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
        hash_password()
    	login_response = login(_name, _password)

    	if login_response == 0:
            return render_template("login_test-bootstrapped.html", error = "Cannot login, try again.")
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
            return render_template("login_test-bootstrapped.html", error = "Cannot login, try again.")

@app.route("/back", methods=['GET'])
def backButton():

    #implement logic for sending user back to their corresponding functionality
    return render_template("login_test-bootstrapped.html", error="Cannot login, try again.")


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
