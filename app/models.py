from sqlalchemy import Column, Integer, String, ForeignKey, Table, create_engine
from sqlalchemy.orm import relationship, backref, Session
from sqlalchemy.ext.declarative import declarative_base

from app.config import DATABASE_URL

Base = declarative_base()


def connect_db():
    engine = create_engine(DATABASE_URL)
    session = Session(bind=engine.connect())
    return session


class Stream(Base):
    __tablename__ = 'stream'
    stream_id = Column(Integer, primary_key=True)
    title = Column(String)
    topic = Column(String)

    def __str__(self):
        return f'{self.stream_id} - {self.title}[{self.topic}]'
