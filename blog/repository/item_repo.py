from fastapi import HTTPException,Depends
from sqlalchemy.orm import Session
import models,schemas
from blog import oauth2


def create_item(request:schemas.itemcreate,db:Session,current_user = Depends(oauth2.admin_required())):
    if current_user.role != "admin" :
        raise HTTPException(status_code=404,detail='only admin can access')
    data=models.Items(pro_id=request.pro_id,
                      item_name=request.item_name,
                      product=request.product,
                      quan_and_qual=request.quantity,
                      price=request.price )
    db.add(data)
    db.commit()
    db.refresh(data)
    return data

def show_item(db:Session,current_user = Depends(oauth2.get_current_user)):
    data=db.query(models.Items == current_user).all()
    return data

# def showid(pro_id:int,item_name:str,db:Session):
#     data=db.query(models.Items).filter(models.Items.pro_id==pro_id,models.Items.item_name==item_name).all()
#     return data

def update_item(id:int,request:schemas.itemcreate,db:Session,current_user = Depends(oauth2.admin_required())):
    if current_user.role != "admin" :
        raise HTTPException(status_code=404,detail='only admin can access')
    item=db.query(models.Items).filter(models.Items.id==id).first()
    if not item:
        raise HTTPException(status_code=404,detail="Not found")
    item.pro_id=request.pro_id
    item.item_name=request.item_name
    item.product=request.product
    item.quantity=request.quantity
    item.price=request.price
    item.user_id=request.user_id
    db.commit()
    db.refresh(item)
    return ('Updated successfully')

def delete_item(id:int,db:Session,current_user = Depends(oauth2.admin_required())):
    if current_user.role != "admin" :
        raise HTTPException(status_code=404,detail='only admin can access')
    data=db.query(models.Items).filter(models.Items.id==id).delete()
    if not data:
        raise HTTPException(status_code=404,detail='Not Found')
    db.commit()
    return ('Deleted successfully')