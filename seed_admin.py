from sqlalchemy.orm import Session
from models import User, Role
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str):
    return pwd_context.hash(password)


def seed_admin(db: Session):
    admin_role = db.query(Role).filter(Role.role == "admin").first()
    if not admin_role:
        admin_role = Role(role="admin")
        db.add(admin_role)
        db.commit()
        db.refresh(admin_role)

    user_role = db.query(Role).filter(Role.role == "user").first()
    if not user_role:
        user_role = Role(role="user")
        db.add(user_role)
        db.commit()
        db.refresh(user_role)


    admin = db.query(User).filter(User.email == "gobi@gmail.com").first()
    if not admin:
        admin = User(
            name="gobi",
            email="gobi@gmail.com",
            ph_no=9876543210,
            address="Head Office",
            password=hash_password("gobi@12"),
            role_id=admin_role.id )
        
        db.add(admin)
        db.commit()

    print("Default admin created (if not existed).")
