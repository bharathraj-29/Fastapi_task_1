from fastapi import APIRouter,Depends,HTTPException
import schemas,models,database,dependency
from sqlalchemy.orm import Session
from blog.repository import orders_repo
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
    return orders_repo.get_orders(db,current_user)


@router.post("/user")
def create_order(request: schemas.orderbase,db: Session = Depends(database.get_db),
                 current_user = Depends(oauth2.get_current_user)):
    return orders_repo.create_order(request,db,current_user)


@router.delete('/delete/{id}')
def delete_order(id,db:Session=Depends(database.get_db),current_user = Depends(oauth2.admin_required())):
    return orders_repo.delete_order(id,db,current_user)


@router.get("/",response_model=schemas.OrderResponse)
def get_order(order_id:int,current_user = Depends(oauth2.get_current_user),db:Session = Depends(database.get_db)):
    return orders_repo.get_order(order_id,current_user,db)


@router.get("/all-orders", response_model=List[schemas.OrderResponse])
def get_all_orders(db: Session = Depends(database.get_db),current_user = Depends(oauth2.admin_required())):
    return orders_repo.get_all_orders(db,current_user)


@router.get("/my-orders", response_model=List[schemas.OrderResponse])
def get_my_orders(current_user = Depends(oauth2.get_current_user),db: Session = Depends(database.get_db)):
    return orders_repo.get_my_orders(current_user, db)
