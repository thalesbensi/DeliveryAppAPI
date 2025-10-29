from fastapi import FastAPI, APIRouter

app = FastAPI(title="Delivery App API")

from auth_routes import auth_router
from order_routes import order_router

app.include_router(auth_router)
app.include_router(order_router)