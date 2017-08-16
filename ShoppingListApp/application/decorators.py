from functools import wraps
from flask import abort, flash,session
def login_required(func):
    """ Decorator function to ensure some routes are only accessed by logged in users """
    @wraps(func)
    def decorated_function(*args, **kwargs):
        """ Modified descriprition of the decorated function """
        if not session.get('username'):
            abort(403)

        return func(*args, **kwargs)
    return decorated_function
