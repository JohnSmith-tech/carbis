import os


class Menu:

    def __init__(self) -> None:
        self.cleaner_url: str = None
        self.suggestions_url: str = None
        self.secret_key: str = None
        self.token: str = None
        self.lang: str = None
        self.view_settings: bool = False
        self.exit_flag: bool = False
        self.address: str = None

    def start_window(self) -> None:
        """Главное меню"""

        choice = input("1 - Просмотр пользовательских настроек\n"
                       "2 - Настройки\n"
                       "3 - Получить координаты по введенному адресу\n"
                       "4 - Выход\n")

        if choice:
            os.system("cls")

        if choice == "1":
            self.view_settings = True

        elif choice == "2":
            os.system("cls")
            self.settings()

        elif choice == "3":
            self.input_address()

        elif choice == "4":
            self.exit_flag = True
            return

    def input_address(self):
        """Ввод адреса"""

        self.address = input("Введите адрес: ")

    def output_all_addresses(self, data) -> bool:
        """Вывод полученных адресов от api"""

        if len(data['suggestions']) == 0:
            print("Адреса не обнаружена\n")
            return False
        else:
            for i in range(len(data['suggestions'])):
                print(i+1, ")", data["suggestions"][i]["value"], end="\n")
        return True

    def get_coordinates_by_id(self, data):
        """Получение индекса адреса"""
        while True:
            choice = input("Введите номер адреса: ")
            if choice.isalpha():
                print("Вы ввели неверный номер")
            elif int(choice) <= len(data) and int(choice) > 0:
                return int(choice) - 1

    def settings(self):
        """Меню настроек"""

        while True:
            choice = input("Настройки\n"
                           "1 - Изменить url для автодополнения\n"
                           "2 - Изменить url для геокодирования\n"
                           "3 - Изменить токен\n"
                           "4 - Изменить секретный ключ\n"
                           "5 - Изменить язык\n"
                           "6 - Выход в главное меню\n")
            if choice:
                os.system("cls")

            if choice == "1":

                while True:
                    self.suggestions_url = input(
                        "Введите новый Url для автодополнения: ")
                    os.system("cls")
                    if self.suggestions_url != '':
                        break

                print("Url для автодополнения изменен\n")

            elif choice == "2":

                while True:
                    self.cleaner_url = input(
                        "Введите новый Url для геокодирования: ")
                    os.system("cls")
                    if self.cleaner_url != '':
                        break

                print("Url для геокодирования изменен\n")

            elif choice == "3":
                self.token = input("Введите новый токен: ")
                os.system("cls")
                print("Токен изменен\n")

            elif choice == "4":
                self.secret_key = input("Введите новый секретный ключ: ")
                os.system("cls")
                print("Секретный ключ изменен\n")

            elif choice == "5":

                while True:
                    choice_lang = input(
                        "Выберите язык ответов на запросы:\n1 - ru\n2 - en\n")

                    if choice_lang:
                        os.system("cls")

                    if choice_lang == "1":
                        self.lang = "ru"
                        break

                    elif choice_lang == "2":
                        self.lang = "en"
                        break
                    else:
                        print("Данные введены неверно!\n")

                print("Язык выбран\n")

            elif choice == "6":
                return
