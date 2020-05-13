from flask import Flask, render_template, request
from Website.baseApp import app, db
from Website.Model import ContactForm

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/Services")
def services():
    return render_template("services.html")

@app.route("/Contact", methods = ['GET','POST'])
def contact():
    if request.method == 'POST':

        newContact: ContactForm = ContactForm(
            firstName = request.form["firstName"],
            lastName = request.form["lastName"],
            email = request.form["email"],
            organization = request.form["organization"],
            phoneNumber = request.form["phoneNumber"],
            message = request.form["message"]
        )
        try:
            db.session.add(newContact)
            db.session.commit()
            return render_template("contactResponse.html")
        except Exception as e:
            print(e)
            return "DB ERROR"
        

    else:
        return render_template("contact.html")