from flask import render_template, flash, redirect
from app import app

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html",active_home='active')

@app.route('/about')
def about():
    return render_template("about.html", active_about='active')

@app.route('/contact')
def contact():
    return render_template("contact.html", active_contact='active')