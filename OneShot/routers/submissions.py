from fastapi import APIRouter, Depends, status, HTTPException, File, Form, UploadFile
from sqlalchemy.orm import Session
from typing import List, Optional
from .. import schemas, database, models
from OneShot.Dependencies import contests
import os
import shutil


router = APIRouter(tags=['Submission'], prefix="/contest")

get_db = database.get_db


# @router.get("{contest_id}/submissions/", response_model=schemas.Submission)
# def get_submissions(contest_id: int,
#                     db: Session = Depends(get_db)):
#     """
#     Get all submissions for a given contest
#     """
#     contests_category = contest = db.query(models.create_contest).filter(
#         models.create_contest.contest_category == "Essay Contest").first()
#     try:
#         contest = db.query(models.Contest).filter(
#             models.create_contest.id == contest_id).one()
#         if contest is None:
#             raise HTTPException(status_code=404, detail="Contest not found")
#         submissions = contest.submissions
#         return schemas.SubmissionSchema(many=True).dump(submissions)
#     except HTTPException as e:
#         raise e
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))


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
        except Exception as e:
            url = ""
        new_submission = models.essay_submission(image=url, body=body,
                                                 users_id=users_id, contest_id=contest_id)
    db.add(new_submission)
    db.commit()
    db.refresh(new_submission)
    return new_submission
