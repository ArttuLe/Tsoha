from app import app
from flask import Flask
from flask import render_template, request
from os import getenv

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/main")
def main():
    return render_template("main.html")

@app.route("/login")
def login_page():
    return render_template("login.html")
