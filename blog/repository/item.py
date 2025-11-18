from fastapi import HTTPException
from sqlalchemy.orm import Session
import models,schemas

def create(request:schemas.itemcreate,db:Session):
    data=models.Items(pro_id=request.pro_id,
                      item_name=request.item_name,
                      product=request.product,
                      quan_and_qual=request.quan_and_qual,
                      price=request.price )
    db.add(data)
    db.commit()
    db.refresh(data)
    return data

def show(db:Session):
    data=db.query(models.Items).all()
    return data

def showid(pro_id:int,item_name:str,db:Session):
    data=db.query(models.Items).filter(models.Items.pro_id==pro_id,models.Items.item_name==item_name).all()
    return data

def update(id:int,request:schemas.itemcreate,db:Session):
    item=db.query(models.Items).filter(models.Items.id==id).first()
    if not item:
        raise HTTPException(status_code=404,detail="Not found")
    item.pro_id=request.pro_id
    item.item_name=request.item_name
    item.product=request.product
    item.quan_and_qual=request.quan_and_qual
    item.price=request.price
    item.user_id=request.user_id
    db.commit()
    db.refresh(item)
    return ('Updated successfully')

def delete(id:int,db:Session):
    data=db.query(models.Items).filter(models.Items.id==id).delete()
    if not data:
        raise HTTPException(status_code=404,detail='Not Found')
    db.commit()
    return ('Deleted successfully')