# This app connects the html render templates to the flask app
from api import *
from database import *
from flask import Flask, render_template, json, request, Response
from decimal import Decimal

app = Flask(__name__)
logged_regular_user = ""
logged_admin = ""
logged_admin_visitor = ""
logged_manager = ""
logged_manager_visitor = ""
logged_staff = ""
logged_staff_visitor = ""
logged_visitor = ""


@app.route('/')
def main():
    """
    Starts app at login screen
    """
    set_connection()
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

@app.route("/sign_in", methods =['POST', 'GET'])

# This function signs the user in with given credentials
# to the correct page based on their account type.
# Makes call to python wrapper, and logs user in 
# or displays appropriate error message
  
#read the posted values from the UI:
def sign_in():
    if request.method == 'POST':
        _name = request.form["username"]
        _password = request.form["password"]
    	login_response = login(_name, _password)

    	if login_response == 1:
    		global logged_regular_user
    		logged_regular_user = _name
    		return render_template("7-userfunc.html", error = "")

    	elif login_response == 2:
    		global logged_admin
    		logged_admin = _name
    		return render_template("8-adminfunc.html", error = "")

    	elif login_response == 3:
    		global logged_admin_visitor
    		logged_admin_visitor = _name
    		return render_template("9-adminvisitfunc.html", error = "")

        elif login_response == 4:
            global logged_manager
            logged_manager = _name
            return render_template("10-manfunc.html", error = "")

        elif login_response == 5:
            global logged_manager_visitor
            logged_manager_visitor = _name
            return render_template("11-manvisitfunc.html", error = "")

        elif login_response == 6:
            global logged_staff
            logged_staff = _name
            return render_template("12-stafffunc.html", error = "")

        elif login_response == 7:
            global logged_staff_visitor
            logged_staff_visitor = _name
            return render_template("13-staffvisitfunc.html", error = "")

        elif login_response == 8:
            global logged_visitor
            logged_visitor = _name
            return render_template("14-visitorfunc.html", error = "")
        else:
            return render_template("1-login.html", error = "Cannot login, try again.")




if __name__ == '__main__':
    app.run()
