from .database import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.types import TIMESTAMP
from sqlalchemy.sql.expression import text
from sqlalchemy.orm import relationship

# these are the DB models for SQL Alchemy.
# if these are not set up when the app starts, it will automatically create them in postgres.

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, nullable=False, unique=True)
    username = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    bio = Column(String, nullable=True)
    website = Column(String, nullable=True)
    facebook_link = Column(String, nullable=True)
    twitter_link = Column(String, nullable=True)
    ig_link = Column(String, nullable=True)
    tiktok_link = Column(String, nullable=True)
    amazon_link = Column(String, nullable=True)
    goodreads_link = Column(String, nullable=True)
    bookbub_link = Column(String, nullable=True)
    is_author = Column(Boolean, nullable=False, server_default='False')
    genre = Column(String, nullable=True)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))

class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    wordcount = Column(Integer, nullable=False)
    booktype = Column(String, nullable=False)
    genre = Column(String, nullable=False)
    subgenre = Column(String, nullable=True)
    status = Column(String, nullable=False)
    is_complete = Column(Boolean, nullable=False, server_default='False')
    is_public = Column(Boolean, nullable=False, server_default='False')
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    updated_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))

    user_id = Column(Integer, ForeignKey('users.id', ondelete="CASCADE"), nullable=False)

    owner = relationship("User")

