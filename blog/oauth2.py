from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from sqlalchemy.orm import Session
import models, jwttoken, schemas
from database import get_db

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    payload = jwt.decode(token, jwttoken.SECRET_KEY, algorithms=[jwttoken.ALGORITHM])
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        username: str = payload.get("sub") 
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    user = db.query(models.User).filter(models.User.email == username).first()
    if user is None:
        raise credentials_exception
    return user


def admin_required():
    def wrapper(current_user = Depends(get_current_user)):
        if current_user.role != "admin":
            raise HTTPException(
                status_code=403,
                detail="Admins only allow."
            )
        return current_user
    return wrapper
