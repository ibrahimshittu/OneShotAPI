from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from datetime import datetime, time, date


class create_contest(BaseModel):
    contest_name: str
    contest_description: str
    prize: str
    start_date: date
    end_date: date
    published: Optional[bool] = False


app = FastAPI()


@app.get("/contests")
async def all_contests():
    return {'Hello': {'name': 'World'}}


@app.get("/video_contests")
async def video_contests():
    return {'data': {'name': 'video_contest'}}


@app.get("/video_contests/{contest_id}")
async def video_contests(contest_id: int):
    return {'data': contest_id}


@app.get("/image_contests")
async def image_contests():
    return {'data': {'name': 'image_contests'}}


@app.get("/image_contests/{contest_id}")
async def image_contests(contest_id: int):
    return {'data': {'name': 'image_contests'}}


@app.get("/essay_contests")
async def essay_contests():
    return 'essay_contests'


@app.get("/essay_contests/{contest_id}")
async def essay_contests(contest_id: int):
    return 'essay_contests'


@app.post("/contest")
async def create_contest(contest_details: create_contest):
    # return contest_details
    return {f"The conest name is {contest_details.contest_name}"}
