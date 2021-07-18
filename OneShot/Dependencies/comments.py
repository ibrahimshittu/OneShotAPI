from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional
from .. import schemas, database, models

get_db = database.get_db


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


def delete(id: int, db: Session = Depends(get_db)):
    comments = db.query(models.Comments).filter(
        models.Comments.id == id).first()
    if not comments:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f'comment with id {id} not found')

    db.query(models.Comments).filter(
        models.Comments.id == id).delete(synchronize_session=False)
    db.commit()
    return comments
