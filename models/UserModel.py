from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from config.common import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String, unique=True)
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True), onupdate=func.now())
    isPremium = Column(Boolean, default=False)
    premium_purchased_date = Column(DateTime(timezone=True), nullable=True)  
    premium_expiry_date = Column(DateTime(timezone=True), nullable=True)

