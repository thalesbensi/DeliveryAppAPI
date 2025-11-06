from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.api.common.dependencies.dependencies import get_session
from src.api.modules.orders.models import Order
from src.api.modules.orders.schemas import OrderSchema

router = APIRouter(prefix="/orders", tags=["Orders"])

@router.get("/", status_code=200)
async def get_all_orders():
    return {"message": "Orders route working!"}

@router.post("/", status_code=201)
async def create_order(order: OrderSchema, session: Session = Depends(get_session)):
    new_order = Order(user_id=order.user_id)
    session.add(new_order)
    session.commit()
    return {"message": f"ID: {order.user_id} Order created successfully!"}
