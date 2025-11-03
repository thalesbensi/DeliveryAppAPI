from http import HTTPStatus

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.dependencies.dependencies import get_session
from src.models.user import User
from src.main import bcrypt_context
from src.schemas.user import UserSchema

auth_controller = APIRouter(prefix="/auth", tags=["Auth"])

@auth_controller.get("/", status_code=HTTPStatus.OK)
async def authenticate():
    return {"message": "Not authenticated", "Autheticate": False}

@auth_controller.post("/register", status_code=HTTPStatus.CREATED)
async def user_register(user_schema: UserSchema, session: Session = Depends(get_session) ):
    user_to_be_created =  session.query(User).filter(User.email == user_schema.email).first()
    if user_to_be_created:
        raise HTTPException(status_code=400, detail="User Already Registered With this Email")
    else:
        encrypted_password = bcrypt_context.hash(user_schema.password)
        user_to_be_created = User(user_schema.name, user_schema.email, encrypted_password)
        session.add(user_to_be_created)
        session.commit()
        return {f"message": f"User Created with success {user_to_be_created.email}"}
