from fastapi import HTTPException,Depends
from sqlalchemy.orm import Session,joinedload
from datetime import datetime,timedelta
import models,schemas,database
from random import randint
from blog import oauth2


def get_orders(db,current_user = Depends(oauth2.admin_required())):
    role = db.query(models.Orders).filter(models.User.role == current_user.role).all()
    return role

def create_order(request: schemas.orderbase,db: Session = Depends(database.get_db),current_user: models.User = Depends(oauth2.get_current_user)):
    order = models.Orders(user_id=current_user.user_id,item_id=request.item_id)
    db.add(order)
    db.commit()
    db.refresh(order)
    return order

def delete(id,db:Session):
    order = db.query(models.Orders).filter(models.Orders.id==id).delete()
    if not order:
        raise HTTPException(status_code=404,detail='Not Found')
    db.commit()
    return ('Deleted Successfully')


def create_otp(order_id:int,db: Session):
    # item = db.query(models.Items).filter(models.Items.id == id).first()
    # if not item:
    #     raise HTTPException(status_code=404, detail="Item not found")

    otp = randint(100000, 999999)
    expiry = datetime.now() + timedelta(minutes=5)

    verify_OTP= models.verify_otp(
        order_id=order_id, 
        otp=otp,
        otp_expiry=expiry,
        delivered="No"
    )

    db.add(verify_OTP)
    db.commit()
    db.refresh(verify_OTP)
    return verify_OTP


def verify_OTP(request: schemas.verify_OTP, db: Session):
    order = db.query(models.Orders).filter(models.Orders.id == request.order_id).first()

    if not order:
        raise HTTPException(status_code=404, detail="Order not found")

    if order.delivery == "Yes":
        return {"message": "Order already delivered"}

    if datetime.now() > verify_OTP.otp_expiry:
        raise HTTPException(status_code=400, detail="OTP expired")

    if order.otp != request.otp:
        raise HTTPException(status_code=400, detail="Invalid OTP")
    
    order.delivery= "Yes"
    db.commit()
    return {"message": "OTP verified. Order marked as delivered."}


def update_order(order_id: int, data: dict, db: Session):
    order = db.query(models.Orders).filter(models.Orders.id == order_id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    # for key, value in data.items():
    #     setattr(order, key, value)
    db.commit()
    db.refresh(order)
    return {"message": "Order updated successfully", "order": order}


def get(order_id:int, db:Session):
    data = (db.query(models.Orders).filter(models.Orders.id == order_id)
            .options(joinedload(models.Orders.user), joinedload(models.Orders.item)).first())
    return data


def get_all_orders(db: Session):
    data = db.query(models.Orders).all()
    return data


def get_my_orders(current_user:models.User=Depends(oauth2.get_current_user), db: Session=Depends(database.get_db)):
     data=(db.query(models.Orders).filter(models.Orders.user_id == current_user.user_id)
            .options(joinedload(models.Orders.user), joinedload(models.Orders.item)).all())
     return data
