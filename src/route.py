from app import app
from flask import Flask
from flask import render_template, request, redirect, flash, url_for
from os import getenv

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/main")
def home():
    return render_template("main.html")

@app.route("/register")
def register_page():
    return render_template("register.html")

@app.route("/register_user", methods=["POST"])
def register():

    username = request.form["username"]
    password = request.form["pword"]

    flash("User registered successfully")

    return redirect(url_for('index'))

@app.route("/login")
def login_page():
    return render_template("login.html")

@app.route("/login_user", methods=["POST"])
def login():
    logged = False

    if request.method == 'POST':
        
    username = request.form["username"]
    password = request.form["pword"]

    if logged:
        return render_template("main.html")
    else:
        flash("Username or password incorrect!")
        return redirect(request.referrer)

@app.route("/add")
def add_new():
    return render_template("add_new.html")

@app.route("/add_expense", methods=["POST"])
def add_expense():
    
    name = request.form["name"]
    category = request.form["category"]
    date = request.form["date"]
    amount = request.form["amount"]
    info = request.form["info"]

    #DB execute

    flash("Submission added successfully!")

    return redirect(request.referrer)



@app.route("/view")
def view():
    return render_template("view.html")

@app.route("/view_expenses")
def view_expenses():
    pass