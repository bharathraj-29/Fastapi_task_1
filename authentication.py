from fastapi import APIRouter,HTTPException,Depends,status
from jwttoken import create_access_token
from database import engine,SessionLocal,get_db
from fastapi.security import OAuth2PasswordBearer
from hashing import Hash
from sqlalchemy.orm import Session
import models,schemas

router = APIRouter(tags=['Authentication'])

session = SessionLocal(bind=engine)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


@router.post('/login')
def login(request: schemas.login, db: Session = Depends(get_db)):

    user = db.query(models.User).filter(models.User.email == request.email).first()
    if not user:
        raise HTTPException(status_code=404, detail='Email Not Found')
    
    if not Hash.verify_password(request.password, user.password):
        raise HTTPException(status_code=404, detail='Incorrect password')

    access_token = create_access_token(
        data={"sub":user.email,"name":user.name,"ph_no":user.ph_no,"id":user.user_id})

    return {"access_token": access_token, "token_type": "bearer"}

