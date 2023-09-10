from functools import wraps
from flask import session, redirect, render_template

def login_required(f):

    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function

def render_error(error_statement):
    return render_template("error.html", error_statement=error_statement)