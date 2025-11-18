from fastapi import APIRouter,Depends,HTTPException
import schemas,models,database,dependency
from sqlalchemy.orm import Session
from blog.repository import orders
from typing import List
from models import User
from authentication import login
from blog import oauth2

router=APIRouter(
    prefix='/order',
    tags=['Orders']
)

 
@router.get("/", response_model=list[schemas.OrderResponse])
def get_orders(db: Session = Depends(database.get_db),
                   current_user = Depends(oauth2.admin_required())):
    return orders.get_orders(db,current_user)

@router.post("/user")
def create_order(request: schemas.orderbase,db: Session = Depends(database.get_db),
                 current_user = Depends(oauth2.get_current_user)):
    return orders.create_order(request,db,current_user)


@router.delete('/delete/{id}')
def delete(id,db:Session=Depends(database.get_db)):
    return orders.delete(id,db)


@router.post('/verify')
def verify_OTP(request:schemas.verify_OTP,db:Session=Depends(database.get_db)):
    return orders.verify_OTP(request,db)


@router.post('/order_otp', response_model=schemas.order_delivery)
def OTP(request: schemas.OrderOTPRequest, db: Session = Depends(database.get_db)):
    return orders.create_otp(request.order_id, db)


@router.put("/{order_id}")
def update_order(order_id: int, data: dict, db: Session = Depends(database.get_db)):
    return orders.update_order(order_id,data,db)

@router.get("/",response_model=schemas.OrderResponse)
def get_order(order_id:int,current_user = Depends(oauth2.get_current_user),db:Session = Depends(database.get_db)):
    return orders.get(order_id,current_user,db)


@router.get("/all-orders", response_model=List[schemas.OrderResponse])
def get_all_orders(db: Session = Depends(database.get_db)):
    return orders.get_all_orders(db)


@router.get("/my-orders", response_model=List[schemas.OrderResponse])
def get_my_orders(current_user = Depends(oauth2.get_current_user),db: Session = Depends(database.get_db)):
    return orders.get_my_orders(current_user, db)
