import pytest
from unittest.mock import patch

from src.vacancy.vacancies_hh import VacanciesHH


@pytest.fixture
def valid_hh_response():
    return {
        'items': [
            {'vacancy_name': '1'},
            {'vacancy_name': '2'},
            {'vacancy_name': '3'},
            {'vacancy_name': '4'},
    ]
    }


@pytest.fixture
def hh_client():
    return VacanciesHH()


@patch('src.vacancy.vacancies_hh.requests.get')
def test_valid_response_from_hh_returns_data(
    mock_request, hh_client, valid_hh_response
):
    mock_request.return_value.json.return_value = valid_hh_response
    mock_request.return_value.ok = True

    vacancies = hh_client.get_vacancies()

    assert vacancies == valid_hh_response['items']


@patch('src.vacancy.vacancies_hh.requests.get')
def test_if_hh_return_invalid_status_code_returns_no_vacancies(
    mock_request, hh_client, valid_hh_response
):
    mock_request.return_value.json.return_value = valid_hh_response
    mock_request.return_value.ok = False

    vacancies = hh_client.get_vacancies()

    assert vacancies == []
