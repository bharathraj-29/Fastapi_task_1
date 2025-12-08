from fastapi import FastAPI
from database import base,engine,get_db
import uvicorn,authentication
from blog.router import user,item,orders
from seed_admin import seed_admin


base.metadata.create_all(bind=engine)
app=FastAPI()

app.include_router(user.router)
app.include_router(item.router)
app.include_router(orders.router)
app.include_router(authentication.router)
# app.include_router(login.router)

@app.on_event("startup")
def startup_event():
    base.metadata.create_all(bind=engine)

    db = next(get_db())
    seed_admin(db)

if __name__=='__main__':
    uvicorn.run('main:app',port=8011)