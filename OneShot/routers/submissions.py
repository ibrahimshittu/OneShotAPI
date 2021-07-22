from fastapi import APIRouter, Depends, status, HTTPException, File, Form, UploadFile
from sqlalchemy.orm import Session
from typing import List, Optional
from .. import schemas, database, models
from OneShot.Dependencies import contests
import os
import shutil


router = APIRouter(tags=['Submission'], prefix="/contest")

get_db = database.get_db


@router.post('/{contest_id}/submission', status_code=status.HTTP_201_CREATED)
async def submit_submission(contest_id: int, users_id: int, body: Optional[str] = None,
                            db: Session = Depends(get_db), file: Optional[List[UploadFile]] = File(None)):
    contest = db.query(models.create_contest).filter(
        models.create_contest.id == contest_id).first()
    if not contest:
        return HTTPException(status_code=404, detail="Contest not found")
    else:
        try:
            for files in file:
                file_location = f"media/{files.filename}"
                with open(file_location, "wb") as img:
                    shutil.copyfileobj(files.file, img)

                url = f'media/{[files.filename for files in file]}'
        except:
            url = ""
        new_submission = models.submission(image=url, body=body,
                                           users_id=users_id, contest_id=contest_id)
    db.add(new_submission)
    db.commit()
    db.refresh(new_submission)
    return new_submission


@router.get('/{contest_id}/submission/', response_model=List[schemas.essay_submission_list], status_code=status.HTTP_200_OK)
def get_submission(contest_id: int, db: Session = Depends(get_db)):
    submission = db.query(models.submission).filter(
        models.submission.contest_id == contest_id).all()
    if not submission:
        return HTTPException(status_code=404, detail="Submission not found")
    return submission


@router.get('/{contest_id}/submission/{submission_id}', response_model=schemas.essay_submission_list)
def get_submission_by_id(contest_id: int, submission_id: int, db: Session = Depends(get_db)):
    submission = db.query(models.submission).filter(
        models.submission.contest_id == contest_id).filter(
        models.submission.id == submission_id).first()
    if not submission:
        return HTTPException(status_code=404, detail="Submission not found")
    return submission
