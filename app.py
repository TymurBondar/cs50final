from flask import Flask, render_template, request, session, redirect
from flask_session import Session
import sqlite3
from werkzeug.security import check_password_hash, generate_password_hash
from helpers import login_required
import os

app = Flask(__name__)

#uses filesistem instead of cookies
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route('/')
def index():
    if request.method == "GET":
        session.clear()
        return render_template ("index.html")

@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        # Connect to SQLite3 database and execute the SELECT
        with sqlite3.connect('typefaster.db') as con:
            cur = con.cursor()
            cur.execute("SELECT username FROM users WHERE username = ?;", (username,))
            rows = cur.fetchall()
        
        if not username or not password or not confirmation:
            error_statement = "All fields must be filled"
            return render_template("error.html", error_statement = error_statement)         

        elif len(rows) != 0:
            error_statement = "Username already exists"
            return render_template("error.html", error_statement = error_statement)

        elif confirmation != password:
            error_statement = "Password doesn't match the confirmation"
            return render_template("error.html", error_statement = error_statement)
        else:
            "add username to the database"
            hash = generate_password_hash(password)
            cur.execute("INSERT INTO users(username, password_hash) VALUES (?, ?)", (username, hash))
            con.commit()
            cur.execute("SELECT rowid FROM users WHERE username = ?;", (username,))
            rows = cur.fetchall()
            session["user_id"] = rows[0][0]
            con.close()
            return redirect ("/home")

    return render_template ("register.html")

@app.route('/login', methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username and password were submitted
        if not request.form.get("username") or not request.form.get("password"):
            error_statement = "All fields must be filled"
            return render_template("error.html", error_statement = error_statement) 

        # Query database for username
        con = sqlite3.connect("typefaster.db")
        con.row_factory = sqlite3.Row

        cur = con.cursor()
        cur.execute("SELECT rowid, * FROM users WHERE username = ?;", (request.form.get("username"),))
        rows = cur.fetchall()
        result_list = []
        for row in rows:
            result_dict = {
            "id": row["rowid"],
            "username": row["username"],
            "password_hash": row["password_hash"]}
            result_list.append(result_dict)

        con.close()
        # Ensure username exists and password is correct
        if len(result_list) != 1 or not check_password_hash(result_list[0]["password_hash"], request.form.get("password")):
            error_statement = "invalid username and/or password"
            return render_template ("error.html", error_statement = error_statement)

        # Remember which user has logged in
        session["user_id"] = rows[0]["rowid"]

        # Redirect user to home page
        return redirect("/home")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route('/home')
@login_required
def home():
    user_id = session['user_id']
    con = sqlite3.connect("typefaster.db")
    con.row_factory = sqlite3.Row

    cur = con.cursor()
    cur.execute("SELECT username FROM users WHERE rowid = ?;", (user_id,))
    res = cur.fetchall()
    username = res[0]["username"]
    con.close()

    return render_template("home.html", username = username)

@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")