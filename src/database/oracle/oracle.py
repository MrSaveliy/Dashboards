# sync_db.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from config import ODB_HOST, ODB_PORT, ODB_USER, ODB_PASSWORD, ODB_NAME

# DSN для Oracle
ORACLE_DATABASE_URL = f"oracle+oracledb://{ODB_USER}:{ODB_PASSWORD}@{ODB_HOST}:{ODB_PORT}/{ODB_NAME}"

engine = create_engine(ORACLE_DATABASE_URL, echo=True)
ORACLE_SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
ORACLE_Base = declarative_base()

def get_db():
    db = ORACLE_SessionLocal()
    try:
        yield db
    finally:
        db.close()