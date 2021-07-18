from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .. import schemas, database, models
from ..hashing import *


def register(user_details: schemas.User, db: Session):
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
