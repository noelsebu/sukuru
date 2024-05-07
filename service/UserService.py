from fastapi_sqlalchemy import DBSessionMiddleware, db
from fastapi import HTTPException
from email.utils import parseaddr

from models.UserModel import User
from dto.UserSchema import User

from models.UserModel import User as ModelUser
import re


class UserService:

    def createUser(user: User):
        if not UserService.isValidEmail(user.email):
            raise ValueError("Invalid email address")
        db_user = ModelUser(first_name=user.first_name,last_name=user.last_name,email=user.email)
        db.session.add(db_user)
        db.session.commit()
        return db_user
    
    def getUser(user_id: int):
        db_user = db.session.query(ModelUser).filter(ModelUser.id == user_id).first()
        if db_user is None:
            raise HTTPException(status_code=404, detail="User not found")
        return db_user
    
    def isValidEmail(email):
        if '@' not in parseaddr(email)[1]:
            return False
        regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(regex, email):
            return False
        return True