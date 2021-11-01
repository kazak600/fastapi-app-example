from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base

from app.config import DATABASE_URL

Base = declarative_base()


def main():
    engine = create_engine(DATABASE_URL)
    session = Session(bind=engine.connect())

    session.execute('CREATE TABLE stream (stream_id INTEGER NOT NULL PRIMARY KEY, title VARCHAR, topic VARCHAR);')

    session.close()


if __name__ == '__main__':
    main()
