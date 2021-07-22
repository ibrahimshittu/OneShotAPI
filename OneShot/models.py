from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date, DateTime, Enum
from sqlalchemy.orm import relationship
from sqlalchemy_utils import EmailType, URLType
import datetime

from .schemas import create_contest
from .database import Base


class create_contest(Base):
    __tablename__ = "contests"

    id = Column(Integer, primary_key=True, index=True)
    contest_name = Column(String, unique=True, index=True)
    contest_description = Column(String)
    contest_prize = Column(String)
    contest_category = Column(String)
    start_date = Column(Date)
    end_date = Column(Date)
    published = Column(Boolean, default=True)
    created_date = Column(DateTime, default=datetime.datetime.utcnow)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="items")
    comment_items = relationship(
        "Comments", back_populates="contest_items")
    essay_sub = relationship("submission", back_populates="contest")
    # image_sub = relationship(
    #     "image_submission", back_populates="image_contest")


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(EmailType)
    password = Column(String)
    created_date = Column(DateTime, default=datetime.datetime.utcnow)
    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=False)

    items = relationship("create_contest", back_populates="owner")
    comment_items = relationship("Comments", back_populates="user_items")
    submission = relationship("submission", back_populates="contestant")

    # image_submission = relationship(
    #     "image_submission", back_populates="image_contestant")


class Comments(Base):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True, index=True)
    created_date = Column(DateTime, default=datetime.datetime.utcnow)
    is_active = Column(Boolean, default=True)
    body = Column(String)
    is_parent = Column(Integer, default=None)
    user_id = Column(Integer, ForeignKey("users.id"))
    contest_id = Column(Integer, ForeignKey("contests.id"))

    user_items = relationship("User", back_populates="comment_items")
    contest_items = relationship(
        "create_contest", back_populates="comment_items")


class submission(Base):
    __tablename__ = "Submission"

    id = Column(Integer, primary_key=True, index=True)
    created_date = Column(DateTime, default=datetime.datetime.utcnow)
    image = Column(URLType, default=None)
    body = Column(String)
    users_id = Column(Integer, ForeignKey("users.id"))
    contest_id = Column(Integer, ForeignKey("contests.id"))

    contestant = relationship("User", back_populates="submission")
    contest = relationship("create_contest", back_populates="essay_sub")
