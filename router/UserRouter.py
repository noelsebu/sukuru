from fastapi import APIRouter, Depends, HTTPException
from fastapi_sqlalchemy import db


from dto.UserSchema import User as SchemaUser
from models.UserModel import User as ModelUser


from service.UserService import UserService as userService

router = APIRouter(prefix="/user", tags=["Users"])

@router.post("/create", response_model=SchemaUser)
async def create_user(user: SchemaUser):
    return userService.createUser(user)

@router.get("/{userId}", response_model=SchemaUser)
async def getUser(userId: int):
    return userService.getUser(userId)