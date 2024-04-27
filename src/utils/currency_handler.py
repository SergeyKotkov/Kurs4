import json


def get_currency_transfer(currency: str) -> str:
    """
    Функция для перевода валют на русское обозначение
    принимает строковое отображение валюты,
    возвращает строковое отображение валюты на русском

    :param currency: (str) стандартное обозначение валюты
    :return: (str) русский перевод валюты
    """
    with open("./data/name_currencies.json") as f:
        f = json.load(f)
        return f.get(currency)