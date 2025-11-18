from fastapi import APIRouter,Depends,HTTPException
import schemas,models,database
from sqlalchemy.orm import Session
from blog.repository import item
from typing import List

router=APIRouter(
    prefix='/items',
    tags=['Items']
)

@router.post('/post',response_model=schemas.itemcreate)
def create(request:schemas.itemcreate,db:Session=Depends(database.get_db)):
    return item.create(request,db)

@router.get('/get',response_model=list[schemas.itemcreate])
def show(db:Session=Depends(database.get_db)):
    return item.show(db)

@router.get('/get/{id}',response_model=list[schemas.itemcreate])
def showid(pro_id:int,item_name:str,db:Session=Depends(database.get_db)):
    return item.showid(pro_id,item_name,db)

@router.put('/put/{id}')
def update(id:int,request:schemas.itemcreate,db:Session=Depends(database.get_db)):
    return item.update(id,request,db)

@router.delete('/del/{id}')
def delete(id:int,db:Session=Depends(database.get_db)):
    return item.delete(id,db)