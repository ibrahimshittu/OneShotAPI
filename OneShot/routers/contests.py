from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .. import schemas, database, models
from OneShot.Dependencies import contests

from .oauth2 import get_current_active_user, get_current_user


router = APIRouter(tags=['Contests'])

get_db = database.get_db


# Get all conests
@router.get("/contests/", status_code=status.HTTP_202_ACCEPTED, response_model=List[schemas.show_create_contest_List])
def show_contest(db: Session = Depends(get_db)):
    return contests.all_contests(db)


# Get contest by ID
@router.get('/contest/{id}', response_model=schemas.show_create_contest_List)
async def show_contest(id: int, db: Session = Depends(get_db)):
    return contests.show(id, db)


# create a new contest
@router.post("/create_contest", status_code=status.HTTP_201_CREATED)
def create_contest(contest_details: schemas.create_contest, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    return contests.create(contest_details=contest_details, db=db, current_user=current_user.id)


# Update contest by ID
@router.put('/update_contest/{id}', status_code=status.HTTP_202_ACCEPTED)
async def update_contest(id: int, contest_details: schemas.create_contest, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    return contests.update(id, contest_details, db, current_user.id)


# Delete contest by ID
@router.delete('/delete_contest/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_contest(id: int, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    return contests.delete(id, db, current_user.id)


@router.get("/essay_contests")
async def essay_contests(db: Session = Depends(get_db)):
    return contests.essay_contest(db)


@router.get("/video_contests")
async def video_contests(db: Session = Depends(get_db)):
    return contests.video_contest(db)


@router.get("/image_contests")
async def image_contests(db: Session = Depends(get_db)):
    return contests.image_contest(db)
