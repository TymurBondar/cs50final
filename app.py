from flask import Flask, render_template, request, session, redirect
from flask_session import Session
import sqlite3
from werkzeug.security import check_password_hash, generate_password_hash
from helpers import login_required, render_error

app = Flask(__name__)

# Use filesystem instead of cookies for sessions
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Database connection function
def get_db_connection():
    return sqlite3.connect("typefaster.db")

@app.route('/')
def index():
    session.clear()
    return render_template("index.html")

@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        if not username or not password or not confirmation:
            return render_error("All fields must be filled")

        with get_db_connection() as con:
            cur = con.cursor()
            cur.execute("SELECT username FROM users WHERE username = ?;", (username,))
            if cur.fetchone():
                return render_error("Username already exists")

            if confirmation != password:
                return render_error("Password doesn't match the confirmation")

            hashed_password = generate_password_hash(password)
            cur.execute("INSERT INTO users(username, password_hash) VALUES (?, ?)", (username, hashed_password))
            con.commit()
            cur.execute("SELECT rowid FROM users WHERE username = ?;", (username,))
            user_id = cur.fetchone()[0]
            session["user_id"] = user_id

        return redirect("/home")

    return render_template("register.html")

@app.route('/login', methods=["GET", "POST"])
def login():
    session.clear()

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if not username or not password:
            return render_error("All fields must be filled")

        with get_db_connection() as con:
            cur = con.cursor()
            cur.execute("SELECT rowid, username, password_hash FROM users WHERE username = ?;", (username,))
            user_data = cur.fetchone()

            if user_data and check_password_hash(user_data[2], password):
                session["user_id"] = user_data[0]
                return redirect("/home")

        return render_error("Invalid username and/or password")

    return render_template("login.html")

@app.route('/home')
@login_required
def home():
    user_id = session['user_id']

    with get_db_connection() as con:
        cur = con.cursor()
        cur.execute("SELECT username FROM users WHERE rowid = ?;", (user_id,))
        user_data = cur.fetchone()
        cur.execute("SELECT * FROM games ORDER BY score DESC LIMIT 5;")
        games = cur.fetchall()
        if user_data:
            username = user_data[0]
        else:
            username = None

    return render_template("home.html", username=username, games = games)

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

@app.route("/game", methods = ["GET", "POST"])
@login_required
def game():
    return render_template("game.html")

@app.route("/save_res", methods = ["POST"])
@login_required
def save_res():
    user_id = session['user_id']
    data = request.get_json()
    res = data.get('res')
    accuracy = data.get('accuracy')
    #save values to db.
    with get_db_connection() as con:
        cur = con.cursor()
        cur.execute("SELECT username FROM users WHERE rowid = ?;", (user_id,))
        username = cur.fetchone()
        cur.execute("INSERT INTO games(username, result, accuracy) VALUES (?, ?, ?)", (username[0], res, accuracy))
        con.commit()
    return ("success")