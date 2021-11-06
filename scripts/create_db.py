from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from app.config import DATABASE_URL


def main():
    engine = create_engine(DATABASE_URL)
    session = Session(bind=engine.connect())

    session.execute("""CREATE TABLE users (
        id INTEGER NOT NULL PRIMARY KEY, 
        email VARCHAR(256),
        password VARCHAR(512),
        first_name VARCHAR(256),
        last_name VARCHAR(256),
        nickname VARCHAR(256),
        created_at VARCHAR(64)
    );""")

    session.execute("""CREATE TABLE auth_token (
        id INTEGER NOT NULL PRIMARY KEY,
        token VARCHAR(256),
        user_id INTEGER REFERENCES users,
        created_at VARCHAR(64)
    );""")

    session.execute("""CREATE TABLE stream (
        id INTEGER NOT NULL PRIMARY KEY,
        user_id INTEGER REFERENCES users, 
        title VARCHAR, 
        topic VARCHAR,
        status VARCHAR(64),
        description VARCHAR,
        created_at VARCHAR(64)
    );""")

    session.close()


if __name__ == '__main__':
    main()
