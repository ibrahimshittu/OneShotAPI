from fastapi import APIRouter, Depends, status, HTTPException, File, Form, UploadFile, Body
from sqlalchemy.orm import Session
from typing import List, Optional
from .. import schemas, database, models
from OneShot.Dependencies import contests
import os
import shutil
import datetime
from .oauth2 import get_current_active_user, get_current_user
import cloudinary
import cloudinary.uploader

router = APIRouter(tags=['Submission'], prefix="/contest")

get_db = database.get_db


@router.post('/{contest_id}/submission', status_code=status.HTTP_201_CREATED)
async def submit_submission(contest_id: int, current_user: models.User = Depends(get_current_user),
                            db: Session = Depends(get_db), files: Optional[List[UploadFile]] = File(None), body: Optional[str] = None):
    contest = db.query(models.create_contest).filter(
        models.create_contest.id == contest_id).first()
    if not contest:
        return HTTPException(status_code=404, detail="Contest not found")
    else:
        if contest.start_date > datetime.date.today():
            return HTTPException(status_code=400, detail="Contest not started yet")
        if contest.end_date < datetime.date.today():
            return HTTPException(status_code=400, detail="Contest already ended")
        else:
            try:
                for files in files:

                    result = cloudinary.uploader.upload(
                        files.file, resource_type="auto")
                    url = result.get("url")

                    new_submission = models.submission(image=url, body=body,
                                                       users_id=current_user.id, contest_id=contest_id)
                    db.add(new_submission)
                    db.commit()
                    db.refresh(new_submission)
            except:
                url = None or ""

            new_submission = models.submission(image=url, body=body,
                                               users_id=current_user.id, contest_id=contest_id)

            db.add(new_submission)
            db.commit()
            db.refresh(new_submission)
    return new_submission


@router.get('/{contest_id}/submissions/', status_code=status.HTTP_200_OK, response_model=List[schemas.submission_list])
def get_submission(contest_id: int, db: Session = Depends(get_db)):
    submission = db.query(models.submission).filter(
        models.submission.contest_id == contest_id).all()
    return submission


@router.get('/{contest_id}/submission/{submission_id}', response_model=schemas.submission_list)
def get_submission_by_id(contest_id: int, submission_id: int, db: Session = Depends(get_db)):
    submission = db.query(models.submission).filter(
        models.submission.contest_id == contest_id).filter(
        models.submission.id == submission_id).first()
    if not submission:
        return HTTPException(status_code=404, detail="Submission not found")
    return submission


@router.put('/{contest_id}/submission/{submission_id}/update')
def update(contest_id: int, submission_id: int, body: Optional[str], files: Optional[List[UploadFile]] = File(None),  db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    submission = db.query(models.submission).filter(
        models.submission.contest_id == contest_id).filter(
        models.submission.id == submission_id)
    contest = db.query(models.create_contest).filter(
        models.create_contest.id == contest_id).first()
    if not submission.first():
        return HTTPException(status_code=404, detail="Submission not found")
    else:
        if contest.end_date < datetime.date.today():
            return HTTPException(status_code=400, detail="You can't update your submission, Contest already ended")
    user_submission = submission.filter(
        models.submission.users_id == current_user.id).first()
    if user_submission:
        try:
            for files in files:

                result = cloudinary.uploader.upload(
                    files.file, resource_type="auto")
                url = result.get("url")
        except:
            url = None
        submission.update({models.submission.image: url, models.submission.body: body, models.submission.users_id: current_user.id,
                           models.submission.contest_id: contest_id}, synchronize_session=False)
    else:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="You are not alowed to edit this contest")
    db.commit()
    return "Submission has updated successfully"


@router.delete('/{contest_id}/submission/{id}/delete')
def delete_submission(contest_id: int, id: int, db: Session = Depends(get_db)):
    submission = db.query(models.submission).filter(
        models.submission.contest_id == contest_id).filter(
        models.submission.id == id).first()
    if not submission:
        return HTTPException(status_code=404, detail="Submission not found")
    db.delete(submission)
    db.commit()
    return {'message': 'Submission deleted'}
