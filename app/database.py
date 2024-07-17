# app/database.py
import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = os.getenv("DATABASE_URL", "")

engine = create_engine(
    DATABASE_URL,
    future=True,
    pool_size=500,
    max_overflow=500,
    pool_timeout=30,
    pool_recycle=3600,
)
SessionFactory = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_database():
    session = SessionFactory()
    try:
        yield session
    finally:
        session.close()
