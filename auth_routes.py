from fastapi import APIRouter


auth_router = APIRouter(prefix="/auth", tags=["Auth"])

@auth_router.get("/", status_code=200)
async def authenticate():
    return {"message": "Not authenticated", "Autheticate": False}