'''
SQLAlchemy - an ORM(OBJECT-Relational Mappers),..a code library to bridge relational db and python objects..also, vice versa.
provides abstraction and helps developer writes python code rather than SQL for CRUD op.
Core component - session
'''
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
#dialect+driver+username+password+host+dbname
DATABASE_URL = "mysql+pymysql://root:@localhost/period_tracker"
#pymysql = python to mysql translator
#Engine connects python code to actual db...Alchemy's db gateway

engine = create_engine(DATABASE_URL, echo=True)#An object of Engine class is instantiated using the create_engine() function
#URL looking string is db's address
#echo=true: print all SQL Queries


#session - temporary workspace for db stuff
#2 things to do - commit(to save) and rollback when anything goes wrong
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)#custom session..instance of a live db session
#needed for smoother connection to db
#bind=engine...Tells sessions which database to talk to

Base = declarative_base()#declarative_base() is a fn that returns a special base class..it returns a class we'll use to define tables/models

#this is necessary for OOP - db binding
#would be defining classes that'll later become db tables
#Base is the blueprint
