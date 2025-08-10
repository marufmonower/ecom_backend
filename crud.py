from sqlalchemy.orm import Session
import models,schemas,auth
from schemas import CartItemCreate

def create_user(db:Session,user:schemas.UserCreate):
    hashed_pw = auth.hash_password(user.password)
    db_user = models.User(email=user.email,hashed_password=hashed_pw)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)


def get_user_by_email(db:Session,email:str):
    return db.query(models.User).filter(models.User.email == email).first()

def create_product(db:Session,product:schemas.ProductCreate):
    db_product = models.Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def get_products(db:Session):
    return db.query(models.Product).all()    


def add_to_cart(db:Session,item:CartItemCreate):
    db_item = models.CartItem(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def get_cart_items_by_user(db:Session,user_id:int):
    return db.query(models.CartItem).filter(models.CartItem.user_id == user_id).all()

def remove_cart_item(db:Session,item_id:int):
    db_item = db.query(models.CartItem).filter(models.CartItem.id == item_id).first()
    
    if db_item:
        db.delete(db_item)
        db.commit()
    return db_item