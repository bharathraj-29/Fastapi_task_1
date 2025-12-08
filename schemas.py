from pydantic import BaseModel,EmailStr
from typing import Optional,Literal
from datetime import datetime

class itembase(BaseModel):
    item_name:str
    product:str
    price:str

class itemcreate(itembase):
    pro_id:int
    # user_id: int
    quantity:str

    class Config:
        orm_mode = True


class Userbase(BaseModel):
    name:str
    ph_no:int
    address:str

class UserCreate(Userbase):
    email:EmailStr
    password:str
    role: Literal["user", "admin", "org"] = "user"

    class Config:
        orm_mode = True


class orderbase(BaseModel):
    item_id:int
    # user_id:int

class Ordercreate(BaseModel):
    ord_id:int
    user_det: Userbase
    item_det: itembase

    class Config:
        orm_mode = True

class OrderResponse(BaseModel):
    id: int
    user: Optional[Userbase]
    item: Optional[itembase]

    class Config:
        orm_mode = True
        

class login(BaseModel):
    email:EmailStr
    password:str


class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: str | None = None