from sqlalchemy.orm import Session
from .models import Settings


class SettingsRepository():
    def __init__(self, db_session: Session) -> None:
        self.db = db_session
        self.__insert_first()

    def __insert_first(self):
        with self.db() as session:
            if not session.query(Settings).first():
                settings = Settings(cleaner_url="https://cleaner.dadata.ru",
                                    suggestions_url="https://suggestions.dadata.ru", token=None, secret_key=None, language="ru")
                session.add(settings)
                session.commit()

    def get_first(self) -> Settings:
        with self.db() as session:
            return session.query(Settings).first()

    def update_cleaner_url(self, settings: Settings, url: str) -> None:
        with self.db() as session:
            settings.cleaner_url = url
            session.commit()

    def update_suggestions_url(self, settings: Settings, url: str) -> None:
        with self.db() as session:
            settings.suggestions_url = url
            session.commit()

    def update_secret_key(self, settings: Settings, secret_key: str) -> None:
        with self.db() as session:
            settings.secret_key = secret_key
            session.commit()

    def update_token(self, settings: Settings, token: str) -> None:
        with self.db() as session:
            settings.token = token
            session.merge(settings)
            session.commit()

    def update_language(self, settings: Settings, language: str) -> None:
        with self.db() as session:
            settings.language = language
            session.merge(settings)
            session.commit()
