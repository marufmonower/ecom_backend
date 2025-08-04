from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
import models

router = APIRouter(prefix="/cart",tags=["Cart"])

def get_db():
    db= SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
@router.get("/{user_id}")
def get_cart_items(user_id: int, db:Session=Depends(get_db)):
    items = db.query(models.CartItem).filter(models.CartItem.user_id==user_id).all()
    return items

@router.post("/")
def add_to_cart(user_id:int,product_id:int,quantity:int,db:Session = Depends(get_db)):
    cart_item = models.CartItem(user_id=user_id,product_id=product_id,quantity=quantity)
    db.add(cart_item)
    db.commit()
    db.refresh(cart_item)
    return cart_item