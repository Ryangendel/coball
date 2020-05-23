from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from config import Development,Qa,Production
rootDirectory = os.path.dirname(os.path.realpath(__file__))

app = Flask(__name__)

if app.config["ENV"] == 'development':
    app.config.from_object(Development)
elif app.config["ENV"] == 'qa':
    app.config.from_object(Qa)
else:
    app.config.from_object(Production)


app.config['SQLALCHEMY_DATABASE_URI'] = app.config["DATABASE_URL"]
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


