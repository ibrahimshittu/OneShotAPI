from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .. import schemas, database, models
from OneShot.Dependencies import comments
from typing import Optional
from .oauth2 import get_current_active_user, get_current_user


router = APIRouter(tags=['Comments'], prefix="/contests")

get_db = database.get_db


@router.post('/{contest_id}/comments')
def comment(comment_details: schemas.comments, contest_id: int, is_parent: Optional[int] = None, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    return comments.create(comment_details, contest_id, is_parent, current_user.id, db)


@router.get('/{contest_id}/comments/{id}')
def show_comment(contest_id: int, id: int,  db: Session = Depends(get_db)):
    return comments.show(contest_id, id, db)


@router.delete('/comments/{id}')
def delete_comment(id: int, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    return "comment successfully deleted", comments.delete(id, current_user.id, db)


# @router.post('/{comment_id}/reply')
# def reply_comment(reply_details: schemas.comment_reply, user_id: int, comment_id: int, db: Session = Depends(get_db)):
#     new_comment_reply = models.comment_reply(user_id=user_id, comment_id=comment_id,
#                                              **reply_details.dict())
#     db.add(new_comment_reply)
#     db.commit()
#     db.refresh(new_comment_reply)
#     return new_comment_reply
