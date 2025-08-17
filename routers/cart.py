from fastapi import APIRouter, Depends, HTTPException,status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer
from database import SessionLocal,get_db
from typing import List
from schemas import CartItemCreate,CartItemOut
import schemas
import models
import auth,crud


router = APIRouter(prefix="/cart", tags=["Cart"])
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="users/login")



def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/{user_id}",response_model=List[schemas.CartItemOut])
def get_cart_items(user_id: int, db: Session = Depends(get_db)):
    items = db.query(models.CartItem).filter(
        models.CartItem.user_id == user_id).all()
    return items


@router.post("/")
def add_to_cart(item: CartItemCreate,token:str=Depends(oauth2_scheme),db:Session=Depends(get_db)):        #(user_id: int, product_id: int, quantity: int, db: Session = Depends(get_db)):
    user_id = auth.verify_token(token)
    if not user_id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Invalid token")
        
    cart_item = models.CartItem(
        user_id=user_id, product_id=item.product_id, quantity=item.quantity)
    db.add(cart_item)
    db.commit()
    db.refresh(cart_item)
    return cart_item


@router.delete("/{item_id}", response_model=schemas.CartItemOut)
def delete_cart_item(item_id: int, db: Session = Depends(get_db)):
    item = crud.remove_cart_item(db, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item
