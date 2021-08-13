from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .. import schemas, database, models
from ..hashing import *


def get_user(db: Session, email: str):
    user = db.query(models.User).filter(models.User.email == email).first()
    return user


def register(user_details: schemas.User, db: Session):
    if get_user(db, user_details.email):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail="User already exists!")
    new_user = models.User(
        name=user_details.name, email=user_details.email, password=Hash.pasword_hashing(user_details.password), is_active=user_details.is_active, is_superuser=user_details.is_superuser)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {'user created successfully', new_user}


def user(id: int, db: Session):
    get_user = db.query(models.User).filter(
        models.User.id == id).first()
    if not get_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="User not available!")
    return get_user
