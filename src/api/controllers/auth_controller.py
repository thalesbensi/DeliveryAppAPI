from datetime import datetime, timedelta, timezone
from http import HTTPStatus

from fastapi import APIRouter, Depends, HTTPException
from jose import jwt
from sqlalchemy.orm import Session

from src.dependencies.dependencies import get_session
from src.models.user import User
from src.main import bcrypt_context, ACCESS_TOKEN_EXPIRE_MINUTES, SECRET_KEY, ALGORITHM
from src.schemas.user import UserSchema, LoginSchema

auth_controller = APIRouter(prefix="/auth", tags=["Auth"])


def generate_token(user_id):
    expire_date = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    token_info = {"sub": user_id, "exp": expire_date}
    encoded_jwt = jwt.encode(token_info,SECRET_KEY,ALGORITHM)
    return encoded_jwt


@auth_controller.get("/", status_code=HTTPStatus.OK)
async def authenticate():
    return {"message": "Not authenticated", "Autheticate": False}

@auth_controller.post("/register", status_code=HTTPStatus.CREATED)
async def register(user: UserSchema, session: Session = Depends(get_session)):
    user_to_be_created =  session.query(User).filter(User.email == user.email).first()
    if user_to_be_created:
        raise HTTPException(status_code=400, detail="User Already Registered With this Email")
    else:
        encrypted_password = bcrypt_context.hash(user.password)
        user_to_be_created = User(user.name, user.email, encrypted_password)
        session.add(user_to_be_created)
        session.commit()
        return {f"message": f"User Created with success {user_to_be_created.email}"}

@auth_controller.post("/login", status_code=HTTPStatus.OK)
async def login(login: LoginSchema, session: Session = Depends(get_session)):
    user = session.query(User).filter(User.email == login.email).first()
    if not user:
        raise HTTPException(status_code=404, detail="User Not Found")
    elif not bcrypt_context.verify(login.password, user.password):
        raise HTTPException(status_code=400, detail="Incorrect Password")
    token = generate_token(user.id)
    return {
             "token": token,
             "token_type": "Bearer"
         }

