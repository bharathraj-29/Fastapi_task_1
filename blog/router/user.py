from fastapi import APIRouter,Depends,HTTPException
import schemas,models,database
from sqlalchemy.orm import Session
from blog.repository import user_repo
from typing import List
from blog import oauth2

router=APIRouter(
    prefix='/user',
    tags=['Users']
)

@router.post('/register', response_model=schemas.Userbase)
def create_user(request:schemas.UserCreate, db: Session = Depends(database.get_db)):
    return user_repo.create_user(request,db)

# @router.delete('/del/{id}')
# def delete(id,db:Session=Depends(database.get_db)):
#     return user.delete(id,db)

@router.get('/get/{id}',response_model=schemas.UserCreate)
def show_id(db:Session=Depends(database.get_db), current_user = Depends(oauth2.get_current_user)):
    return user_repo.get_user(db,current_user)

# @router.get('/get')
# def show(db:Session=Depends(database.get_db), current_user = Depends(oauth2.get_current_user)):
#     return user.show(db,current_user)

@router.put('/put/{id}')
def update(request:schemas.UserCreate,db:Session=Depends(database.get_db), current_user = Depends(oauth2.get_current_user)):
    return user_repo.update(request,db,current_user)