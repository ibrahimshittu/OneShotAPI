from fastapi import Depends, FastAPI, HTTPException, status
from jose import JWTError, jwt
from datetime import datetime, timedelta
from typing import Optional
from .. import schemas
from OneShot.Dependencies import users
from sqlalchemy.orm import Session
import secrets

SECRET_KEY = "70da40ffc09cc0d1a5004a738005d13153116f9f4f1557414e6bf722c29e7cad"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_HOURS = 48

PASSWORD_RESET_TOKEN: str = secrets.token_urlsafe(32)
ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def verify_token(db: Session, token: str, credentials_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
        token_data = schemas.TokenData(email=email)
    except JWTError:
        raise credentials_exception
    user = users.get_user(db, email=token_data.email)
    if user is None:
        raise credentials_exception
    return user


def generate_password_reset_token(email: str) -> str:
    delta = timedelta(hours=ACCESS_TOKEN_EXPIRE_HOURS)
    now = datetime.utcnow()
    expires = now + delta
    exp = expires.timestamp()
    encoded_jwt = jwt.encode(
        {"exp": exp, "nbf": now, "sub": email}, PASSWORD_RESET_TOKEN, algorithm="HS256",
    )
    return encoded_jwt


def verify_password_reset_token(token: str) -> Optional[str]:
    try:
        decoded_token = jwt.decode(
            token, PASSWORD_RESET_TOKEN, algorithms=["HS256"])
        return decoded_token["sub"]
    except jwt.JWTError:
        return None
