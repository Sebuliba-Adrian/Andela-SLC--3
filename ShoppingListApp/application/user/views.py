import re
from functools import wraps
from . import user_blueprint
from flask import render_template,session, redirect, request, url_for, flash
from application.models.user import User

USERS = {}

def register(name, username, password, rpt_password):
    """ This function handles user registration"""
    if name and username and password and rpt_password:
        if name.strip() and username.strip() and password.strip() and rpt_password.strip():
            if len(username) > 3 and len(username) < 11:
                if re.match("^[a-zA-Z0-9_.-]+$", username):
                    if len(password) > 5 and len(password) < 11:
                        if password == rpt_password:
                            USERS[username] = User(name, username, password)
                            return "Registration successful"
                        return "Passwords don't match"
                    return "Password should be 6 to 10 characters"
                return "Illegal characters in username"
            return "Username should be 4 to 10 characters"
        return "Blank input"
    return "None input"




def login(username, password):
    """ Handles user login """
    if username and password:
        if username.strip() and password.strip():
            if USERS.get(username):
                if USERS[username].password == password:
                    return "Login successful"
                return "Wrong password"
            return "User not found"
        return "Blank input"
    return "None input"

@user_blueprint.route('/')
def index():
    """ Handles the index route """
    if session.get('username'):
        return redirect(url_for('read_buckets'))
    else:
        return redirect(url_for('sign_in'))

@user_blueprint.route('/sign_in', methods=['GET','POST'])
def sign_in():
    if request.method == 'POST':
        result = login(request.form['username'], request.form['password'])
        if result == "Login successful":
            session['username'] = request.form['username']
            return redirect(url_for('read_items'))
        flash(result, 'warning')
    #return render_template('login.html')
    return render_template('user/index.html')

@user_blueprint.route('/sign_up', methods=['GET','POST'])
def sign_up():
    """ Handles the sign_up route """
    if request.method == 'POST':
        result = register(request.form['name'], request.form['username'], request.form['password']
                          , request.form['rpt_password'])
        if result == "Registration successful":
            flash(result, 'info')
            return redirect(url_for('sign_in'))
        flash(result, 'warning')
    return render_template('register.html')

def login_required(func):
    """ Decorator function to ensure some routes are only accessed by logged in users """
    @wraps(func)
    def decorated_function(*args, **kwargs):
        """ Modified descriprition of the decorated function """
        if not session.get('username'):
            flash('Login to continue', 'warning')
            return redirect(url_for('sign_in', next=request.url))
        return func(*args, **kwargs)
    return decorated_function

