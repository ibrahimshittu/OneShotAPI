from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .. import schemas, database, models
from ..hashing import *
from OneShot.Dependencies import users
from .oauth2 import get_current_active_user, get_current_user
from .token import generate_password_reset_token
from OneShot.Dependencies import mail

router = APIRouter(tags=['Users'])

get_db = database.get_db


@router.post('/register', status_code=status.HTTP_201_CREATED)
async def create_user(user_details: schemas.User, db: Session = Depends(get_db)):
    return users.register(user_details, db)

# password recorvery email
@router.post('/password-recovery/{email}', status_code=status.HTTP_201_CREATED)
async def create_reset_password(email: str, db: Session = Depends(get_db)):
    user = users.get_user(db, email=email)
    if not user:
        raise HTTPException(
            status_code=404, detail="The user with this email does not exist in the system.")
    password_reset_token = generate_password_reset_token(email=email)
    await mail.send(email, password_reset_token)
    return {"msg": "Password recovery email sent"}


@router.get('/user/{id}', response_model=schemas.Show_user)
async def get_user(id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return users.user(id, db)


@router.get("/users/me")
async def read_users_me(current_user: schemas.User = Depends(get_current_user)):
    return current_user
