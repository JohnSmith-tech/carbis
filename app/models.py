from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


class Base(DeclarativeBase):
    pass


class Settings(Base):
    __tablename__ = "settings"
    id: Mapped[int] = mapped_column(primary_key=True)
    cleaner_url: Mapped[str] = mapped_column(String(255), nullable=False)
    suggestions_url: Mapped[str] = mapped_column(String(255), nullable=False)
    token: Mapped[str] = mapped_column(String(255), nullable=True)
    secret_key: Mapped[str] = mapped_column(String(255), nullable=True)
    language: Mapped[str] = mapped_column(String(10), nullable=False)

    def __repr__(self) -> str:
        return f"id = {self.id}\ncleaner_url = {self.cleaner_url}\nsuggestions_url = {self.suggestions_url}\ntoken = {self.token}\nsecret_key = {self.secret_key}\nlanguage = {self.language}"
