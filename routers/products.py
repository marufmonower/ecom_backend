from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from typing import List
import schemas,crud

router = APIRouter(prefix="/products",tags=["Products"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/",response_model=schemas.ProductOut)
def create(product:schemas.ProductCreate,db:Session=Depends(get_db)):
    return crud.create_product(db,product)


@router.get("/",response_model=List[schemas.ProductOut])
def read_all(db:Session=Depends(get_db)):
    return crud.get_products(db)