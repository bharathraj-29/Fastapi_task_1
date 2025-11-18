from fastapi import FastAPI
from database import base,engine
import uvicorn,authentication
from blog.router import user,item,orders


base.metadata.create_all(bind=engine)
app=FastAPI()

app.include_router(user.router)
app.include_router(item.router)
app.include_router(orders.router)
app.include_router(authentication.router)
# app.include_router(login.router)


if __name__=='__main__':
    uvicorn.run('main:app',port=8011)