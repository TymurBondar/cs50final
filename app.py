from flask import Flask, render_template, request, session, redirect
import sqlite3
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)

@app.route('/')
def index():
    if request.method == "GET":
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
            con.close()
            return render_template("home.html", username = username)

    return render_template ("register.html")

@app.route('/login', methods=["GET", "POST"])
def login():
    return render_template ("login.html")