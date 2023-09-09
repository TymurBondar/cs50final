from flask import Flask, render_template, request, session, redirect

app = Flask(__name__)

@app.route('/')
def index():
    if request.method == "GET":
        return render_template ("index.html")

@app.route('/register', methods=["GET", "POST"])
def register():
    return render_template ("register.html")

@app.route('/login', methods=["GET", "POST"])
def login():
    return render_template ("login.html")