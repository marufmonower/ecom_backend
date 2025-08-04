from fastapi import APIRouter

router = APIRouter(prefix="/orders",tags=["orders"])

@router.get("/")
def read_orders():
    return {"message":"List of orders"}