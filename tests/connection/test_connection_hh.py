import pytest
from contextlib import contextmanager


@contextmanager
def does_not_raise():
    yield


def test_connect_to_api(service):
    assert service.connect_to_api() == 200


@pytest.mark.parametrize(
    "param, expectation",
    [
        ("Python developer", does_not_raise()),
        ("Менеджер", does_not_raise()),
        ("Сантехник", does_not_raise()),
        ("", does_not_raise()),
        ("123asd123", pytest.raises(NameError))
    ]
)
def test_get_vacancies(service, param, expectation):
    with expectation:
        service.get_vacancies(param)