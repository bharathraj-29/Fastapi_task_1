# from fastapi import APIRouter, HTTPException,Depends
# from sqlalchemy.orm import Session
# from hashing import Hash
# from jwttoken import create_access_token
# from database import get_db
# import models,schemas

# router = APIRouter()

# @router.post("/login")
# def login(request: schemas.login, db: Session = Depends(get_db)):
#     user = db.query(models.User).filter(models.User.email == request.email).first()
#     if not user:
#         raise HTTPException(status_code=404, detail="Invalid Email")

#     if not Hash.verify_password(request.password, user.password):
#         raise HTTPException(status_code=401, detail="Incorrect Password")

#     token = create_access_token({"password": user.password})
#     return {"access_token": token, "token_type": "bearer"}
