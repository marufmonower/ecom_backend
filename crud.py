from sqlalchemy.orm import Session
import models,schemas,auth

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