from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from Website.config import Development,Qa,Production

# connectionString ='sqlite:///C:\\Users\\NT_WIN10\\Desktop\\Coball\\Website\\testDatabase.db'

app = Flask(__name__)

if app.config["ENV"] == 'development':
    app.config.from_object(Development)
elif app.config["ENV"] == 'qa':
    app.config.from_object(Qa)
else:
    app.config.from_object(Production)


# app.config['SQLALCHEMY_DATABASE_URI'] = connectionString
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)