from sqlalchemy import Column,Integer,String,Foreignkey,Float,Boolean
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = 'products'
    id = Column(Integer,primary_key=True,index=True)
    email = Column(String,unique=True,index=True)
    hashed_password = Column(String)
    
class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer,primary_key=True,index=True)
    title = Column(String)
    description = Column(String)
    price = Column(Float)
    in_stock = Column(Boolean,default=True)
    
class CartItem(Base):
    __tablename__ = 'cart_items'
    id = Column(Integer,primary_key=True,index=True)
    user_id = Column(Integer,Foreignkey("users.id"))
    product_id = Column(Integer,Foreignkey("products.id"))
    quantity = Column(Integer)
    
class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer,primary_key=True,index=True)
    user_id = Column(Integer,Foregnkey("users.id"))
    total_price = Column(Float)
    
    

