#https://flask-migrate.readthedocs.io/en/latest/
# $ python manage.py db init
# $ python manage.py db migrate
# $ python manage.py db upgrade
# $ python manage.py db --help
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from baseApp import app,db

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

class ContactForm(db.Model):
    contactId = db.Column(db.Integer, primary_key=True)
    firstName  = db.Column(db.String(45))
    lastName = db.Column(db.String(45))
    email = db.Column(db.String(45))
    organization = db.Column(db.String(45))
    phoneNumber = db.Column(db.String(45))
    message = db.Column(db.String(1000))


if __name__ == '__main__':
    manager.run()