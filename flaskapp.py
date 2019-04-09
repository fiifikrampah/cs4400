# This app connects the html render templates to the flask app
from api import *
from database import *
from flask import Flask, render_template, json, request, Response
from decimal import Decimal

app = Flask(__name__)
logged_user = ""
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
    return render_template('login.html', error = "")

@app.route("/to_user_register")
def to_user_register():
    """
    Takes user to user register page
    """
    return render_template('user_register.html', error="")

@app.route("/to_visitor_register")
def to_visitor_register():
    """
    Takes user to visitor register page
    """
    return render_template('visitor_register.html', error="")

@app.route("/to_employee_register")
def to_employee_register():
    """
    Takes user to employee register page
    """
    return render_template('employee_register.html', error="")

@app.route("/to_emp_visitor_register")
def to_emp_visitor_register():
    """
    Takes user to employee-visitor register page
    """
    return render_template('emp_visitor_register.html', error="")

@app.route("/to_login")
def to_login():
    """
    Takes user to login page
    """
    global logged_user
    logged_user = ""
    return render_template("login.html", error = "")

@app.route("/sign_in", methods =['POST', 'GET'])
def sign_in():
	 """
    This function signs the user in with given credentials
    Makes call to python wrapper, and logs user in 
    or displays appropriate error message
    """
    #read the posted values from the UI:
    if request.method == "POST":
    	_name = request.form["username"]
    	_password = request.form["password"]
    	login_response = login(_name, _password)

    	if login_response == 1:
    		global logged_admin
    		logged_admin = _name
    		return render_template("admin.html", error = "")

    	elif login_response == 2:
    		global logged_admin_visitor
    		logged_admin_visitor = _name
    		return render_template("admin_visitor.html", error = "")

    	elif login_response == 3:
    		global logged_manager
    		logged_manager = _name
    		return render_template("manager.html", error = "")



