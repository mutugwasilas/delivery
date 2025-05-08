from fastapi import APIRouter


router = APIRouter(
    tags=['auth']
)

@router.get("/")
async def hello():
    return {"message" : "let the dance begin"}
