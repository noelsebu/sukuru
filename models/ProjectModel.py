from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from .UserModel import User
from config.common import Base

class Project(Base):
    __tablename__ = 'project'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    project_name = Column(String)
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True), onupdate=func.now())
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User')



