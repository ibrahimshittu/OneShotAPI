from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from . import models
from .database import engine
from .routers import contests, users, comments, submissions


models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="OneShot - The Contest Platform",
    description="A contest patform to host, and particpate in contests",
    version="0.1",
)

origins = [
    "http://localhost.tiangolo.com",
    "http://127.0.0.1:8000/",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(contests.router)
app.include_router(users.router)
app.include_router(submissions.router)
app.include_router(comments.router)


# make submissin, based on contest, and user
# @app.post('/contest/{id}/make_submission')
# async def make_submission(id: int, db: Session = Depends(get_db)):
#     contest = db.query(models.create_contest).filter(
#         models.create_contest.id == id).first()
#     return contest


# @app.get('/contest/essay_contest')
# async def essay_contest(db: Session = Depends(get_db)):
#     contest = db.query(models.create_contest).filter(
#         models.create_contest.contest_category == 'Essay').all()
#     return contest


# @app.get("/video_contests")
# async def video_contests():
#     return {'data': {'name': 'video_contest'}}


# @app.get("/video_contests/{contest_id}")
# async def video_contests(contest_id: int):
#     return {'data': contest_id}


# @app.get("/image_contests")
# async def image_contests():
#     return {'data': {'name': 'image_contests'}}


# @app.get("/image_contests/{contest_id}")
# async def image_contests(contest_id: int):
#     return {'data': {'name': 'image_contests'}}


# @app.get("/essay_contests/{contest_id}")
# async def essay_contests(contest_id: int):
#     return 'essay_contests'
