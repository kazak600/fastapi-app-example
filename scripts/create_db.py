from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base

from app.config import DATABASE_URL

Base = declarative_base()


def main():
    engine = create_engine(DATABASE_URL)
    session = Session(bind=engine.connect())

    session.execute('CREATE TABLE stream (stream_id INTEGER NOT NULL PRIMARY KEY, title VARCHAR, topic VARCHAR);')

    session.execute("""CREATE TABLE users (
        id INTEGER NOT NULL PRIMARY KEY, 
        email VARCHAR(256),
        password VARCHAR(512),
        first_name VARCHAR(256),
        last_name VARCHAR(256),
        nickname VARCHAR(256),
        created_at VARCHAR(64)
    );""")

    session.close()


if __name__ == '__main__':
    main()
