from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///hikers_management.db', echo=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

class Hiker(Base):
    __tablename__ = 'hikers'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    contact_info = Column(String)
    emergency_contact = Column(String)

class Equipment(Base):
    __tablename__ = 'equipment'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    condition = Column(String)

class Trip(Base):
    __tablename__ = 'trips'

    id = Column(Integer, primary_key=True)
    trip_name = Column(String, nullable=False)



def initialize_database():
    Base.metadata.create_all(engine)