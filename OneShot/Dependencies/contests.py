from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .. import schemas, database, models

get_db = database.get_db


def all_contests(db: Session):
    contest = db.query(models.create_contest).all()
    return contest


def create(contest_details, db: Session, current_user: int):
    contest_check = db.query(models.create_contest).filter(
        models.create_contest.contest_name == contest_details.contest_name).first()
    if contest_check:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail="Contest already exists!")
    new_contest = models.create_contest(
        contest_name=contest_details.contest_name, contest_description=contest_details.contest_description,
        contest_prize=contest_details.contest_prize, contest_category=contest_details.contest_category, end_date=contest_details.end_date,
        start_date=contest_details.start_date, published=contest_details.published, owner_id=current_user)
    db.add(new_contest)
    db.commit()
    db.refresh(new_contest)
    return new_contest


def show(id: int, db: Session):
    contest = db.query(models.create_contest).filter(
        models.create_contest.id == id).first()
    if not contest:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Contest not available!")
    return contest


def update(id: int, contest_details: schemas.create_contest, db: Session, current_user: int):
    contest = db.query(models.create_contest).filter(
        models.create_contest.id == id).first()
    if not contest:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f'Contest with id {id} not found')
    else:
        contest = db.query(models.create_contest).filter(
            models.create_contest.id == id).filter(models.create_contest.owner_id == current_user).first()
        if contest:
            contest = db.query(models.create_contest).filter(models.create_contest.id == id).update(
                contest_details.dict(), synchronize_session=False)
        else:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                detail="You are not alowed to edit this contest")
    db.commit()
    return "contest has updated successfully"


def delete(id: int, db: Session, current_user: int):
    contest = db.query(models.create_contest).filter(
        models.create_contest.id == id).first()
    if not contest:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f'Contest with id {id} not found')
    else:
        contest = db.query(models.create_contest).filter(
            models.create_contest.id == id).filter(models.create_contest.owner_id == current_user).first()
        if contest:
            db.query(models.create_contest).filter(
                models.create_contest.id == id).delete(synchronize_session=False)
        else:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                detail="You are not alowed to delete this contest")
    db.commit()
    return "Contest successfully deleted"


def essay_contest(db: Session):
    essay_contests = db.query(models.create_contest).filter(
        models.create_contest.contest_category == "Essay Contest").all()

    if not essay_contests:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Contest not available!")
    return essay_contests


def video_contest(db: Session):
    video_contests = db.query(models.create_contest).filter(
        models.create_contest.contest_category == "Video Contest").all()

    if not video_contests:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Contest not available!")
    return video_contests


def image_contest(db: Session):
    image_contests = db.query(models.create_contest).filter(
        models.create_contest.contest_category == "Image Contest").all()

    if not image_contests:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Contest not available!")
    return image_contests
