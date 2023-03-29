import os

from flask import Flask
from flask import render_template
from flask import request, flash
from flask_sqlalchemy import SQLAlchemy
from flask import redirect
from model import Store
from app import app , db

import random
from sqlalchemy.sql.expression import func,select

#register
app.app_context.push()

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method=="POST":
        if not request.form["email"] or not request.form["username"] or not request.form["password"]:
            print("Please enter correct details")
            return redirect("/register")
        else:
            print(request.form["email"])
            print(request.form["username"])
            print(request.form["password"])
            result=0
            store = Store(request.form["email"],request.form["username"],request.form["password"])
            db.session.add(store)
            db.session.commit()
            return redirect("/store")
    return render_tempelate("login/register.html")

#Login
check_email=""
@app.route("/", methods=["GET","POST"])
def login():
    print("check")
    global check_email
    if request.methods=="POST":
        print(request.form["email"])
        print(request.form["psw"])
        if not request.form["email"] or not request.form["psw"]:
            print("Please enter correct details")

        else:
            email=request.form["email"]
            user = Store.query.filter_by(email=email).first()
            print(user.email)
            print(user.password)
            if(user.password==request.form["psw"]):
                print("Login successful")
                check_email = user.email
                return redirect("/store")
            
    return render_template("login/login.html")




