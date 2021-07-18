from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .. import schemas, database, models
from OneShot.Dependencies import contests


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


@router.post('/{contest_id}/submission')
def submit_submission(contest_id: int, users_id: int, submission_details: schemas.essay_submission, db: Session = Depends(get_db)):
    contests_category = db.query(models.create_contest).filter(
        models.create_contest.id == contest_id)
    # contests_category2 = db.query(models.create_contest).filter(
    # models.create_contest.id == contest_id).filter(models.create_contest.contest_category == schemas.ContestType.Essay_Contest).first()

    if contests_category.filter(models.create_contest.contest_category == schemas.ContestType.Essay_Contest).first():
        new_submission = models.essay_submission(
            **submission_details.dict(), users_id=users_id, contest_id=contest_id)
    elif contests_category.filter(models.create_contest.contest_category == schemas.ContestType.Image_Contest).first():
        # new_submission = models.essay_submission(
        #     **submission_details.dict(), users_id=users_id, contest_id=contest_id)
        return "hello"
    elif contests_category.filter(models.create_contest.contest_category == schemas.ContestType.Video_Contest).first():
        # new_submission = models.essay_submission(
        #     **submission_details.dict(), users_id=users_id, contest_id=contest_id)
        return "hi"
    else:
        return HTTPException(status_code=404, detail="Contest not found")
    db.add(new_submission)
    db.commit()
    db.refresh(new_submission)
    return new_submission
