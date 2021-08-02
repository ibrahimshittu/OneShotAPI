from pydantic import BaseModel
from typing import Optional, List
from datetime import date, datetime
from enum import Enum

from pydantic import BaseModel, Field


class ContestType(str, Enum):
    Essay_Contest = "Essay Contest"
    Video_Contest = "Video Contest"
    Image_Contest = "Image Contest"


class create_contest(BaseModel):
    contest_name: str
    contest_description: str = Field(..., max_length=500)
    contest_prize: str
    contest_category: ContestType
    start_date: date
    end_date: date
    published: Optional[bool] = True


class create_contest_List(create_contest):
    class Config():
        orm_mode = True


class User(BaseModel):
    name: str
    email: str
    password: str
    is_active: bool = True
    is_superuser: bool = False


# shows user with the list of contests
class Show_user(BaseModel):
    name: str
    email: str
    items: List[create_contest_List] = []

    class Config():
        orm_mode = True


# shows user without the list of contests
class Show_user_List(BaseModel):
    name: str
    email: str

    class Config():
        orm_mode = True


class show_create_contest(BaseModel):
    contest_name: str
    contest_description: str
    contest_prize: str
    contest_category: str
    start_date: date
    end_date: date
    published: Optional[bool] = False
    owner: Show_user

    class Config():
        orm_mode = True


class comments(BaseModel):
    created_date = datetime
    body: str
    # is_parent: int
    is_active: bool


class show_comments(comments):
    user_items: Show_user_List

    class Config():
        orm_mode = True


class show_create_contest_List(BaseModel):
    contest_name: str
    contest_description: str
    contest_prize: str
    contest_category: str
    start_date: date
    end_date: date
    published: Optional[bool] = False
    owner: Show_user_List
    #comment_items:  List[show_comments] = []

    class Config():
        orm_mode = True


class comments_List(BaseModel):
    created_date = datetime
    body: str
    is_active: bool
    is_parent: int
    user_id: int
    contest_id: int
    user_items: Show_user_List
    contest_items: show_create_contest_List


class submission(BaseModel):
    created_date: datetime
    body: Optional[str] = None


class submission_list(submission):
    image: Optional[str] = None
    contestant: Show_user_List

    class Config():
        orm_mode = True


class UserLogin(BaseModel):
    email: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None
