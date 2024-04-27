import json

from src.data_storage.work_with_file import WorkWithFile


class WorkJSON(WorkWithFile):
    """
    Класс для работы с JSON файлом
    """
    def add_vacancies(self, file: list[object, ...]) -> None:
        """
        Функция принимает список объектов класса
        и записывает их в формате JSON

        :param file: (list) файл JSON
        """
        list_vacancies = []
        for el in file:
            if el.salary_from == 0 and el.salary_to == 0 and el.currency is None:
                vacancies = {
                    "name": el.name,
                    "city": el.city,
                    "salary": "Зарплата не указана...",
                    "requirement": el.requirements,
                    "url": el.link
                }
                list_vacancies.append(vacancies)

            else:
                vacancies = {
                    "name": el.name,
                    "city": el.city,
                    "salary_from": el.salary_from,
                    "salary_to": el.salary_to,
                    "currency": el.currency,
                    "requirement": el.requirements,
                    "url": el.link
                }
                list_vacancies.append(vacancies)

        with open("./data/hh_vacancies.json", "w") as f:
            json.dump(list_vacancies, f, ensure_ascii=False, indent=4)

    def print_vacancies(self) -> None:
        """
        Функция печатает файл JSON который есть в файле
        """
        with open("./data/hh_vacancies.json") as f:
            f = json.dumps(json.load(f), ensure_ascii=False, indent=4)
            print(f)

    def del_vacancies(self) -> None:
        """
        Функция удаляет содержимое файла JSON
        """
        with open("./data/hh_vacancies.json", "w") as f:
            pass