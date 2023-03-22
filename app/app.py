import os

from .database import Database
from .models import Settings
from .repositories import SettingsRepository
from .services import SettingsService
from .api import Api
from .menu import Menu
from .exceptions import ResponseException, DadataException


class App:

    def __init__(self) -> None:
        pass

    def run() -> None:
        db = Database()
        db.create_database()
        repository = SettingsRepository(db.session)
        service = SettingsService(repository)
        settings: Settings = service.get_first()
        menu = Menu()

        while not menu.exit_flag:
            menu.start_window()
            if menu.view_settings is True:
                print(settings)
                menu.view_settings = False

            if menu.secret_key != None:
                service.update_secret_key(
                    settings=settings, secret_key=menu.secret_key)

            if menu.token != None:
                service.update_token(
                    settings=settings, token=menu.token)

            if menu.cleaner_url != None:
                service.update_cleaner_url(
                    settings=settings, url=menu.cleaner_url)

            if menu.suggestions_url != None:
                service.update_suggestions_url(
                    settings=settings, url=menu.suggestions_url)

            if menu.lang != None:
                service.update_language(
                    settings=settings, language=menu.lang)

            if menu.address is not None:
                api = Api(settings.cleaner_url, settings.suggestions_url,
                          settings.token, settings.secret_key)

                try:
                    response_suggestions = api.suggest_address(
                        menu.address, settings.language)

                except ResponseException:
                    print(
                        "Доступ к запрошенному ресурсу запрещен\nПроверьте правильность ввода токена и секретного ключа")

                except DadataException:
                    print("Ошибка. Проверьте правильность url для автодополнения")

                else:

                    if menu.output_all_addresses(response_suggestions):
                        id_address = menu.get_coordinates_by_id(
                            response_suggestions["suggestions"])

                        try:
                            response_geocode = api.geocode_address(
                                response_suggestions["suggestions"][id_address]["value"])

                        except ResponseException:
                            print(
                                "Доступ к запрошенному ресурсу запрещен\nПроверьте правильность ввода токена и секретного ключа")

                        except DadataException:
                            print(
                                "Ошибка. Проверьте правильность url для геокодирования")

                        else:
                            os.system("cls")
                            print("Адрес: ", response_geocode[0]["result"])
                            print("Широта: ", response_geocode[0]["geo_lat"])
                            print("Долгота: ", response_geocode[0]["geo_lon"])

                menu.address = None

        os.system("cls")
        db.close()
