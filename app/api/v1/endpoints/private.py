from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def read_private():
    return {"message": "private endpoint"} 