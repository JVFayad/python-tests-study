import pytest

from fizz_buzz_code import fizz_buzz


@pytest.mark.parametrize('number', [x for x in range(1, 100)])
def test_should_retun_value(number):
    result = fizz_buzz(number)

    assert result


@pytest.mark.parametrize(
    'number', 
    [x for x in range(1, 100) if not x % 3 and x % 5]
)
def test_should_retun_fizz_if_number_divisible_by_3(number):
    result = fizz_buzz(number)

    assert result == 'Fizz'


@pytest.mark.parametrize(
    'number', 
    [x for x in range(1, 100) if not x % 5 and x % 3]
)
def test_should_retun_buzz_if_number_divisible_by_5(number):
    result = fizz_buzz(number)

    assert result == 'Buzz'


@pytest.mark.parametrize(
    'number', 
    [x for x in range(1, 100) if not x % 5 and not x % 3]
)
def test_should_retun_fizz_buzz_if_number_divisible_by_3_and_5(number):
    result = fizz_buzz(number)

    assert result == 'Fizz Buzz'


@pytest.mark.parametrize(
    'number', 
    [x for x in range(1, 100) if x % 5 and x % 3]
)
def test_should_retun_number_if_number_not_divisible_by_3_and_5(number):
    result = fizz_buzz(number)

    assert result == number
