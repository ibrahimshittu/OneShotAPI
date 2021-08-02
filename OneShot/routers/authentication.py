from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from starlette import status
from .. import schemas, database, models
from ..hashing import Hash

from datetime import datetime, timedelta
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from .token import create_access_token, ACCESS_TOKEN_EXPIRE_MINUTES


router = APIRouter(tags=["authentication"], prefix="/authentication")


@router.post('/login')
async def login(user_details: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(
        models.User.email == user_details.username).first()
    if user:
        if not Hash.verify_password(user_details.password, user.password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid password", headers={"WWW-Authenticate": "Bearer"})
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid email or password", headers={"WWW-Authenticate": "Bearer"})

    # generate jwt token and return it
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}
