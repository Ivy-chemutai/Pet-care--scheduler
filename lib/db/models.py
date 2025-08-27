from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

Base = declarative_base()
engine = create_engine('sqlite:///pet_care.db')
Session = sessionmaker(bind=engine)
session = Session()

class Owner(Base):
    __tablename__ = 'owners'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    
    @classmethod
    def create(cls, name, email):
        owner = cls(name=name, email=email)
        session.add(owner)
        session.commit()
        return owner
    
    @classmethod
    def get_all(cls):
        return session.query(cls).all()
    
    @classmethod
    def find_by_id(cls, id):
        return session.query(cls).filter(cls.id == id).first()
    
    def delete(self):
        session.delete(self)
        session.commit()

class Pet(Base):
    __tablename__ = 'pets'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    species = Column(String, nullable=False)
    breed = Column(String)
    age = Column(Integer)
    owner_id = Column(Integer, ForeignKey('owners.id'))
    
    @classmethod
    def create(cls, name, species, breed, age, owner_id):
        pet = cls(name=name, species=species, breed=breed, age=age, owner_id=owner_id)
        session.add(pet)
        session.commit()
        return pet
    
    @classmethod
    def get_all(cls):
        return session.query(cls).all()
    
    @classmethod
    def find_by_id(cls, id):
        return session.query(cls).filter(cls.id == id).first()
    
    def delete(self):
        session.delete(self)
        session.commit()

class CareLog(Base):
    __tablename__ = 'care_logs'
    
    id = Column(Integer, primary_key=True)
    activity = Column(String, nullable=False)
    notes = Column(String)
    timestamp = Column(DateTime, default=datetime.now)
    pet_id = Column(Integer, ForeignKey('pets.id'))
    
    @classmethod
    def create(cls, activity, notes, pet_id):
        care_log = cls(activity=activity, notes=notes, pet_id=pet_id)
        session.add(care_log)
        session.commit()
        return care_log
    
    @classmethod
    def get_all(cls):
        return session.query(cls).all()
    
    @classmethod
    def find_by_id(cls, id):
        return session.query(cls).filter(cls.id == id).first()
    
    def delete(self):
        session.delete(self)
        session.commit()

Base.metadata.create_all(engine)
