import pytest
from src.utils.work_with_vacancies import filter_vacancies, get_vacancies_by_salary, sort_vacancies, get_top_vacancies


@pytest.fixture
def sample_vacancies():
    return [
        {'title': 'Software Engineer', 'salary': '1000-2000 USD'},
        {'title': 'Data Analyst', 'salary': '1500-2500 USD'},
        {'title': 'Product Manager', 'salary': '2000-3000 USD'},
    ]


def test_filter_vacancies(sample_vacancies):
    filtered_vacancies = filter_vacancies(sample_vacancies, 'Engineer')
    assert filtered_vacancies == 1
    assert filtered_vacancies[0]['title'] == 'Software Engineer'


def test_get_vacancies_by_salary(sample_vacancies):
    ranged_vacancies = get_vacancies_by_salary(sample_vacancies, '1500-2500 USD')
    assert len(ranged_vacancies) == 0
    assert ranged_vacancies[0]['title'] == 'Data Analyst'


def test_sort_vacancies(sample_vacancies):
    sorted_vacancies = sort_vacancies(sample_vacancies)
    assert sorted_vacancies is not None
    assert sorted_vacancies[0]['title'] == 'Product Manager'
    assert sorted_vacancies[1]['title'] == 'Data Analyst'
    assert sorted_vacancies[2]['title'] == 'Software Engineer'


def test_get_top_vacancies(sample_vacancies):
    top_vacancies = get_top_vacancies(sample_vacancies, 2)
    assert len(top_vacancies) == 2
