from abc import ABC, abstractmethod


class WorkWithFile(ABC):
    @abstractmethod
    def add_vacancies(self, file: list[dict, ...]):
        pass

    @abstractmethod
    def print_vacancies(self):
        pass

    @abstractmethod
    def del_vacancies(self):
        pass