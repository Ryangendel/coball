#%%
import pandas as pd
import psycopg2
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date,DateTime, Float
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import text
#%%


connectionString ='sqlite:///a:\\DataVizRepo\\RecommendedSession_01232020\\icecreamstore.sqlite'
databaseConnectionEngine = create_engine(connectionString,echo=True)

databaseSession = sessionmaker(bind=databaseConnectionEngine)
# databaseSession = scoped_session(databaseSession)

firstSession = databaseSession()

anInstanceofDeclaritiveBase = declarative_base()

class connectionInstatiator():
    def __init__(self):
        pass

    def instantiateConnection(connectionString: str):
        databaseConnectionEngine = create_engine(connectionString,echo=True)
        databaseSession = sessionmaker(bind=databaseConnectionEngine)
        firstSession = databaseSession()
        return firstSession


class IceCreamStore(anInstanceofDeclaritiveBase):

    def __init__(self,currentSession):
        self.databaseConnection = currentSession

    __tablename__ = 'icecreamstore'

    ID = Column(Integer, primary_key=True)
    Flavors = Column(String(45))
    Quantities = Column(String(45))
    Price = (Float)

    def __rep__(self):
        return f"<IceCreamStore(ID='{self.ID}',Flavors = '{self.Flavors}', Quantities = '{self.Quantities}', Price = '{self.Price}')>"

    def allFlavors(self) -> list:
        sql: str = "select * from icecreamstore"
        return self.databaseConnection.query(IceCreamStore).from_statement(text(sql)).all()
        # return firstSession.query(IceCreamStore).from_statement(text(sql)).all()

class Sharks(anInstanceofDeclaritiveBase):
    __tablename__ = 'sharks'
    def __init__(self,currentSession):
        self.databaseConnection = currentSession

    id = Column(Integer, primary_key=True)
    Case_number = Column(String(45))
    Date = Column(String(45))
    Year = Column(String)
    Type = Column(String)
    Country = Column(String)
    Area = Column(String)
    Location = Column(String)
    Activity = Column(String)
    Name = Column(String)
    Sex = Column(String)
    Age  = Column(String)
    Injury  = Column(String)
    Fatal_y_n = Column(String)
    Time = Column(String)
    Investigator_or_source = Column(String)
    pdf = Column(String)
    original_order = Column(String)
    
    def __rep__(self):
        return f"""<Shark(id='{self.id}'
        ,Case_number = '{self.Case_number}'
        ,Date = '{self.Date}'
        ,Year = '{self.Year}'
        ,Type = '{self.Type}'
        ,Country = '{self.Country}'
        ,Area = '{self.Area}', 
        ,Location = '{self.Location}'
        ,Activity = '{self.Activity}'
        ,Name = '{self.Name}'
        ,Sex = '{self.Sex}'
        ,Age = '{self.Age}'
        ,Injury = '{self.Injury}'
        ,Fatal_y_n = '{self.Fatal_y_n}'
        ,Time = '{self.Time}'
        ,Investigator_or_source = '{self.Investigator_or_source}'
        ,pdf = '{self.pdf}'
        ,original_order = '{self.original_order}'
)>"""
    def allSharks(self):
        sql: str = "select * from sharks"
        return self.databaseConnection.query(Sharks).from_statement(text(sql)).all()