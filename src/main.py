import os

from fastapi import FastAPI
from passlib.context import CryptContext
from dotenv import load_dotenv

load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")

app = FastAPI(title="Delivery App API")

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

from src.api.controllers.auth_controller import auth_controller
from src.api.controllers.order_controller import order_controller

app.include_router(auth_controller)
app.include_router(order_controller)