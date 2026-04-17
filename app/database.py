from typing import Generator

from sqlalchemy import URL, create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker, Session

from .settings import settings


url = URL.create(
    drivername="postgresql+psycopg2",
    host=settings.db_host,
    port=settings.db_port,
    username=settings.db_user,
    password=settings.db_pass,
    database=settings.db_name,
)
engine = create_engine(url)
SessionLocal = sessionmaker(engine)


def get_session() -> Generator[Session, None, None]:
    with SessionLocal() as db:
        try:
            yield db
        except Exception as e:
            db.rollback()
            raise e
        

class Base(DeclarativeBase):
    pass