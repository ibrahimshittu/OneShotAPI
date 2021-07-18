from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .. import schemas, database, models
from ..hashing import *
from OneShot.Dependencies import users

router = APIRouter(tags=['Users'])

get_db = database.get_db


@router.post('/register', status_code=status.HTTP_201_CREATED)
async def create_user(user_details: schemas.User, db: Session = Depends(get_db)):
    return users.register(user_details, db)


@router.get('/user/{id}', response_model=schemas.Show_user)
async def get_user(id: int, db: Session = Depends(get_db)):
    return users.user(id, db)
