from enum import Enum
from datetime import datetime

from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base

from app.config import DATABASE_URL

Base = declarative_base()


def connect_db():
    engine = create_engine(DATABASE_URL, connect_args={'check_same_thread': False})
    session = Session(bind=engine.connect())
    return session


class StreamStatus(Enum):
    PLANED = 'planed'
    ACTIVE = 'active'
    CLOSED = 'closed'


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String)
    password = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    nickname = Column(String)
    created_at = Column(String, default=datetime.utcnow())

    def __str__(self):
        return f'[{self.id}]{self.email}'

    def get_filtered_data(self):
        return {
            'email': self.email,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'nickname': self.nickname,
            'created_at': self.created_at
        }


class AuthToken(Base):
    __tablename__ = 'auth_token'
    id = Column(Integer, primary_key=True)
    token = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    created_at = Column(String)


class Stream(Base):
    __tablename__ = 'stream'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    title = Column(String)
    topic = Column(String)
    status = Column(String, default=StreamStatus.PLANED.value)
    description = Column(String)
    created_at = Column(String, default=datetime.utcnow())

    def __str__(self):
        return f'{self.id} - {self.title}[{self.topic}]'
