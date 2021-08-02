from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .. import schemas, database, models
from OneShot.Dependencies import contests

from .oauth2 import get_current_active_user, get_current_user


router = APIRouter(tags=['Contests'])

get_db = database.get_db


# Get all conests
@router.get("/contests/", status_code=status.HTTP_201_CREATED, response_model=List[schemas.show_create_contest_List])
def show_contest(db: Session = Depends(get_db)):
    return contests.all_contests(db)


# create a new contest
@router.post("/create_contest", status_code=status.HTTP_201_CREATED)
def create_contest(contest_details: schemas.create_contest, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):

    new_contest = models.create_contest(
        contest_name=contest_details.contest_name, contest_description=contest_details.contest_description,
        contest_prize=contest_details.contest_prize, contest_category=contest_details.contest_category, end_date=contest_details.end_date,
        start_date=contest_details.start_date, published=contest_details.published, owner_id=current_user)
    db.add(new_contest)
    db.commit()
    db.refresh(new_contest)
    return new_contest

    # return contests.create(contest_details=contest_details, db=db, current_user=user_id)


# Get contest by ID
@router.get('/contest/{id}', response_model=schemas.show_create_contest_List)
async def show_contest(id: int, db: Session = Depends(get_db)):
    return contests.show(id, db)


# Update contest by ID
@router.put('/update_contest/{id}', status_code=status.HTTP_202_ACCEPTED)
async def update_contest(id: int, contest_details: schemas.create_contest, db: Session = Depends(get_db)):
    return contests.update(id, contest_details, db)


# Delete contest by ID
@router.delete('/delete_contest/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_contest(id: int, db: Session = Depends(get_db)):
    return contests.delete(id, db)


@router.get("/essay_contests")
async def essay_contests(db: Session = Depends(get_db)):
    return contests.essay_contest(db)


@router.get("/video_contests")
async def video_contests(db: Session = Depends(get_db)):
    return contests.video_contest(db)


@router.get("/image_contests")
async def image_contests(db: Session = Depends(get_db)):
    return contests.image_contest(db)
