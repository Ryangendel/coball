from flask import Flask
from flask_sqlalchemy import SQLAlchemy

connectionString ='sqlite:///C:\\Users\\NT_WIN10\\Desktop\\Coball\\Website\\testDatabase.db'

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = connectionString
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)