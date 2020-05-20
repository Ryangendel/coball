from flask import Flask, render_template, request
from baseApp import app, db
from Model import ContactForm
from flask_mail import Mail,Message

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/Services")
def services():
    return render_template("services.html")

@app.route("/Contact", methods = ['GET','POST'])
def contact():
    if request.method == 'POST':
        mailer = Mail(app)
        _recipients = None
        newContact: ContactForm = ContactForm(
            firstName = request.form["firstName"],
            lastName = request.form["lastName"],
            email = request.form["email"],
            organization = request.form["organization"],
            phoneNumber = request.form["phoneNumber"],
            message = request.form["message"]
        )
        
        if app.config['DEBUG']:
            _recipients = app.config["ADMIN_MAIL_LIST"]
        else:
            _recipients = [newContact.email]
        
        try:
            db.session.add(newContact)
            db.session.commit()
            thankYouMessage = Message(
                sender=app.config['MAIL_USERNAME'],
                recipients = _recipients,
                body = "We got your message"
            )
            mailer.send(thankYouMessage)
            adminMessage = Message(
                sender=app.config['MAIL_USERNAME'],
                recipients = app.config["ADMIN_MAIL_LIST"],
                body = f"New Contact from {newContact.firstName} {newContact.lastName}\n{newContact.email}\n{newContact.phoneNumber}\n{newContact.organization}\n{newContact.message}"
            )
            try:
                mailer.send(adminMessage)
                return render_template("contactResponse.html")
            except:
                return "Mail ERROR"
        except Exception as e:
            print(e)
            return f"DB Error\n\n {e}"
    else:
        return render_template("contact.html")

@app.route("/Rollman")
def rollMan():
    return render_template("rollMan.html")