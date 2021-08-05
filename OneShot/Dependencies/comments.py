from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional
from .. import schemas, database, models

get_db = database.get_db


def create(comment_details, contest_id: int, is_parent: Optional[int], current_user: int, db: Session = Depends(get_db)):
    new_comment = models.Comments(user_id=current_user,
                                  contest_id=contest_id, is_parent=is_parent, **comment_details.dict())
    db.add(new_comment)
    db.commit()
    db.refresh(new_comment)
    return new_comment


def show(contest_id: int, id: int, db: Session = Depends(get_db)):
    comment = db.query(models.Comments).filter(
        models.create_contest.id == contest_id).filter(
        models.Comments.id == id).first()
    childcomment = db.query(models.Comments).filter(
        models.create_contest.id == contest_id).filter(
        models.Comments.is_parent == id).all()

    if not comment:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"comment with id {id} not available!")
    else:

        return comment, {"reply": childcomment}
    # else:
    #     if not comment:
    #         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
    #                             detail=f"comment with {id} not available!")
    #     else:
    #         return comment, {"reply": childcommment}


def delete(id: int, current_user: int, db: Session = Depends(get_db)):
    comments = db.query(models.Comments).filter(
        models.Comments.id == id).first()
    if not comments:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f'comment with id {id} not found')
    else:
        contest = db.query(models.create_contest).filter(
            models.Comments.id == id).filter(models.Comments.user_id == current_user).first()
        if contest:
            db.query(models.Comments).filter(
                models.Comments.id == id).delete(synchronize_session=False)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail="You are not authorized to delete this comment")
    db.commit()
    return comments
