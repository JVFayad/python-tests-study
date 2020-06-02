import pytest

from leap_year_code import is_leap_year


def test_should_return_boolean_value():
    response = is_leap_year(2020)

    assert isinstance(response, bool)


@pytest.mark.parametrize('year', [x * 400 for x in range(2, 8)])
def test_should_return_true_if_leap_year_divisible_by_400(year):
    response = is_leap_year(year)

    assert response 


@pytest.mark.parametrize('year', [x * 4 for x in range(501, 508)])
def test_should_return_true_if_leap_year_divisible_by_4_but_not_by_100(year):
    response = is_leap_year(year)

    assert response


@pytest.mark.parametrize('year', [x for x in range(2000, 2010) if x % 4])
def test_should_return_false_if_not_leap_year(year):
    response = is_leap_year(year)

    assert not response