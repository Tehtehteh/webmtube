import datetime

from sqlalchemy import create_engine, Column, Integer, String, DateTime,\
    Float, CheckConstraint, ForeignKey, PrimaryKeyConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.sql import func

from config import DB_ENGINE

engine = create_engine(DB_ENGINE)

Base = declarative_base()

# TODO: Use scoped_session
Session = sessionmaker(bind=engine)


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer(), primary_key=True, autoincrement=True)
    user = Column(String(64))

    def __init__(self, user):
        self.user = user

    def __str__(self):
        return self.user


class Comment(Base):
    __tablename__ = 'comments'
    __table_args__ = (PrimaryKeyConstraint('user', 'text', 'date', 'webm'),)
    user = Column(Integer, ForeignKey('users.user'))
    webm = Column(String(32), ForeignKey('WEBM.md5'))
    text = Column(String(length=200))
    date = Column(DateTime(), server_default=func.now())

    def __init__(self, user, text, date, webm):
        self. user = user
        self.webm = webm
        self.text = text
        self.date = date

    def __str__(self):
        return "{}:{}".format(self.user, self.text[:20])


class WEBM(Base):
    __tablename__ = 'WEBM'
    # __table_args__ = (CheckConstraint(func.length('md5')==32),)
    md5 = Column(String(32), primary_key=True)
    size = Column(Integer())
    time_created = Column(DateTime(), server_default=func.now())
    screamer_chance = Column(Float(), nullable=True)

    # TODO: Define to_dictionary for JSON serialization
    def to_dict(self):
        return {'md5': self.md5, 'size': self.size, 'time_created': self.time_created.isoformat(),
                'scream_chance': self.screamer_chance}

    def __init__(self, md5, size, screamer_chance=None):
        self.md5 = md5
        self.size = size
        self.screamer_chance = screamer_chance

    def __repr__(self):
        return "<WEBM(md5={}, size={}, time_created={}, screamer_chance={})>".format(self.md5, self.size,
                                                                                     self.time_created,
                                                                                     self.screamer_chance)
