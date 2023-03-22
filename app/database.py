from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import Base


class Database:

    def __init__(self, db_url: str = "sqlite:///mydb.db") -> None:
        self._engine = create_engine(db_url, echo=False)
        self._session = sessionmaker(bind=self._engine)

    @property
    def session(self):
        return self._session

    def create_database(self) -> None:
        Base.metadata.create_all(self._engine)

    def close(self) -> None:
        self._session.close_all()
