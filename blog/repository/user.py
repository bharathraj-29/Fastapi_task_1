from fastapi import HTTPException
from sqlalchemy.orm import Session
import models,schemas
from hashing import Hash


def create(request:schemas.UserCreate,db:Session):
    # items = db.query(models.Items).filter(models.Items.id == request.item_id).first()
    # if not items:
    #     raise HTTPException(status_code=404,detail='Not found')
    data = models.User(name=request.name,
                       address=request.address,
                       ph_no=request.ph_no,
                       role=request.role,
                       email=request.email,
                       password=Hash.bcrypt(request.password))
    
    db.add(data)
    db.commit()
    db.refresh(data)
    return data

# def delete(id:int,db:Session):
#     data=db.query(models.User).filter(models.User.id==id).delete()
#     if not data: 
#         raise HTTPException(status_code=404,detail='Not Found')
#     db.commit()
#     return ('Deleted successfully')

def get_user(id: int, db: Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
   

def show(db:Session):
    data=db.query(models.User).all()
    return data

def update(id:int,request:schemas.UserCreate,db:Session):
    user=db.query(models.User).filter(models.User.id==id).first()
    if not user:
        raise HTTPException(status_code=404,detail="Not found")
    user.name=request.name
    user.ph_no=request.ph_no
    user.address=request.address
    user.role=request.role
    user.email=request.email
    user.password=Hash.bcrypt(request.password)
    db.commit()
    db.refresh(user)
    return ('Updated successfully')