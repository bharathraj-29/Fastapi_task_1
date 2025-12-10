from fastapi import HTTPException,Depends
from sqlalchemy.orm import Session,joinedload
from datetime import datetime,timedelta
import models,schemas,database,jwttoken
from random import randint
from blog import oauth2


def get_orders(db,current_user = Depends(oauth2.admin_required())):
    role = db.query(models.Orders).filter(models.User.role == current_user.role).all()
    return role


def create_order(request: schemas.orderbase,db: Session = Depends(database.get_db),current_user: jwttoken = Depends(oauth2.get_current_user)):
    order = models.Orders(user_id=current_user.user_id,item_id=request.item_id)
    db.add(order)
    db.commit()
    db.refresh(order)
    return order


def delete_order(id,db:Session,current_user = Depends(oauth2.admin_required())):
    order = db.query(models.Orders).filter(models.Orders.id==id).delete()
    if not order:
        raise HTTPException(status_code=404,detail='Not Found')
    db.commit()
    return ('Deleted Successfully')


def get_order(order_id:int, db:Session,current_user = Depends(oauth2.admin_required())):
    data = (db.query(models.Orders).filter(models.Orders.id == order_id)
            .options(joinedload(models.Orders.user), joinedload(models.Orders.item)).first())
    return data


def get_all_orders(db: Session,current_user = Depends(oauth2.admin_required())):
    data = db.query(models.Orders).all()
    return data


def get_my_orders(current_user:models.User=Depends(oauth2.get_current_user), db: Session=Depends(database.get_db)):
     data=(db.query(models.Orders).filter(models.Orders.user_id == current_user.user_id)
            .options(joinedload(models.Orders.user), joinedload(models.Orders.item)).all())
     return data
