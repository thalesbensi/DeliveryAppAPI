from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.dependencies.dependencies import get_session
from src.models.order import Order
from src.schemas.order import OrderSchema

order_controller = APIRouter(prefix="/orders", tags=["Orders"])

@order_controller.get("/", status_code=200)
async def get_all_orders():
    return {"message": "Orders route working!"}

@order_controller.post("/", status_code=201)
async def create_order(order: OrderSchema, session: Session = Depends(get_session)):
    new_order = Order(user_id=order.user_id)
    session.add(new_order)
    session.commit()
    return {"message": f"ID: {order.user_id} Order created successfully!"}
