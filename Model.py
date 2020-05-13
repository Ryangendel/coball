from sqlalchemy import *
from baseApp import app,db

class ContactForm(db.Model):
    contactId = Column(Integer, primary_key=True)
    firstName  = Column(String(45))
    lastName = Column(String(45))
    email = Column(String(45))
    organization = Column(String(45))
    phoneNumber = Column(String(45))
    message = Column(String(1000))

db.create_all()