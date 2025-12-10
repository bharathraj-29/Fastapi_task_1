from fastapi import HTTPException,Depends
from sqlalchemy.orm import Session
import models,schemas
from hashing import Hash
from blog import oauth2

def create_user(request: schemas.UserCreate, db: Session):
  role = db.query(models.Role).filter(models.Role.role =="user").first()
  if not role:
        raise HTTPException(status_code=404, detail= "Role not found")
  new_user = models.User(
        name=request.name,
        address=request.address,
        ph_no=request.ph_no,
        email=request.email,
        password=Hash.bcrypt(request.password),
        role_id=role.id,
        role=role )
  
  db.add(new_user)
  db.commit()
  db.refresh(new_user)
  return  ("User created successfully")


# def delete(id:int,db:Session):
#     data=db.query(models.User).filter(models.User.id==id).delete()
#     if not data: 
#         raise HTTPException(status_code=404,detail='Not Found')
#     db.commit()
#     return ('Deleted successfully')

def get_user(db: Session, current_user: models.User = Depends(oauth2.get_current_user)):
    user = db.query(models.User).filter(models.User.id == current_user.user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
   

# def show(db:Session, current_user: models.User = Depends(oauth2.get_current_user)):
#     data=db.query(models.User == current_user).all()
#     return data

def update(request:schemas.UserCreate,db:Session, current_user: models.User = Depends (oauth2.get_current_user)):
    user=db.query(models.User).filter(models.User.id==current_user.user_id).first()
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