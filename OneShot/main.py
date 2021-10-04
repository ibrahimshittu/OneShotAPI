from OneShot.routers import authentication
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from . import models
from .database import engine
from .routers import contests, users, comments, submissions, authentication, oauth2, votes


models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="OneShot - The Contest Platform",
    description="The Development of OneShot -The Contest Platform's API. This is a contest platform that connects 3 types or groups of users. It is intended to act as a creative hub for contest sponsors (individuals and corporates) that seek to crowd-source solutions to creativity problems.",
    version="0.1",
)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(authentication.router)
app.include_router(users.router)
app.include_router(contests.router)

app.include_router(submissions.router, dependencies=[
                   Depends(oauth2.oauth2_scheme)])
app.include_router(comments.router, dependencies=[
                   Depends(oauth2.oauth2_scheme)])
app.include_router(votes.router)
