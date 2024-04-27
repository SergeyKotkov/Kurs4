import re

from src.utils.currency_handler import get_currency_transfer


class Vacancy:
    def __init__(self, name, city, salary_from, salary_to, currency, requirements, link):
        self.name = name
        self.city = city

        if salary_from:
            self.salary_from = salary_from
        else:
            self.salary_from = 0

        if salary_to:
            self.salary_to = salary_to
        else:
            self.salary_to = 0

        self.currency = currency
        self.requirements = requirements
        self.link = link

    def __repr__(self):
        """
        Магический метод для отображения объекта
        в понятном для пользователя виде

        :return: (str) строковое отображение объекта
        """
        if self.salary_from == 0 and self.salary_to == 0 and self.currency is None:
            return (f"\n{"-" * 50}\n\n"
                    f"Название вакансии: {self.name}\n"
                    f"Город: {self.city}\n"
                    f"Заработная плата: Зарплата не указана...\n"
                    f"Требования: {re.sub(r'<.*?>', '', self.requirements)}\n"
                    f"Ссылка на вакансию: {self.link}")
        else:
            return (f"\n{"-" * 50}\n\n"
                    f"Название вакансии: {self.name}\n"
                    f"Город: {self.city}\n"
                    f"Заработная плата: {self.salary_from}-{self.salary_to} {self.currency}.\n"
                    f"Требования: {re.sub(r'<.*?>', '', self.requirements) if self.requirements else "Нету"}\n"
                    f"Ссылка на вакансию: {self.link}")

    def __eq__(self, other: object) -> bool:
        """
        Магический метод который проверяет
        равны ли два объекта

        :param other: (object) объект класса с которым сравнивать
        :return: (bool) True | False
        """
        return self.salary_from == other.salary_from

    def __lt__(self, other):
        """
        Магический метод который проверяет
        какой из объектов больше

        :param other: (object) объект класса с которым сравнивать
        :return: (bool) True | False
        """
        return self.salary_from < other.salary_from

    def __gt__(self, other):
        """
        Магический метод который проверяет
        какой из объектов меньше

        :param other: (object) объект класса с которым сравнивать
        :return: (bool) True | False
        """
        return self.salary_from > other.salary_from

    @classmethod
    def cast_to_object_list(cls, vacancies: list[dict, ...] | dict) -> list[object, ...]:
        """
        Класс метод который создает новый объект
        этого класса по полученным данным в поле (vacancies)

        :param vacancies: (list[dict, ...) данные
        :return: (list[object, ...) список объектов
        """
        list_vacancies = []
        try:
            for el in vacancies:
                if el.get("salary"):
                    list_vacancies.append(cls(el.get("name"),
                                              el.get("area").get("name"),
                                              el.get("salary").get("from"),
                                              el.get("salary").get("to"),
                                              get_currency_transfer(el.get("salary").get("currency")),
                                              el.get("snippet").get("requirement"),
                                              el.get("alternate_url")
                                              ))

                else:
                    list_vacancies.append(cls(el.get("name"),
                                              el.get("area").get("name"),
                                              0,
                                              0,
                                              None,
                                              el.get("snippet").get("requirement"),
                                              el.get("alternate_url")
                                              ))
        except TypeError:
            pass

        return list_vacancies