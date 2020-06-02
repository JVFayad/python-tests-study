# encoding: utf-8
import pytest

from mastermind_code import mastermind


def test_should_return_list():
    response = mastermind(['red'], ['red'])

    assert isinstance(response, list)


def test_should_return_list_with_2_components():
    response = mastermind(['red'], ['red'])

    assert len(response) > 0


def test_should_return_int_list_components():
    response = mastermind(['red'], ['red'])

    assert isinstance(response[0], int)
    assert isinstance(response[1], int)


def test_should_return_well_placed_for_minimum_case():
    response = mastermind(['red'], ['red'])

    assert response[0] == 1
    assert response[1] == 0


def test_should_return_incorrect_for_minimum_case():
    response = mastermind(['red'], ['blue'])

    assert response[0] == 0
    assert response[1] == 0


def test_should_return_miss_placed_for_minimum_case():
    response = mastermind(['red', 'blue'], ['blue', 'yellow'])

    assert response[0] == 0
    assert response[1] == 1


def test_should_raise_value_error_if_different_len():
    with pytest.raises(ValueError):
        mastermind(['red', 'blue'], ['yellow'])
