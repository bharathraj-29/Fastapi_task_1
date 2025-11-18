from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,relationship
from sqlalchemy.ext.declarative import declarative_base

Database_URL="mysql+mysqlconnector://root:bharath@localhost/task"
engine=create_engine(Database_URL)
SessionLocal=sessionmaker(bind=engine,autocommit=False,autoflush=False)
base=declarative_base()

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()
