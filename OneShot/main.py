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
