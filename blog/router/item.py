from fastapi import APIRouter,Depends,HTTPException
import schemas,models,database
from sqlalchemy.orm import Session
from blog.repository import item_repo
from typing import List
from blog import oauth2

router=APIRouter(
    prefix='/items',
    tags=['Items']
)

@router.post('/post',response_model=schemas.itemcreate)
def create_item(request:schemas.itemcreate,db:Session=Depends(database.get_db),current_user = Depends(oauth2.admin_required())):
    return item_repo.create_item(request,db,current_user)

@router.get('/get',response_model=list[schemas.itemcreate])
def show_item(db:Session=Depends(database.get_db),current_user = Depends(oauth2.get_current_user)):
    return item_repo.show_item(db,current_user)

# @router.get('/get/{id}',response_model=list[schemas.itemcreate])
# def showid(pro_id:int,item_name:str,db:Session=Depends(database.get_db)):
#     return item.showid(pro_id,item_name,db)

@router.put('/put/{id}')
def update_item(id:int,request:schemas.itemcreate,db:Session=Depends(database.get_db),current_user = Depends(oauth2.get_current_user)):
    return item_repo.update_item(id,request,db,current_user)

@router.delete('/del/{id}')
def delete_item(id:int,db:Session=Depends(database.get_db),current_user = Depends(oauth2.get_current_user)):
    return item_repo.delete_item(id,db,current_user)