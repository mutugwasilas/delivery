from fastapi import APIRouter


router = APIRouter()

@router.get("/order")
async def hello():
    return {"message": "hello from orders"}