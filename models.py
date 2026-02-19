from db import Base
from sqlalchemy import Column,Integer,String,DateTime,Text
from datetime import datetime

class User(Base):
    __tablename__="users"
    id=Column(Integer,primary_key=True,index=True)
    user_name=Column(String,index=True)
    email=Column(String,index=True)
    password=Column(String)
    API_KEY=Column(String)
