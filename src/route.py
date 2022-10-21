from app import app
from db import db
from flask import Flask
from flask import render_template, request, redirect, flash, url_for, session, send_file
from werkzeug.security import check_password_hash

from data import generate_barchart, generate_pie, get_monthly
from queries import db_get_date, db_register, db_login, db_add_expense, db_update_logged_in


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

    db_register(username, password, db)

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

        user = db_login(username, db)

        if user:
            hash = user.password

            if check_password_hash(hash, password):
                session['user_id'] = user.id
                db_update_logged_in(user.id, db)
                info = db_get_date(user.id, db)
                return render_template("main.html", username=username, info=info)

        flash("username or password wrong, please try again!")
        return redirect(request.referrer)

@app.route("/logout")
def logout():
    del session['user_id']
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

    db_add_expense(name, category, date, amount, info, db, session['user_id'])
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

@app.route("/view_month")
def view_month():
    svg_file = generate_barchart(session["user_id"])

    return send_file(svg_file, mimetype='image/png')