from app import app
from db import db
from flask import Flask
from flask import render_template, request, redirect, flash, url_for, session, send_file
from werkzeug.security import check_password_hash, generate_password_hash

from data import generate_pie, get_monthly


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

    pass_hash = generate_password_hash(password)

    sql = "INSERT INTO users (username, password) VALUES (:username, :password)"

    db.session.execute(sql, {"username" :username, "password" :pass_hash})
    db.session.commit()

    flash("User registered successfully")

    return redirect(url_for('index'))

@app.route("/login")
def login_page():
    return render_template("login.html")

@app.route("/login_user", methods=["POST"])
def login():

    if request.method == 'POST':

        username = request.form["username"]
        password = request.form["pword"]

        query = "SELECT id,password FROM users WHERE username=:username"
        result = db.session.execute(query, {"username": username})
        
        user = result.fetchone()
        if user:
            hash = user.password
            if check_password_hash(hash, password):
                session["user_id"] = user.id
                return render_template("main.html")

        flash("username or password wrong, please try again!")
        return redirect(request.referrer)

@app.route("/logout")
def logout():
    del session["user_id"]
    return redirect("/")

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

    sql = "INSERT INTO expenses (name,amount,category,date,added,comment,user_owner) VALUES (:name,:amount,:category,:date,NOW(),:comment,:user_owner)"

    db.session.execute(sql, {"name" :name, "amount" :amount, "category" :category, "date" :date, "comment" :info,"user_owner" :session["user_id"]})
    db.session.commit()
    flash("Submission added successfully!")

    return redirect(request.referrer)

@app.route("/view")
def view():
    total = get_monthly(session['user_id'])
    return render_template("view.html", tables=[total.to_html(classes='data', index=False)], titles=total.columns.values)

@app.route("/view_expenses")
def view_expenses():
    svg_file = generate_pie(session["user_id"])

    return send_file(svg_file, mimetype='image/png')
