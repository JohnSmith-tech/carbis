
import requests
import json

from .exceptions import DadataException, ResponseException


class Api:

    def __init__(self, cleaner_url: str, suggestions_url: str, token: str, secret: str = None) -> None:
        self.headers = {
            "Content-type": "application/json",
            "Accept": "application/json",
            "Authorization": f"Token {token}",
        }
        if secret:
            self.headers["X-Secret"] = secret

        self.cleaner_url = f"{cleaner_url}/api/v1/clean"
        self.suggestions_url = f"{suggestions_url}/suggestions/api/4_1/rs"

    def __send_request(self, url, data) -> dict:
        try:
            response = requests.post(
                url=url, data=json.dumps(data), headers=self.headers)
            response.raise_for_status()

        except requests.exceptions.HTTPError as error:
            raise ResponseException(str(error))

        except Exception as error:
            raise DadataException(str(error))
        else:
            return response.json()

    def suggest_address(self, address: str, lang: str):
        url = f"{self.suggestions_url}/suggest/address"
        return self.__send_request(url=url, data={"query": address, "language": lang})

    def geocode_address(self, address: str):
        url = f"{self.cleaner_url}/address"
        return self.__send_request(url=url, data=[address])
