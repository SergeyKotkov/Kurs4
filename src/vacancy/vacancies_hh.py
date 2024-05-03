import requests

from src.vacancy.work_with_api_service import WorkWithAPIService


class VacanciesHH(WorkWithAPIService):
    """
    Класс реализует подключение к сервисам поиска вакансий
    """

    def connect_to_api(self) -> int:
        """
        Функция реализует подключение к сервису hh.ru
        возвращает статус подключения к сервису

        :return: (int) статус подключения
        """
        response = requests.get("https://api.hh.ru/vacancies")

        return response.status_code

    def get_vacancies(self, keyword, page=None, salary=None):
        """
        Функция возвращает вакансии сервиса hh.ru

        если параметр (params) не передан
        по умолчанию будет поиск по всем вакансиям
        которые есть на сервисе hh.ru

        если по переданному параметру (params)
        не найдено ни одного совпадения
        пользователю вернется сообщение об ошибке

        :param param: (str) Параметры поиска вакансий
        :return: (str) файл json
        """
        url = 'https://api.hh.ru/vacancies'

        params = {
            'text': keyword,
            'per_page': page,
            'salary': salary,

        }
        response = requests.get(url.strip(), params=params)


        if not response.ok:
            print(f'Connection error, status code {response.status_code}')
            return []

        try:
            return response.json()['items']
        except KeyError:
            print(f'Invalid HH response: {response.text}')
            return []