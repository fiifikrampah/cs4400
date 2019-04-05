# This app connects the html render templates to the flask app
from api import *
from database import *
from flask import Flask, render_template, json, request, Response
from decimal import Decimal

app = Flask(__name__)
logged_user = ""
logged_admin = ""

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

