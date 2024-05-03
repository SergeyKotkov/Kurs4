import sys


def filter_vacancies(list_classes: list[object, ...], word: str | None) -> list[object, ...] | None:
    word = word + ','
    try:
        if word:
            if "," not in word:
                raise ValueError("Некорректный ввод, вы забыли указать запятую - ',' !")

            name, city = word.lower().replace(" ", "").split(",")
            if name != "" and city != "":
                list_filtered_classes = [el for el in list_classes if name in el.name.lower() and city == el.city.lower()]

            elif name != "" and city == "":
                list_filtered_classes = [el for el in list_classes if name in el.name.lower()]

            elif city != "" and name == "":
                list_filtered_classes = [el for el in list_classes if city == el.city.lower()]

            else:
                raise ValueError("Не указаны ключевые слова для фильтрации")

            if len(list_filtered_classes) < 1:
                raise ValueError(f"По заданным ключевым словам ({name}, {city.capitalize()}) не найдено ни одного совпадения")


            return list_filtered_classes

        else:
            return list_classes

    except ValueError as e:
        print(e)
        sys.exit(1)


def get_vacancies_by_salary(list_classes: list[object, ...], salary_range: str) \
        -> list[object, ...] | str:
    """
    Функция сортирует список объектов по указанному диапазону зарплат,
    в случае если указанный диапазон не найден, возвращается сообщение пользователю
    о том что нужно указать другой диапазон

    :param list_classes: (list[object, ...) список объектов
    :param salary_range: (str) строковое отображение диапазона зарплат
    :return: (list[object, ...]) список отфильтрованных объектов по переданной зарплате
    """
    salary_range = salary_range + '-'
    try:
        list_filtered_classes = []
        if salary_range:
            try:
                salary_from, salary_to, currency = salary_range.lower().split("-")
            except ValueError:
                print(f"\nВы ввели больше двух аргументов - {salary_range.lower().split("-")}")

            else:
                if salary_from != "" and salary_to != "" and currency != "":
                    for el in list_classes:
                        if el.salary_from >= int(salary_from) and el.salary_to <= int(
                                salary_to) and el.currency == currency:
                            list_filtered_classes.append(el)

                    if len(list_filtered_classes) < 1:
                        raise NameError(f"\nПо данному диапазону зарплат \n"
                                        f"( от - {salary_from}, до - {salary_to}, валюта - {currency}. )\n"
                                        f"не найдено ни одного совпадения ...")


                if salary_from != "" and salary_to != "" and currency == "":
                    for el in list_classes:
                        if el.salary_from >= int(salary_from) and el.salary_to <= int(salary_to):
                            list_filtered_classes.append(el)

                    if len(list_filtered_classes) < 1:
                        raise NameError(f"\nПо данному диапазону зарплат \n"
                                        f"( от - {salary_from}, до - {salary_to} )\n"
                                        f"не найдено ни одного совпадения ...")

                if salary_from != "" and salary_to == "" and currency == "":
                    for el in list_classes:
                        if el.salary_from >= int(salary_from):
                            list_filtered_classes.append(el)

                    if len(list_filtered_classes) < 1:
                        raise NameError(f"\nПо данному диапазону зарплат \n"
                                        f"( от - {salary_from} )\n"
                                        f"не найдено ни одного совпадения ...")

                if salary_from == "" and salary_to != "" and currency != "":
                    for el in list_classes:
                        if el.salary_to <= int(salary_to) and el.currency == currency:
                            list_filtered_classes.append(el)

                    if len(list_filtered_classes) < 1:
                        raise NameError(f"\nПо данному диапазону зарплат \n"
                                        f"( до - {salary_to}, валюта - {currency}. )\n"
                                        f"не найдено ни одного совпадения ...")

                if salary_from == "" and salary_to == "" and currency != "":
                    for el in list_classes:
                        if el.currency == currency:
                            list_filtered_classes.append(el)

                    if len(list_filtered_classes) < 1:
                        raise NameError(f"\nПо данному диапазону валюты \n"
                                        f"( валюта - {currency}. )\n"
                                        f"не найдено ни одного совпадения ...")

                if salary_from == "" and salary_to != "" and currency == "":
                    for el in list_classes:
                        if el.salary_to <= int(salary_to):
                            list_filtered_classes.append(el)

                    if len(list_filtered_classes) < 1:
                        raise NameError(f"\nПо данному диапазону зарплат \n"
                                        f"( до - {salary_to} )\n"
                                        f"не найдено ни одного совпадения ...")

                if salary_from != "" and salary_to == "" and currency != "":
                    for el in list_classes:
                        if el.salary_from >= int(salary_from) and el.salary_to <= int(
                                salary_to) and el.currency == currency:
                            list_filtered_classes.append(el)

                    if len(list_filtered_classes) < 1:
                        raise NameError(f"\nПо данному диапазону зарплат \n"
                                        f"( от - {salary_from}, валюта - {currency}. )\n"
                                        f"не найдено ни одного совпадения ...")

        else:
            return list_classes

    except NameError as a:
        print(a)
    else:
        return list_filtered_classes


def sort_vacancies(list_classes: list[object, ...] | object | None) -> list[object, ...] | object:
    """
    Функция сортирует список объектов по зарплате
    от большего к меньшему

    :param list_classes: (list[object, ...] | object) список объектов или объект
    :return: (list[object, ...] | object) список отсортированных объектов или объект
    """
    try:
        sorted_list = sorted(list_classes, reverse=True)
        return sorted_list
    except TypeError:
        pass


def get_top_vacancies(list_classes: list[object, ...] | object | None, top_n: str) -> list[object, ...] | object:
    """
    Функция возвращает только то количество элементов
    которое укажет пользователь в параметре (top_n)

    если параметр (top_n) не указан
    функция вернет изначальный список (list_classes)

    если переданный параметр (top_n) больше
    чем количество элементов в списке
    пользователю вернется список всех элементов
    и сообщение о том что в списке нет указанного количества элементов

    :param list_classes: (list[object, ...]) список объектов
    :param top_n: (str) количество объектов которые нужно вернуть
    :return: (list[object, ...] | object) список объектов
    """
    try:
        if top_n:
            if int(top_n) == 0:
                raise IndexError(f"\n\nВы передали некорректное значение - {top_n}\n"
                                 f"Ошибка: невозможно вернуть {top_n} вакансий")

            else:
                try:
                    if int(top_n) > len(list_classes):
                        if len(list_classes) != 11 and len(list_classes) % 10 == 1:
                            raise IndexError(f"\n\nПо указанным параметрам мы нашли только {len(list_classes)} "
                                             f"вакансию")
                        elif 2 <= len(list_classes) <= 4:
                            raise IndexError(f"\n\nПо указанным параметрам мы нашли только {len(list_classes)} "
                                             f"вакансии")
                        else:
                            raise IndexError(f"\n\nПо указанным параметрам мы нашли только {len(list_classes)} "

                                             f"вакансий")
                except IndexError as a:
                    print(a)

                finally:
                    return list_classes[:int(top_n)]

        else:
            return list_classes

    except TypeError:
        pass
    except IndexError as a:
        print(a)


def print_vacancies(list_classes: list[object, ...] | object | None) -> None:
    """
    Функция печатает список объектов

    :param list_classes: (list[object, ...]) список объектов
    """
    try:
        for elem in list_classes:
            print(elem)
    except TypeError:
        pass