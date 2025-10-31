from fastapi import APIRouter

order_controller = APIRouter(prefix="/orders", tags=["Orders"])

@order_controller.get("/", status_code=200)
async def get_all_orders():
    return {"message": "Orders route working!"}