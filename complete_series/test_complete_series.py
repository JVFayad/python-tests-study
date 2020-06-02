import pytest
import random

from complete_series_code import complete_series


def test_should_return_list():
    response = complete_series([])

    assert isinstance(response, list)


def test_should_return_list_with_zero_if_number_repeats():
    response = complete_series([1, 1])

    assert response == [0]


def test_should_return_ordered_list():
    response = complete_series([1, 0, 2])

    assert response == [0, 1, 2]


@pytest.mark.parametrize('series', [[random.randrange(1, 40)] for x in range(6)])
def test_should_return_full_number_list_if_incomplete(series):
    response = complete_series(series)

    assert response == [x for x in range(0, series[0] + 1)]