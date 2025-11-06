import os

from fastapi import FastAPI
from passlib.context import CryptContext
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))

app = FastAPI(title="Delivery App API")

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

from src.api.modules.users.auth_controller import router as auth_router
from src.api.modules.orders.router import router as order_router

app.include_router(auth_router)
app.include_router(order_router)