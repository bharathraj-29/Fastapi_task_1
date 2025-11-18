from fastapi import APIRouter,Depends,HTTPException
import schemas,models,database
from sqlalchemy.orm import Session
from blog.repository import user
from typing import List

router=APIRouter(
    prefix='/user',
    tags=['Users']
)

@router.post('/post', response_model=schemas.UserCreate)
def create(request:schemas.UserCreate, db: Session = Depends(database.get_db)):
    return user.create(request,db)

# @router.delete('/del/{id}')
# def delete(id,db:Session=Depends(database.get_db)):
#     return user.delete(id,db)

@router.get('/get/{id}',response_model=schemas.UserCreate)
def show_id(id:int,db:Session=Depends(database.get_db)):
    return user.get_user(id,db)

@router.get('/get')
def show(db:Session=Depends(database.get_db)):
    return user.show(db)

@router.put('/put/{id}')
def update(id:int,request:schemas.UserCreate,db:Session=Depends(database.get_db)):
    return user.update(id,request,db)