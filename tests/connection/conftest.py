import pytest
from src.vacancy.vacancies_hh import VacanciesHH


@pytest.fixture
def service():
    work_service = VacanciesHH()
    return work_service