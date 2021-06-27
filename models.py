from sqlalchemy import create_engine, Column, String, Integer, DECIMAL, ForeignKey
from sqlalchemy.orm import session, sessionmaker

engine = create_engine('sqlite:///Budget.db', echo = True)
Session = sessionmaker(bind=engine)
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class Account(Base):
   __tablename__ = 'Accounts'
   account_id = Column(Integer, primary_key=True)

   name = Column(String)
   ie_type = Column(String)
   budget=Column(DECIMAL)
   auto_post=Column(DECIMAL)
   category=Column(String)

class Transaction(Base):
   __tablename__="Transactions"
   trans_id=Column(Integer, primary_key=True)
   account_id=Column(Integer, ForeignKey('Accounts.account_id'))
   amount=Column(DECIMAL)
   period=Column(String)
   trans_date=Column(String)

class Account_Period(Base):
   __tablename__="Account_Period"
   id=Column(Integer, primary_key=True)
   account_id=Column(Integer, ForeignKey('Accounts.account_id'))
   period=Column(String)
   amount=Column(DECIMAL)
   budget=Column(DECIMAL)

class Setting(Base):
   __tablename__="Settings"
   key=Column(String, primary_key=True)
   value=Column(String)


Base.metadata.create_all(engine)