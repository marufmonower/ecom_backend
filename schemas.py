from pydantic import BaseModel,EmailStr
from typing import Optional

class UserCreate(BaseModel):
    email:EmailStr
    password:str

class UserOut(BaseModel):
    id:int
    email: EmailStr
    
    class Config:
        orm_mode = True

class ProductCreate(BaseModel):
    title :str
    description :Optional[str]
    price : float
    
class ProductOut(ProductCreate):
    id:int
    
    class Config:
        orm_mode = True
        
class CartItemCreate(BaseModel):
    user_id: int
    product_id: int
    quantity:int
    
class CartItemOut(CartItemCreate):
    id:int
    
    class Config:
        orm_mode = True
        
        