from http import HTTPStatus

from fastapi import APIRouter, Depends
from src.dependencies.dependencies import get_session
from src.models.user import User
from src.main import bcrypt_context

auth_controller = APIRouter(prefix="/auth", tags=["Auth"])

@auth_controller.get("/", status_code=HTTPStatus.OK)
async def authenticate():
    return {"message": "Not authenticated", "Autheticate": False}

@auth_controller.post("/register", status_code=HTTPStatus.CREATED)
async def user_register(email:str, password:str, name:str, session = Depends(get_session) ):
    user_to_be_created =  session.query(User).filter(User.email == email).first()
    if user_to_be_created:
        return {"message": "User already exists", "Autheticate": False}
    else:
        encrypted_password = bcrypt_context.hash(password)
        user_to_be_created = User(name, email, encrypted_password)
        session.add(user_to_be_created)
        session.commit()
        return user_to_be_created
