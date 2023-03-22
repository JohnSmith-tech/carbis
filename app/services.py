from .repositories import SettingsRepository
from .models import Settings


class SettingsService:

    def __init__(self, settings_repository: SettingsRepository) -> None:
        self._repository: SettingsRepository = settings_repository

    def get_first(self) -> Settings:
        return self._repository.get_first()

    def update_cleaner_url(self, settings: Settings, url: str) -> None:
        self._repository.update_cleaner_url(settings, url)

    def update_suggestions_url(self, settings: Settings, url: str) -> None:
        self._repository.update_suggestions_url(settings, url)

    def update_token(self, settings: Settings, token: str) -> None:
        self._repository.update_token(settings, token)

    def update_language(self, settings: Settings, language: str) -> None:
        self._repository.update_language(settings, language)

    def update_secret_key(self, settings: Settings, secret_key: str) -> None:
        self._repository.update_secret_key(settings, secret_key)
