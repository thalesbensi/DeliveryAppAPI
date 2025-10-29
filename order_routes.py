from fastapi import APIRouter

order_router = APIRouter(prefix="/orders", tags=["Orders"])

@order_router.get("/", status_code=200)
async def get_all_orders():
    return {"message": "Orders route working!"}