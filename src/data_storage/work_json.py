import json

from src.data_storage.work_with_file import WorkWithFile


class WorkJSON(WorkWithFile):
    """
    Класс для работы с JSON файлом
    """

    def add_vacancies(self, file: list[object, ...]) -> None:
        list_vacancies = []
        """
        Функция принимает список объектов класса
        и записывает их в формате JSON

        :param file: (list) файл JSON
        """
        for el in file:
            if el.salary_from == el.salary_to == 0:
                salary = 'Зарплата не указана...'
            else:
                salary = el.salary_from or el.salary_to

            vacancies = {
                "name": el.name,
                "city": el.city,
                "salary": salary,
                "requirement": el.requirements,
                "url": el.link
            }
            list_vacancies.append(vacancies)

        with open("./data/hh_vacancies.json", "w", encoding='utf-8') as f:
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