from sqlmodel import SQLModel, Session
from typing import Annotated
from fastapi import Depends
from sqlmodel import Session, create_engine
from constants.Database import SQLITE_URL 

def create_db_and_tables(engine):
    SQLModel.metadata.create_all(engine)

connect_args = {"check_same_thread": False}
engine = create_engine(SQLITE_URL, connect_args=connect_args)

def get_session():
    """
    Dependency function to yield a database session.
    """
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]