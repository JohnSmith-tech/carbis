
class TestTaskException(Exception):
    """Базовый класс исключений"""


class DadataException(TestTaskException):
    """Базовый класс исключений для API Dadata"""


class ResponseException(DadataException):
    """Класс исключений для ошибочных ответов от Dadata"""
