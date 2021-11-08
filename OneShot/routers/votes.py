from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .. import schemas, database, models
from OneShot.Dependencies import contests

from .oauth2 import get_current_active_user, get_current_user

router = APIRouter(tags=['Vote'])

get_db = database.get_db


@router.post("/{contest_id}/vote/{submission_id}")
def vote(contest_id: int, submission_id: int, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    contest = db.query(models.submission).filter(
        models.submission.contest_id == contest_id).filter(
        models.submission.id == submission_id).first()
    votes = db.query(models.votes).filter(
        models.votes.user_id == current_user.id).filter(models.votes.submission_id == submission_id)
    if contest is None:
        raise HTTPException(status_code=404, detail="Submission not found")
    elif votes.first():
        votes.delete(synchronize_session=False)
        db.commit()
        return {'details': "successfully unvoted", 'vote count': votes.count()}
    else:
        vote = models.votes(user_id=current_user.id,
                            submission_id=submission_id)
        db.add(vote)
        db.commit()
        db.refresh(vote)
        return {'details': "successfully voted", 'vote count': votes.count()}
