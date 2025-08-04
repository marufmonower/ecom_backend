from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session
from schemas import UserCreate,UserOut
import crud,auth
from database import SessionLocal

router = APIRouter(prefix="/users",tags=["Users"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
@router.post("/register",response_model=UserOut)
def register(user:UserCreate,db:Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db,user.email)
    if db_user:
        raise HTTPException(status_code=400,detail="Email already registered")
    return crud.create_user(db,user)

@router.post("/login")
def login(user:UserCreate,db:Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db,user.email)
    if not db_user or not auth.verify_password(user.password,db_user.hashed_password):
        raise HTTPException(status_code=400,detail="Invalid credentials")
    return {"access_token":auth.fake_jwt(user.email)}
