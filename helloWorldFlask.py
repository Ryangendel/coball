from flask import Flask
from Models import IceCreamStore,Sharks, connectionInstatiator
from sqlalchemy.orm import sessionmaker, scoped_session
import psycopg2
from sqlalchemy import create_engine

app = Flask(__name__)



@app.route("/")
def home():

    i = 0
    for x in range(0,10):
        i = i + x
    return "Hello World!"


@app.route("/allflavors")
def allFlavors():

    connectionString ='sqlite:///a:\\DataVizRepo\\RecommendedSession_01232020\\icecreamstore.sqlite'
    databaseConnectionEngine = create_engine(connectionString,echo=True)

    databaseSession = sessionmaker(bind=databaseConnectionEngine)

    firstSession = databaseSession()
    # firstSession.close()
    
    # conn = connectionInstatiator()
    # firstSession = conn.instantiateConnection()
    iceCreamStore = IceCreamStore(firstSession)
    # iceCreamStore = IceCreamStore()
    allTheFlavors = iceCreamStore.allFlavors()
    theView = ""
    for flavor in allTheFlavors:
        theView = theView + f"<p>{flavor.Flavors}</p>"
    return theView


@app.route("/sharks")
def allSharks():
    connectionString ='sqlite:///a:\\DataVizRepo\\RecommendedSession_01232020\\sharks.sqlite'
    databaseConnectionEngine = create_engine(connectionString,echo=True)

    databaseSession = sessionmaker(bind=databaseConnectionEngine)

    firstSession = databaseSession()

    sharks = Sharks(firstSession)
    allTheSharks = sharks.allSharks()

    theView = ""
    for sharkAttack in allTheSharks:
        theView = theView + f"<p>There was an attack on {sharkAttack.Date}</p>"
    return theView
    