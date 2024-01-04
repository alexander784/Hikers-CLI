from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///hikers_management.db', echo=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()
